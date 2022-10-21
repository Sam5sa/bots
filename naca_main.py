from naca_api import send_pic_url, send_explanation, send_rand_pic

import telebot
import configparser
from telebot import types
import time

config = configparser.ConfigParser()
config.read("config.ini")


bot = telebot.TeleBot(config["space_esteticks_bot"]["api_token"])


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name} {message.from_user.last_name}. Нажми кнопку, чтобы получить кусочек космоса на сегодня)'
    inline_markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("ЖМИ", callback_data='pic')
    inline_markup.add(button1)
    bot.send_photo(message.chat.id, photo="https://www.oecd.org/media/oecdorg/directorates/directorateforsciencetechnologyandindustry/stp/space_astronaut_iStock-1353874144.jpg", caption=mess, reply_markup = inline_markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.data == 'pic':
            inline_markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("ЖМИ", callback_data='pic')
            inline_markup.add(button1)
            flag = 0
            while (flag == 0) :
                try:
                    flag = 1
                    url, exp = send_rand_pic()
                    bot.edit_message_media(message_id=call.message.message_id, chat_id=call.message.chat.id, media=types.InputMediaPhoto(url,caption= exp),reply_markup=inline_markup)
                except: 
                    flag = 0
                    time.sleep(0.5)
    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)