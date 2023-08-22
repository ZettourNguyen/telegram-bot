import telegram
import asyncio
import os
import openai
from config import BOT_TOKEN, API, GROUP_CHAT_ID


# send message from bot to chat_id
# https://api.telegram.org/bot[TOKEN]/sendMessage?chat_id=[CHAT_ID]&text=[MY_MESSAGE_TEXT]

async def send_message():
    message_text = "Message"
    bot = telegram.Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id= GROUP_CHAT_ID, text="New message")
    # await bot.sendPhoto(GROUP_CHAT_ID, photo=open('img/idol.jpg','rb'), caption=message_text)

if __name__ == '__main__':
    asyncio.run(send_message())
