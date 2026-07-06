from app.clients.llama_client import LlamaClient
from app.core.logger import logger


class HealthService:
    """
    Business logic for application health.
    """

    def __init__(self,client: LlamaClient):
        self.client = client

    def get_health(self) -> dict:
        backend = self.client.health()
        logger.info(f"Health check: backend={backend}")
        return {
            "status": "healthy",
            "backend": backend,
        }