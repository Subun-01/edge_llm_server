from fastapi import FastAPI

from app.api.routes import router
from app.config.settings import settings

app = FastAPI(
    title=settings["app"]["name"],
    version=settings["app"]["version"],
    debug=settings["app"]["debug"],
)


@app.on_event("startup")
async def startup():
    pass


@app.on_event("shutdown")
async def shutdown():
    pass


app.include_router(router)