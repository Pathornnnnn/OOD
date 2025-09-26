import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Backend.api.routes import router

app = FastAPI(
    title="Hybrid Music Player API",
    description="A hybrid music player backend with FastAPI",
    version="1.0.0",
    docs_url="/docs",       # Swagger UI
    redoc_url="/redoc"      # ReDoc UI
)
app.include_router(router)

# CORS for frontend
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("Backend.main:app", host="127.0.0.1", port=8000, reload=True)
