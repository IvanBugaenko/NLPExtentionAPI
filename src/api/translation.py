from fastapi import APIRouter, Depends
from src.schemas.translation.translation_response import TranslationResponse
from src.schemas.translation.translation_request import TranslationRequest
from src.services.translation import TranslationService


router = APIRouter(
    prefix='/translation',
    tags=['translation']
)


@router.get('/translate', response_model=TranslationResponse, name='Перевод предложения')
def translate(text: str, src_lang: str, trg_lang: str, translation_service: TranslationService = Depends()):
    """
    Перевод предложения с исходного языка на целевой.
    """
    return TranslationResponse(text=translation_service.translate(TranslationRequest(
        text=text, src_lang=src_lang, trg_lang=trg_lang
    )))
