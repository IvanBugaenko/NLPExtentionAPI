from fastapi import FastAPI
from src.api.base_router import router
from fastapi.middleware.cors import CORSMiddleware


tag_description = [
    {
        'name': 'translation',
        'description': 'Перевод текста'
    }
]

origins = ["*"]

app = FastAPI(
    title='Приложение для перевода текста на различные языки',
    description='РГР по дисциплине NLP',
    version='0.0.1',
    openapi_tags=tag_description
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
