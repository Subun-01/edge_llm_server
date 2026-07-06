from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    prompt: str = Field(..., min_length=1)
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: int = Field(default=256, gt=0)


class GenerateResponse(BaseModel):
    request_id: str
    model: str
    latency_ms: float
    response: str