import telebot
from telebot import types

from environs import Env
import matplotlib.pyplot as plt
import numpy as np
import numexpr
import re

env = Env()
env.read_env()

API_TOKEN = env("BOT_API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_start(message):
    global key_markup_commands
    key_markup_commands = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    key_markup_commands.add('/help', '/example')
    bot.send_message(message.chat.id, 'wellcome to my first bot', reply_markup=key_markup_commands)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, r'I do computational physics calculation.')


@bot.message_handler(commands=['example'])
def send_example(message):
    key_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    key_markup.add('/one', '/two', '/close')
    bot.reply_to(message, 'this is our example', reply_markup=key_markup)


@bot.message_handler(commands=['one'])
def one_example(message):
    msg = bot.reply_to(message, "send me plot interval(for example [-5, 5])")
    bot.register_next_step_handler(msg, get_plot_interval)


def get_plot_interval(message):
    global interval
    chat_id = message.chat.id
    interval = message.text

    f = bot.reply_to(message, "ok, now send me your function to plot")
    bot.register_next_step_handler(f, plot_graph_updater)

    bot.enable_save_next_step_handlers(delay=1)
    bot.load_next_step_handlers()


def plot_graph_updater(message):
    chat_id = message.chat.id
    msg = message.text
    interval1 = list(map(eval, re.findall(r"[-+]?(?:\d*\.*\d+)", interval)))

    x = np.linspace(interval1[0], interval1[1], 100)
    y = numexpr.evaluate(msg)
    plt.plot(x, y, 'r')
    plt.grid()
    plt.xlabel('x')
    plt.ylabel(msg)
    plt.savefig('plot_name.png', dpi=300)
    bot.send_photo(chat_id, photo=open('plot_name.png', 'rb'))

    bot.enable_save_next_step_handlers(delay=2)
    bot.load_next_step_handlers()


@bot.message_handler(commands=['close'])
def close_markup(message):
    key_markup_remove = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, 'close the example', reply_markup=key_markup_remove)
    bot.delete_message(message.chat.id, message.message_id + 1)
    bot.send_message(message.chat.id, 'Please select:', reply_markup=key_markup_commands)


# @bot.message_handler(commands=['electromagnetic'])
# def send_electromagnetic(message):
#     key_markup2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
#     key_markup2.add('one', 'two', 'three', 'four', '/close')
#     bot.reply_to(message, 'this is our example', reply_markup=key_markup2)


# @bot.message_handler()
# def key_bord_message(message):
#     if message.text == 'x**2':
#         bot.ge
#         # bot.send_message(message.chat.id, "Please post a simple function to draw the graph")
#         x = np.linspace(-5, 5, 100)
#         y = numexpr.evaluate(message.text)
#         plt.plot(x, y, 'r')
#         plt.grid()
#         plt.xlabel('x')
#         plt.ylabel(message.text)
#         plt.savefig('plot_name.png', dpi=300)
#         bot.send_photo(message.chat.id, photo=open('plot_name.png', 'rb'))
#     elif message.text == 'two':
#         bot.send_message(message.chat.id, 'nice1-three')
#     elif message.text == 'three':
#         bot.send_message(message.chat.id, 'nice2-three')
#     elif message.text == 'four':
#         bot.send_message(message.chat.id, 'nice3-four')
#     else:
#         bot.send_message(message.chat.id, 'comment dos not exist')


bot.infinity_polling()
