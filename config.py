from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph//file/de299084a7d428f6c630c.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph//file/feb8f95994406a2ad01d8.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/BestieVirtual")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Nenen_degrees")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"

EXTRA_PLUGINS = getenv(
    "EXTRA_PLUGINS",
    "True",
)

# Fill True if you want to load extra plugins


EXTRA_PLUGINS_REPO = getenv(
    "EXTRA_PLUGINS_REPO",
    "https://github.com/Fsyrl99/ferdimusik",
)
# Fill here the external plugins repo where plugins that you want to load

SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", "https://t.me/Nenen_degrees"

  SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", "galeribv"

# Set it in True if you want to leave your assistant after a certain amount of time. [Set time via AUTO_LEAVE_ASSISTANT_TIME]
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", False)

# Time after which you're assistant account will leave chats automatically.
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "50000")
)  # Remember to give value in Seconds
