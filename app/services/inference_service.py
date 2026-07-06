from app.clients.llama_client import LlamaClient
from app.utils.timer import Timer
from app.utils.request_id import generate_request_id
from app.core.logger import logger



class InferenceService:

    def __init__(self,client: LlamaClient):
        self.client = client

    def generate(
        self,
        prompt: str,
        temperature: float,
        max_tokens: int,
    ):
        timer = Timer()
        timer.start()
        request_id = generate_request_id()
        logger.info(
            "[%s] Prompt received (%d chars)",
            request_id,
            len(prompt),
        )
        try:
            result = self.client.generate(
                prompt,
                temperature,
                max_tokens,
                request_id,
            )
            latency = timer.elapsed_ms()
            logger.info(
                "[%s] Completed in %.2f ms",
                request_id,
                latency,
            )
            return {
                "request_id": request_id,
                "model": result["model"],
                "latency_ms": latency,
                "response": result["choices"][0]["message"]["content"],
            }
        except Exception as e:
            logger.exception("[%s] Inference failed", request_id)
            raise   