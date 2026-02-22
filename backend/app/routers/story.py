from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
import httpx
import logging

from app.core.config import settings
from app.core.security import get_current_user  # Исправленный импорт

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/story", tags=["story"])

class StoryRequest(BaseModel):
    name: str
    theme: str

@router.post("/generate")
async def generate_story(data: StoryRequest, user: dict = Depends(get_current_user)):
    """
    Генерация сказки с разграничением доступа:
    - гости и free subscription → демо-заглушка
    - платные пользователи → полноценная AI-генерация (текст + картинка)
    """

    # Гость или бесплатная подписка → демо-заглушка
    if not user or user.get("subscription_tier") == "free":
        return {
            "story": f"Жила-была маленькая коала по имени {data.name}. Она очень любила приключения в стиле {data.theme}. Это демонстрационная версия сказки.",
            "image": "https://images.unsplash.com/photo-1616091093714-c64882e9ab55?q=80&w=1000&auto=format&fit=crop"  # Красивая заглушка
        }

    # Проверка ключа OpenAI
    if not settings.OPENAI_API_KEY:
        raise HTTPException(status_code=500, detail="OpenAI API key not configured")

    async with httpx.AsyncClient() as client:
        try:
            # 1. Генерация текста сказки
            prompt = f"Напиши сказку для ребёнка {data.name} на тему {data.theme}. Сказка должна быть доброй, увлекательной и поучительной."
            
            text_response = await client.post(
                "https://api.openai.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {settings.OPENAI_API_KEY}"},
                json={
                    "model": "gpt-4",
                    "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": 1000
                },
                timeout=60.0
            )
            text_response.raise_for_status()
            res_data = text_response.json()
            story_text = res_data["choices"][0]["message"]["content"]

            # 2. Генерация картинки через DALL-E 3
            # Мы используем тему и имя для создания промпта к картинке
            image_prompt = f"High-quality children's book illustration for a story about {data.name} with the theme of {data.theme}. Style: magical, vibrant colors, dreamy atmosphere, digital art."
            
            image_response = await client.post(
                "https://api.openai.com/v1/images/generations",
                headers={"Authorization": f"Bearer {settings.OPENAI_API_KEY}"},
                json={
                    "model": "dall-e-3",
                    "prompt": image_prompt,
                    "n": 1,
                    "size": "1024x1024"
                },
                timeout=60.0
            )
            image_response.raise_for_status()
            image_data = image_response.json()
            image_url = image_data["data"][0]["url"]

            return {
                "story": story_text,
                "image": image_url
            }
        except httpx.HTTPStatusError as e:
            logger.error(f"OpenAI API error: {e.response.text}")
            raise HTTPException(status_code=e.response.status_code, detail=f"AI service error: {e.response.text}")
        except Exception as e:
            logger.exception("Unexpected error during story generation")
            raise HTTPException(status_code=500, detail=f"Failed to generate story: {str(e)}")
