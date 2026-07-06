# Jetson Edge LLM Server

A lightweight offline LLM inference gateway built for NVIDIA Jetson using **FastAPI** and **llama.cpp**.

Instead of interacting directly with `llama-server`, applications communicate with this REST API, providing a clean, modular, and reusable interface for local LLM inference.

## Features

- Offline LLM inference
- REST API using FastAPI
- Modular layered architecture
- OpenAI-compatible backend integration
- YAML-based configuration
- Request validation with Pydantic
- Structured logging
- Health monitoring
- Request latency measurement
- Automatic Swagger documentation

## Architecture

```
Client
   │
   ▼
FastAPI
   │
   ▼
Inference Service
   │
   ▼
Llama Client
   │
   ▼
llama-server
   │
   ▼
GGUF Model
```

## Project Structure

```text
app/
├── api/
├── clients/
├── config/
├── core/
├── schemas/
├── services/
└── utils/

configs/
logs/
tests/
```

## Tech Stack

- Python
- FastAPI
- llama.cpp
- httpx
- Pydantic
- PyYAML
- NVIDIA Jetson Orin

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Service information |
| GET | `/health` | Backend health status |
| POST | `/generate` | Generate text |

Swagger UI:

```
http://<jetson-ip>:8000/docs
```

## Run

Start `llama-server`

```bash
./llama-server -m <model.gguf> --host 127.0.0.1 --port 8080
```

Start the API

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Example Request

```json
POST /generate

{
    "prompt": "Explain CUDA.",
    "temperature": 0.7,
    "max_tokens": 256
}
```

## Future Improvements

- Streaming responses
- Metrics endpoint
- Benchmark endpoint
- Docker deployment
- Offline Voice Assistant integration

---

Built as a learning project to understand backend architecture and Edge AI system design.