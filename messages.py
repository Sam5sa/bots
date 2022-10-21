import telebot
import configparser
from telebot import types

''
config = configparser.ConfigParser()
config.read("config.ini")

bot = telebot.TeleBot(config["pyrogram"]["api_token"])


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Здравствуйте, {message.from_user.first_name} {message.from_user.last_name}. Я помогу вам узнать всю необходимую информацию, только задайте мне вопрос.'
    site_or_city = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("узнать о нас больше", callback_data='info')
    button2 = types.InlineKeyboardButton("задать вопрос", callback_data='qestion')
    site_or_city.add(button1,button2)
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup = site_or_city)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.data == 'info':
           mess = 'я гуль'
           bot.send_message(call.message.chat.id, mess, parse_mode='html') 
    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
