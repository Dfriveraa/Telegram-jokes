from app.debug import init_debug

from app.bot import bot
from app.logging import get_logging

log = get_logging(__name__)

if __name__ == "__main__":
    log.info("Telejoke bot startas")
    init_debug()
    bot.infinity_polling()
