import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8037028112:AAFkP8jdTaf7Vtqlj-D6wVJcSYUhsYuy8js")
API_ID = int(os.environ.get("API_ID", "27382550"))
API_HASH = os.environ.get("API_HASH", "c428034cb811de290315501d8e3c82b5")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002346117539"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "7006712482").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://Rajveerb:Rajveerb@cluster0.v82fv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
