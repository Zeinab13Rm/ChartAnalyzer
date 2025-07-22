from fastapi import FastAPI
from infrastructure.api.fastapi.routes import auth

app = FastAPI(
    title="Chart Analyzer API",
    description="API for analyzing charts and managing users.",
    version="1.0.0",
)

app.include_router(auth.router, prefix="/auth")

@app.get("/")
async def root():
    return {"message": "Welcome to Chart Analyzer"}
