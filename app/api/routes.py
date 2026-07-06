from fastapi import APIRouter
from app.config.settings import settings
from app.schemas.inference_schema import GenerateRequest, GenerateResponse

def create_router(
    inference_service,
    health_service,
):

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
        return health_service.get_health()

    @router.post(
        "/generate",
        response_model=GenerateResponse,
    )
    async def generate(request: GenerateRequest):

        return inference_service.generate(
            request.prompt,
            request.temperature,
            request.max_tokens,
        )

    return router