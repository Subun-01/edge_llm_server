import httpx

from app.config.settings import settings


class LlamaClient:
    def __init__(self):
        host = settings["llama"]["host"]
        port = settings["llama"]["port"]
        print("port:",port)
        self.base_url = f"http://{host}:{port}"

    def generate(
        self,
        prompt: str,
        temperature: float,
        max_tokens: int,
    ) -> dict:

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

        response = httpx.post(
            f"{self.base_url}/v1/chat/completions",
            json=payload,
            timeout=60,
        )

        response.raise_for_status()

        return response.json()