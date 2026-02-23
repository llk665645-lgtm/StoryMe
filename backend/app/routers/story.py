import logging
from datetime import datetime, timezone
import httpx
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from app.core.config import settings
from app.core.security import get_optional_user
from app.core.database import get_users_collection, get_items_collection

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

# Тематические изображения для демо-версии
THEME_DEMO_IMAGES = {
    "forest": ["/images/fairytales/foresttt.jpg"],
    "space": ["/images/fairytales/cosmosttt.jpg"],
    "ocean": ["/images/fairytales/oceanttt.jpg"],
    "dino": ["/images/fairytales/dinosaurttt.jpg"],
    "magic": ["/images/fairytales/fairyttt.jpg"],
    "city": ["/images/fairytales/cityttt.jpg"]
}

def get_demo_image(theme: str, name: str = "") -> str:
    import zlib
    urls = THEME_DEMO_IMAGES.get(theme, THEME_DEMO_IMAGES["magic"])
    # stable random index based on name or default to 0
    idx = zlib.adler32(name.encode()) % len(urls) if name else 0
    return urls[idx]

# Описания стилей для DALL-E 3
THEME_STYLE_MODIFIERS = {
    "forest": "enchanted woodland, watercolor style, soft morning mist, friendly forest animals",
    "space": "retro-futuristic space art, cosmic glowing stars, cute friendly aliens, nebula colors",
    "ocean": "vibrant coral reef, bright underwater light, friendly sea creatures, Disney-style animation",
    "dino": "prehistoric jungle, lush green ferns, cute baby dinosaurs, bright sunny day, Pixar style",
    "magic": "sparkling fairy dust, golden hour lighting, whimsical storybook illustration, glowing magic wand",
    "city": "comic book style, dynamic action lines, vibrant pop art, heroic pose, bright primary colors"
}

