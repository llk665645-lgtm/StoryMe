# Тематические изображения для демо-версии (высокое качество с Unsplash)
THEME_DEMO_IMAGES = {
    "forest": "https://images.unsplash.com/photo-1448375240581-ed3216b38c8c?q=80&w=1200&auto=format&fit=crop",
    "space": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop",
    "ocean": "https://images.unsplash.com/photo-1551244072-5d12893278ab?q=80&w=1200&auto=format&fit=crop",
    "dino": "https://images.unsplash.com/photo-1517930410329-0eb7c9d69901?q=80&w=1200&auto=format&fit=crop",
    "magic": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1200&auto=format&fit=crop",
    "super": "https://images.unsplash.com/photo-1533411448364-7707e4d8fb87?q=80&w=1200&auto=format&fit=crop"
}

# Описания стилей для DALL-E 3
THEME_STYLE_MODIFIERS = {
    "forest": "enchanted woodland, watercolor style, soft morning mist, friendly forest animals",
    "space": "retro-futuristic space art, cosmic glowing stars, cute friendly aliens, nebula colors",
    "ocean": "vibrant coral reef, bright underwater light, friendly sea creatures, Disney-style animation",
    "dino": "prehistoric jungle, lush green ferns, cute baby dinosaurs, bright sunny day, Pixar style",
    "magic": "sparkling fairy dust, golden hour lighting, whimsical storybook illustration, glowing magic wand",
    "super": "comic book style, dynamic action lines, vibrant pop art, heroic pose, bright primary colors"
}

@router.post("/generate", response_model=StoryResponse)
async def generate_story(data: StoryRequest, user: dict | None = Depends(get_optional_user)):
    """
    Генерация сказки с разграничением доступа:
    - гость (без токена) или free subscription → демо-версия (статичный контент)
    - paid → полноценная AI-генерация через GPT-4 и DALL-E 3
    """
    is_paid = user is not None and user.get("subscription_tier") == "paid"

    if not is_paid:
        # Ответ для гостей и бесплатных пользователей (Демо)
        demo_image = THEME_DEMO_IMAGES.get(data.theme, THEME_DEMO_IMAGES["magic"])
        
        # Мы можем добавить немного персонализации даже в демо, используя имя
        demo_story = (
            f"Жил-был отважный герой по имени {data.name}, которому было всего {data.age} лет. "
            f"Однажды в чудесном мире ({data.theme}), произошло нечто невероятное... "
            "\n\n✨ Это демонстрационная версия вашей сказки. В платной подписке вы получите:\n"
            "✅ Полную историю на 8-10 страниц с захватывающим сюжетом.\n"
            "✅ Уникальную иллюстрацию, созданную специально для вашего ребенка.\n"
            "✅ Возможность сохранить сказку в свою библиотеку или распечатать ее.\n\n"
            "Хотите узнать, что случилось дальше? Активируйте магический доступ!"
        )
        return StoryResponse(
            story=demo_story,
            image=demo_image,
            is_demo=True
        )

    # ЛОГИКА ДЛЯ ПЛАТНЫХ ПОЛЬЗОВАТЕЛЕЙ
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
            # Если не получится - используем тематический fallback
            image_url = THEME_DEMO_IMAGES.get(data.theme, THEME_DEMO_IMAGES["magic"])
            
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
                # Мы не бросаем ошибку, чтобы пользователь хотя бы получил текст сказки

            # 3. Обновление статистики пользователя
            users_coll = get_users_collection()
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
