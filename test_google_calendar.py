import configparser
import requests
import telebot
from telebot import types

config = configparser.ConfigParser()
config.read("config.ini")

bot = telebot.TeleBot(config["DialogGS_bot"]["api_token"])

@bot.message_handler(commands=['start'])
def start(message):
    mess = "ТЫК"
    inline_markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("ТЫК", callback_data='click')
    inline_markup.add(button1)
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup = inline_markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
         if call.data == 'click':
            endpoint = config["google_calendar_app"]["endpoint"]
            response = requests.get(endpoint)
            mess = response.json()["start_date"]
            print(mess)
            inline_markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("ТЫК", callback_data='click')
            inline_markup.add(button1)
            #try: 
            bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id, text=mess, parse_mode='html', reply_markup = inline_markup)
           # except:
               # bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id, text="response", parse_mode='html', reply_markup = inline_markup)
    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)
