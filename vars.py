# DON'T add anything here just add in render's secret or env section 
from os import environ

API_ID = int(environ.get("API_ID", "29467268"))
API_HASH = environ.get("API_HASH", "314e5ae9ce4f78ef127a5a04a5c97649")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
