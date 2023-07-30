import telebot
from environs import Env

env = Env()
env.read_env()

API_TOKEN = env("BOT_API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id, 'wellcome to my first bot 😊')


key_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
key_markup.add('one', 'two', 'three')


@bot.message_handler(commands=['help'])
def send_start(message):
    bot.reply_to(message, 'I do physics calculation', reply_markup=key_markup)


bot.infinity_polling()
