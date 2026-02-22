from datetime import datetime, timezone
from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel
import httpx
import logging

from app.core.config import settings
from app.core.security import get_optional_user, get_current_user
from app.core.database import get_users_collection

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/story", tags=["story"])

class StoryRequest(BaseModel):
    name: str
    age: int
    theme: str
    additional_params: str | None = None

class StoryResponse(BaseModel):
    story: str
    image: str
    is_demo: bool

@router.post("/generate", response_model=StoryResponse)
async def generate_story(data: StoryRequest, user: dict | None = Depends(get_optional_user)):
    """
    Генерация сказки с разграничением доступа:
    - гость (без токена) или free subscription → демо-версия
    - paid → полноценная AI-генерация
    """
    is_paid = user is not None and user.get("subscription_tier") == "paid"

    if not is_paid:
        # Ответ для гостей и бесплатных пользователей (Демо)
        demo_story = (
            f"Жил-был отважный герой по имени {data.name}, которому было всего {data.age} лет. "
            f"Однажды в чудесном мире, где главной темой было {data.theme}, произошло нечто невероятное... "
            "\n\nЭто демонстрационная версия вашей сказки. Чтобы получить полную версию — "
            "содержательную историю на 600-900 слов с уникальной моралью и потрясающей иллюстрацией — "
            "пожалуйста, активируйте магическую подписку!"
        )
        return StoryResponse(
            story=demo_story,
            image="https://images.unsplash.com/photo-1616091093714-c64882e9ab55?q=80&w=1000&auto=format&fit=crop",
            is_demo=True
        )

    # ЛОГИКА ДЛЯ ПЛАТНЫХ ПОЛЬЗОВАТЕЛЕЙ
    
    # 3.7 Ограничение (например, 10 генераций в день)
    today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    gen_stats = user.get("generation_stats", {})
    daily_count = gen_stats.get(today_str, 0)

    if daily_count >= 10:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Вы достигли ежедневного лимита генераций (10). Приходите завтра!"
        )

    if not settings.OPENAI_API_KEY:
        logger.error("OpenAI API key missing")
        raise HTTPException(status_code=500, detail="Конфигурация AI временно недоступна")

    async with httpx.AsyncClient() as client:
        try:
            # 1. Формирование продуманного промпта (3.5)
            prompt = (
                f"Напиши длинную, увлекательную детскую сказку для ребёнка по имени {data.name}, которому {data.age} лет. "
                f"Тема сказки: {data.theme}. "
                f"Дополнительные пожелания: {data.additional_params or 'нет'}. "
                "\n\nТребования к сказке:\n"
                "- Язык: простой, понятный ребенку, но богатый описаниями.\n"
                "- Структура: Четкое введение, нарастание интриги, кульминация (конфликт), мудрое решение и добрая мораль.\n"
                "- Длина: Минимум 600-900 слов.\n"
                "- Оформление: Раздели текст на логические абзацы.\n"
                "- Безопасность: Категорически избегай насилия, страшных сцен или жестокости.\n"
                "- Мораль: В конце кратко сформулируй важный жизненный урок, который дает эта история."
            )
            
            # Генерация текста
            text_response = await client.post(
                "https://api.openai.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {settings.OPENAI_API_KEY}"},
                json={
                    "model": "gpt-4",
                    "messages": [
                        {"role": "system", "content": "You are a professional children's book author with a magical and kind writing style."},
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.7,
                    "max_tokens": 2000
                },
                timeout=90.0
            )
            text_response.raise_for_status()
            res_data = text_response.json()
            story_text = res_data["choices"][0]["message"]["content"]

            # 2. Генерация картинки
            image_prompt = (
                f"High-quality digital art illustration for a children's book. "
                f"Scene: {data.theme} with a {data.age}-year-old child named {data.name}. "
                f"Atmosphere: magical, dreamy, vibrant colors, soft lighting, 8k resolution, trending on ArtStation."
            )
            
            image_response = await client.post(
                "https://api.openai.com/v1/images/generations",
                headers={"Authorization": f"Bearer {settings.OPENAI_API_KEY}"},
                json={
                    "model": "dall-e-3",
                    "prompt": image_prompt,
                    "n": 1,
                    "size": "1024x1024",
                    "quality": "standard"
                },
                timeout=60.0
            )
            image_response.raise_for_status()
            image_data = image_response.json()
            image_url = image_data["data"][0]["url"]

            # Обновление статистики пользователя
            users_coll = get_users_collection()
            users_coll.update_one(
                {"_id": user["_id"]},
                {"$set": {f"generation_stats.{today_str}": daily_count + 1}}
            )

            return StoryResponse(
                story=story_text,
                image=image_url,
                is_demo=False
            )

        except httpx.HTTPStatusError as e:
            logger.error(f"OpenAI API error: {e.response.text}")
            raise HTTPException(status_code=502, detail="AI сервис временно недоступен. Попробуйте позже.")
        except Exception as e:
            logger.exception("Unexpected error during story generation")
            raise HTTPException(status_code=500, detail="Ошибка при создании сказки. Попробуйте еще раз.")
