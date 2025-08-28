import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Backend.api import router

app = FastAPI(title="Hybrid Music Player API")
app.include_router(router)
origins = [
    "http://localhost:5173",  # URL ของ React dev server
    "http://127.0.0.1:5173"   # เผื่อเรียกแบบ IP
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # ใส่ origin ของ frontend
    allow_credentials=True,
    allow_methods=["*"],    # อนุญาต GET, POST, PUT, DELETE ทุกชนิด
    allow_headers=["*"],    # อนุญาตทุก header
)
if __name__ == "__main__":
    uvicorn.run("Backend.main:app", host="127.0.0.1", port=8000, reload=True)
