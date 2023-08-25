from config import BOT_TOKEN, API, GROUP_CHAT_ID, THAO_ID
from commandHandler import start, help_command, echo
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from telegram import Update, Bot


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(BOT_TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("help3", help_command))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