@router.post("/generate", response_model=StoryResponse)
async def generate_story(data: StoryRequest, user: dict | None = Depends(get_optional_user)):
    """
    Генерация сказки с разграничением доступа:
    - гость (без токена) или free subscription → лимит 3 сказки в день
    - paid → полноценная AI-генерация с дневными лимитами
    """
    # 1. Проверяем лимиты
    if user and user.get("email") == "admin@example.com":
        # Admin can always generate
        pass
    else:
        today = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
        stories_coll = get_items_collection()
        
        # Determine limit based on tier
        tier = user.get("subscription_tier", "free") if user else "free"
        
        if tier == "free":
            limit = 3
        elif tier == "pro":
            limit = 10
        elif tier == "enterprise":
            limit = 50
        else:
            limit = 3 # Default to 3 for safety
            
        if user:
            daily_count = await stories_coll.count_documents({
                "user_id": str(user["_id"]),
                "created_at": {"$gte": today}
            })
            
            if daily_count >= limit:
                error_type = "limit_reached" if tier == "free" else "daily_limit_reached"
                return JSONResponse(
                    status_code=403,
                    content={
                        "error": error_type,
                        "message": f"You have reached your {limit}-story daily limit. Please upgrade or come back tomorrow."
                    }
                )

    # Determine if we should use AI generation
    # tier 'paid' was used in previous code, but schema says 'pro'/'enterprise'
    is_paid = user is not None and user.get("subscription_tier") in ["paid", "pro", "enterprise"]

    if not is_paid:
        # Ответ для гостей и бесплатных пользователей (Демо)
        demo_image = get_demo_image(data.theme, data.name)
        
        demo_story = (
            f"Жил-был отважный герой по имени {data.name}, которому было всего {data.age} лет. "
            f"Однажды в чудесном мире ({data.theme}), произошло нечто невероятное... "
            "\n\n✨ Это демонстрационная версия вашей сказки. В платной подписке вы получите:\n"
            "✅ Полную историю на 8-10 страниц с захватывающим сюжетом.\n"
            "✅ Уникальную иллюстрацию, созданную специально для вашего ребенка.\n"
            "✅ Возможность сохранить сказку в свою библиотеку или распечатать ее.\n\n"
            "Хотите узнать, что случилось дальше? Активируйте магический доступ!"
        )
        
        # Save guest/free story if registered
        if user:
            stories_coll = get_items_collection()
            await stories_coll.insert_one({
                "user_id": str(user["_id"]),
                "name": data.name,
                "age": data.age,
                "theme": data.theme,
                "story_text": demo_story,
                "image_url": demo_image,
                "is_demo": True,
                "created_at": datetime.now(timezone.utc)
            })

        return StoryResponse(
            story=demo_story,
            image=demo_image,
            is_demo=True
        )

    # ЛОГИКА ДЛЯ ПЛАТНЫХ ПОЛЬЗОВАТЕЛЕЙ
    if not settings.OPENAI_API_KEY or settings.OPENAI_API_KEY == "your-api-key-here":
        # Если ключ не задан, все равно даем более качественное демо с картинками
        return StoryResponse(
            story="AI Генерация временно недоступна (не настроен API ключ). Но мы подготовили для вас эту демо-сказку!",
            image=get_demo_image(data.theme, data.name),
            is_demo=True
        )

    async with httpx.AsyncClient() as client:
        try:
            # 1. Генерация текста (GPT-4)
            prompt = (
                f"Напиши длинную, увлекательную детскую сказку для ребёнка по имени {data.name}, которому {data.age} лет. "
                f"Тема сказки: {data.theme}. "
                f"Дополнительные детали: {data.additional_params or 'приключения и счастье'}. "
                "\n\nТребования:\n"
                "- Тон: магический, вдохновляющий, добрый.\n"
                "- Длина: Минимум 800 слов.\n"
                "- Сюжет: введение, приключение, урок/мораль.\n"
                "- Формат: Только текст сказки."
            )
            
            text_response = await client.post(
                "https://api.openai.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {settings.OPENAI_API_KEY}"},
                json={
                    "model": "gpt-4",
                    "messages": [
                        {"role": "system", "content": "You are a world-class children's book author. Write in Russian."},
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.8
                },
                timeout=60.0
            )
            text_response.raise_for_status()
            story_text = text_response.json()["choices"][0]["message"]["content"]

            # 2. Попытка генерации уникальной картинки (DALL-E 3)
            image_url = get_demo_image(data.theme, data.name)
            
            try:
                style_desc = THEME_STYLE_MODIFIERS.get(data.theme, "whimsical storybook illustration")
                image_prompt = (
                    f"A masterpiece children's book illustration for a {data.age}-year-old child. "
                    f"Theme: {data.theme}. Details: {data.additional_params or ''}. "
                    f"Visual style: {style_desc}. "
                    f"Atmosphere: heartwarming, high quality, soft lighting, award-winning digital art, no text."
                )
                
                image_response = await client.post(
                    "https://api.openai.com/v1/images/generations",
                    headers={"Authorization": f"Bearer {settings.OPENAI_API_KEY}"},
                    json={
                        "model": "dall-e-3",
                        "prompt": image_prompt,
                        "n": 1,
                        "size": "1024x1024",
                        "quality": "hd"
                    },
                    timeout=60.0
                )
                image_response.raise_for_status()
                image_url = image_response.json()["data"][0]["url"]
            except Exception as e:
                logger.error(f"Failed to generate unique image: {e}")

            # 3. Сохранение истории
            stories_coll = get_items_collection()
            new_story = {
                "user_id": str(user["_id"]),
                "name": data.name,
                "age": data.age,
                "theme": data.theme,
                "additional_params": data.additional_params,
                "story_text": story_text,
                "image_url": image_url,
                "is_demo": False,
                "created_at": datetime.now(timezone.utc)
            }
            await stories_coll.insert_one(new_story)

            # 4. Обновление статистики (для обратной совместимости если нужно)
            users_coll = get_users_collection()
            today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
            users_coll.update_one(
                {"_id": user["_id"]},
                {"$inc": {f"generation_stats.{today_str}": 1}}
            )

            return StoryResponse(
                story=story_text,
                image=image_url,
                is_demo=False
            )

        except httpx.HTTPStatusError as e:
            logger.error(f"OpenAI API status error: {e.response.text}")
            raise HTTPException(status_code=502, detail="Сервис AI перегружен. Пожалуйста, попробуйте через минуту.")
        except Exception as e:
            logger.exception("Unexpected error during story generation")
            raise HTTPException(status_code=500, detail="Ошибка на стороне сервера. Мы уже работаем над исправлением!")
