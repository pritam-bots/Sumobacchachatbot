from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "28572091"
# -------------------------------------------------------------
API_HASH = "8e0e5b12ad0624ad291422db70ad3098"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "6260080241"))
SUPPORT_GRP = "RockyXUpdate"
UPDATE_CHNL = "RockyXSupport"
OWNER_USERNAME = "MrRockyTG"
