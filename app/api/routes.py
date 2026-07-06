from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.schemas.generate import GenerateRequest, GenerateResponse
from app.services.inference_service import InferenceService
from app.config.settings import settings

service = InferenceService()


router = APIRouter()


@router.get("/")
async def root():
    return {
        "application": settings["app"]["name"],
        "version": settings["app"]["version"],
        "status": "running",
    }


@router.get("/health")
async def health():
    return {
        "status": "healthy",
        "llama_server": "unknown",
    }


@router.post("/generate",response_model=GenerateResponse,)
async def generate(request: GenerateRequest):

    return service.generate(
        request.prompt,
        request.temperature,
        request.max_tokens
    )

