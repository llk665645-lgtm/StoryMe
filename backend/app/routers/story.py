from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import httpx
from app.core.config import settings

router = APIRouter(prefix="/story", tags=["story"])

class StoryRequest(BaseModel):
    name: str
    theme: str

@router.post("/generate")
async def generate_story(data: StoryRequest):
    """
    Генерация сказки с помощью AI.
    """
    if not settings.OPENAI_API_KEY:
        # Для демо, если ключа нет, возвращаем заглушку
        return {
            "story": f"Жила-была маленькая коала по имени {data.name}. Она очень любила приключения в стиле {data.theme}. Однажды она нашла волшебное дерево...",
            "image": "https://example.com/template.png"
        }

    prompt = f"Напиши сказку для ребёнка {data.name} на тему {data.theme}. Сказка должна быть доброй, увлекательной и поучительной."

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                "https://api.openai.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {settings.OPENAI_API_KEY}"},
                json={
                    "model": "gpt-4",
                    "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": 1000
                },
                timeout=60.0
            )
            response.raise_for_status()
            res_data = response.json()
            story_text = res_data["choices"][0]["message"]["content"]
            
            # В MVP картинка статичная или генерируется отдельно
            return {
                "story": story_text,
                "image": "https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?q=80&w=1000&auto=format&fit=crop"
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to generate story: {str(e)}")
