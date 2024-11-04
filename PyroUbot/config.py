import os

from dotenv import load_dotenv

load_dotenv(".env")

API_ID: int = os.getenv('API_ID', 23346063)
API_HASH: str = os.getenv('API_HASH', "91a8bfefb69664b2770d41c9876e052e")

BOT_TOKEN = os.getenv("7615008031:AAFbKJ47-GYjyornEuRtOkZjpaW6RWLAPM8")

OWNER_ID = int(os.getenv("1835508209"))

LOGS_MAKER_UBOT = int(os.getenv("-1001948756607"))

MAX_BOT = int(os.getenv("30"))

RMBG_API = os.getenv("RMBG_API")

OPENAI_KEY = os.getenv("OPENAI_KEY")

MONGO_URL = os.getenv("MONGO_URL")
