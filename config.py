import os
from dotenv import load_dotenv
load_dotenv()

ZETTO_ID = os.environ["ZETTO_ID"]
BOT_TOKEN = os.environ["BOT_TOKEN"]
GROUP_CHAT_ID = os.environ["GROUP_CHAT_ID"]
API = os.environ.get("OPENAI_API_KEY", None)