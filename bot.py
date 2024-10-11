import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio
import nest_asyncio

# nest_asyncio ni qo'llash
nest_asyncio.apply()

# Loggingni o'rnatamiz
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Botning asosiy /start funksiyasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Rasmiy kanalimiz📱", url='https://t.me/guroba_pic'),
            InlineKeyboardButton("Web sahifamiz🌐 ", web_app={'url': 'https://guroba.media'})
        ],
        [
            InlineKeyboardButton("Aloqa manzil📩", url='https://t.me/nusrat')
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo=open('gurobapic.png', 'rb'),
        caption="G'uroba katibasining rasmiy boti✅",
        reply_markup=reply_markup
    )

# Botni ishga tushirish
async def main():
    application = ApplicationBuilder().token('7607159405:AAGRkLDGupAPqRjnC9Q6BigZcdt79M2sgcE').build()

    application.add_handler(CommandHandler("start", start))

    await application.run_polling()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
