import logging
import os
import asyncio

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Reply to /start."""
    if update.effective_message:
        await update.effective_message.reply_text(
            "سلام! به ربات ما خوش آمدید 👋"
        )


async def main() -> None:
    if not TOKEN:
        raise RuntimeError(
            "توکن تنظیم نشده است. فایل .env را از روی .env.example بسازید "
            "و TELEGRAM_BOT_TOKEN را در آن وارد کنید."
        )

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    logger.info("ربات در حال اجراست. برای توقف Ctrl+C را بزنید.")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    try:
        # Keep the process alive while polling for Telegram updates.
        await asyncio.Event().wait()
    finally:
        await app.updater.stop()
        await app.stop()
        await app.shutdown()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nربات متوقف شد.")
