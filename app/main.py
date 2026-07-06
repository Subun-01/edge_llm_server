from fastapi import FastAPI

from app.api.routes import create_router

from app.clients.llama_client import LlamaClient

from app.services.inference_service import InferenceService
from app.services.health_service import HealthService

from app.config.settings import settings

app = FastAPI(
    title=settings["app"]["name"],
    version=settings["app"]["version"],
)

llama_client = LlamaClient()

inference_service = InferenceService(llama_client)

health_service = HealthService(llama_client)

app.include_router(
    create_router(
        inference_service,
        health_service,
    )
)