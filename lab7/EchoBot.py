import telebot
import os
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

@bot.message_handler(content_types=['text', 'photo', 'video', 'audio', 'document', 'sticker', 'voice', 'video_note', 'location', 'contact'])
def echo_all(message):
    bot.copy_message(
        chat_id = message.chat.id,
        from_chat_id = message.chat.id,
        message_id = message.message_id
    ) # I just don't want to type all those content types again so I used copy_message

bot.infinity_polling()