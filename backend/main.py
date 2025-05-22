from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import DEBUG_MODE
import logging
import os  # добавляем для работы с окружением

from api.room import RoomRouter
from api.user import UserRouter
from api.events import EventRouter
from api.game import GameRouter
from api.debug import DebugRouter

fileHandler = logging.FileHandler("log.txt")
fileHandler.setLevel(logging.ERROR)
logging.getLogger().addHandler(fileHandler)

app = FastAPI(title="World Domination API", root_path="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(RoomRouter, prefix="/room", tags=["Комната"])
app.include_router(UserRouter, prefix="/room/user", tags=["Пользователь"])
app.include_router(GameRouter, prefix="/game", tags=["Игра"])
app.include_router(EventRouter, prefix="/room/events", tags=["Eventmanager"])

if DEBUG_MODE:
    app.include_router(DebugRouter, prefix="/debug", tags=["Debug"])

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))  # читаем порт из окружения или ставим 8000 по умолчанию
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
