from fastapi import FastAPI
from src.api.base_router import router


tag_description = [
    {
        'name': 'translation',
        'description': 'Перевод текста'
    }
]

app = FastAPI(
    title='Приложение для перевода текста на различные языки',
    description='РГР по дисциплине NLP',
    version='0.0.1',
    openapi_tags=tag_description
)

app.include_router(router)
