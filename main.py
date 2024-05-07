# import asyncio
#
# from config import dp, bot
# from database.a_db import AsyncDatabase
# from handlers import setup_routers
#
#
# async def main():
#     db = AsyncDatabase()
#     await db.create_tables()
#     router = setup_routers()
#     dp.include_router(router)
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
#

import logging
from telegram.ext import Updater, CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text('Привет! Я бот. Как дела?')

def main():

    updater = Updater(token='7009134619:AAGxwyJp8vMLOajKhAOFMZSj2XC0Dr24WWY', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
