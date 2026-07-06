from app.core.logger import logger
import logging
import httpx
logging.getLogger("httpx").setLevel(logging.WARNING)
from app.config.settings import settings



class LlamaClient:
    def __init__(self):
        host = settings["llama"]["host"]
        port = settings["llama"]["port"]
        self.base_url = f"http://{host}:{port}"
        self.client = httpx.Client(
            base_url=self.base_url,
            timeout=settings["llama"].get("timeout", 60),
        )

        logger.info("LlamaClient initialized")
    # --------------------------------------------------
    # Private Helpers
    # --------------------------------------------------

    def _get(self, endpoint: str) -> dict:

        response = self.client.get(endpoint)

        response.raise_for_status()

        return response.json()

    def _post(self, endpoint: str, payload: dict) -> dict:

        response = self.client.post(
            endpoint,
            json=payload,
        )

        response.raise_for_status()

        return response.json()

    # --------------------------------------------------
    # Public API
    # --------------------------------------------------

    def generate(
        self,
        prompt: str,
        temperature: float,
        max_tokens: int,
        request_id: str,
    ) -> dict:

        logger.info("[%s] Sending request to llama-server", request_id)

        payload = {
            "model": settings["llama"]["model"],
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            "temperature": temperature,
            "max_tokens": max_tokens,
        }

        return self._post(
            "/v1/chat/completions",
            payload,
        )

    def health(self) -> dict:
        return self._get("/health")

  
    def close(self):
        self.client.close()