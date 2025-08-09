import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "سلام! ربات فعال است.")

print("Bot is running...")
bot.infinity_polling()
