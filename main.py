import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("توکن BOT_TOKEN پیدا نشد. لطفاً تو Railway اضافه کن.")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "سلام! ربات فعال است ✅")

print("ربات روشن شد...")
bot.infinity_polling()
