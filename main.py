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
    bot.send_message(message.chat.id, 'wellcome to my first bot')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, r'I do computational physics calculation: , please use this comment: '
                          '  /example'
                          '/electromagnetic')


key_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
key_markup.add('x**2', 'two', 'three')


@bot.message_handler(commands=['example'])
def send_example(message):
    bot.reply_to(message, 'this is our example', reply_markup=key_markup)


key_markup2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
key_markup2.add('one', 'two', 'three', 'four', 'five')


@bot.message_handler(commands=['electromagnetic'])
def send_electromagnetic(message):
    bot.reply_to(message, 'this is our example', reply_markup=key_markup2)


@bot.message_handler()
def key_bord_message(message):
    if message.text == 'x**2':
        # bot.send_message(message.chat.id, "Please post a simple function to draw the graph")
        x = np.linspace(-5, 5, 100)
        y = numexpr.evaluate(message.text)
        plt.plot(x, y, 'r')
        plt.grid()
        plt.xlabel('x')
        plt.ylabel(message.text)
        plt.savefig('plot_name.png', dpi=300)
        bot.send_photo(message.chat.id, photo=open('plot_name.png', 'rb'))
    elif message.text == 'two':
        bot.send_message(message.chat.id, 'nice1-three')
    elif message.text == 'three':
        bot.send_message(message.chat.id, 'nice2-three')
    elif message.text == 'four':
        bot.send_message(message.chat.id, 'nice3-four')
    elif message.text == 'five':
        bot.send_message(message.chat.id, 'nice4-five')


bot.infinity_polling()
