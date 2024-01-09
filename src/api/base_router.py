from fastapi import APIRouter
from src.api import translation


router = APIRouter()
router.include_router(translation.router)
