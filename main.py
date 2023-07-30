import telebot

from environs import Env
import matplotlib.pyplot as plt
import numpy as np
import numexpr

env = Env()
env.read_env()

API_TOKEN = env("BOT_API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id, 'wellcome to my first bot 😊')


key_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
key_markup.add('x**2', 'two', 'three')


@bot.message_handler(commands=['help'])
def send_start(message):
    bot.reply_to(message, 'I do computational physics calculation', reply_markup=key_markup)


@bot.message_handler()
def key_bord_message(message):
    if message.text == 'x**2':
        # bot.send_message(message.chat.id, "Please post a simple function to draw the graph")
        x = np.linspace(-5, 5, 100)
        y = numexpr.evaluate(message.text)
        plt.plot(x, y, 'r')
        plt.savefig('plot_name.png', dpi=300)
        bot.send_photo(message.chat.id, photo=open('plot_name.png', 'rb'))
    else:
        bot.send_message(message.chat.id, "It will be added in the future")


bot.infinity_polling()
