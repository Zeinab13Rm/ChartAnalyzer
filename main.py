from fastapi import FastAPI
from src.infrastructure.api.fastapi.routes import auth, charts
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Chart Analyzer API",
    description="API for analyzing charts and managing users.",
    version="1.0.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Your Vite frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router, prefix="/auth")
app.include_router(charts.router, prefix="/charts")

@app.get("/")
async def root():
    return {"message": "Welcome to Chart Analyzer"}
