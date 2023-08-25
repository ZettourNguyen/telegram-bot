# from config import BOT_TOKEN, API, GROUP_CHAT_ID, ZETTO_ID, THAO_ID
# from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
# from telegram import Update, BotCommand, Bot
# import asyncio
#
# bot = Bot(BOT_TOKEN)
# async def setcommand():
#     application = Application.builder().token(BOT_TOKEN).build()
#     commands = [
#         BotCommand('start', 'Start the bot'),
#         BotCommand('help', 'Get help command'),
#         BotCommand('help3', 'Help')
#     #   add another bot command here
#     ]
#     await application.bot.set_my_commands(commands)
#     await bot.sendMessage(ZETTO_ID,"Set command successfully")
#
#     await bot.sendMessage(THAO_ID, "LOO")
#
#
# asyncio.run(setcommand())
#
