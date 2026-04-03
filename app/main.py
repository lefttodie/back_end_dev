from fastapi import FastAPI
from app.routes.github import router

app = FastAPI(
    title="GitHub Cloud Connector",
    description="Backend assignment project",
    version="1.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "GitHub Connector is running"}