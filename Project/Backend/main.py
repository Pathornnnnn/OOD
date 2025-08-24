import uvicorn
from fastapi import FastAPI
from Backend.api import router

app = FastAPI(title="Hybrid Music Player API")
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("Backend.main:app", host="127.0.0.1", port=8000, reload=True)
