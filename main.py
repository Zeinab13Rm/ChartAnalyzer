from fastapi import FastAPI
from src.infrastructure.api.fastapi.routes import auth, charts

app = FastAPI(
    title="Chart Analyzer API",
    description="API for analyzing charts and managing users.",
    version="1.0.0",
)

app.include_router(auth.router, prefix="/auth")
app.include_router(charts.router, prefix="/charts")

@app.get("/")
async def root():
    return {"message": "Welcome to Chart Analyzer"}
