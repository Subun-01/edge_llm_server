from app.clients.llama_client import LlamaClient
from app.utils.timer import Timer
from app.utils.request_id import generate_request_id




class InferenceService:

    def __init__(self):
        self.client = LlamaClient()

    def generate(
        self,
        prompt: str,
        temperature: float,
        max_tokens: int,
    ):
        timer = Timer()
        timer.start()
        request_id = generate_request_id()
        result = self.client.generate(
            prompt,
            temperature,
            max_tokens,
        )
        latency = timer.elapsed_ms()
        return {
            "request_id": request_id,
            "model": result["model"],
            "latency_ms": latency,
            "response": result["choices"][0]["message"]["content"],
        }