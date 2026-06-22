import os
import telebot
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
AI_KEY = os.getenv("AI_KEY")

bot = telebot.TeleBot(BOT_TOKEN)

def ask_ai(message):
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {AI_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are Growth Lab AI Tutor. Teach simply."},
            {"role": "user", "content": message}
        ]
    }

    res = requests.post(url, headers=headers, json=data)
    return res.json()["choices"][0]["message"]["content"]

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 Welcome to Growth Lab AI Tutor!")

@bot.message_handler(func=lambda message: True)
def handle(message):
    try:
        reply = ask_ai(message.text)
        bot.reply_to(message, reply)
    except:
        bot.reply_to(message, "Error: Try again later.")

bot.polling()
