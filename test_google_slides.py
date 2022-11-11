import configparser
import requests
import telebot
from telebot import types

config = configparser.ConfigParser()
config.read("config.ini")

bot = telebot.TeleBot(config["test_bot"]["api_token"])

user_dict = {}


class User:
    def __init__(self, text):
        self.text = text

def post_req(text):
    endpoint = config["google_slides_app"]["endpoint"]

    data = {'text': text}
    response = requests.post(endpoint, json=data)
    #return response

@bot.message_handler(commands=['start'])
def start(message):
    mess = "ТЫК, чтобы писать на слайде"
    inline_markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("ТЫК", callback_data='get_text')
    inline_markup.add(button1)
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup = inline_markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

    def get_text():

        def collect(message):
            #try:
                chat_id = message.chat.id
                text = message.text
                user = User(text)
                user_dict[chat_id] = user
                inline_markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("Подтвердить", callback_data='confurm_order')
                button2 = types.InlineKeyboardButton("Изменить данные", callback_data='get_text')
                inline_markup.add(button1, button2)
                msg = "показать " + user.text + ' на доске?'
                bot.send_message(chat_id,  msg, parse_mode='html', reply_markup = inline_markup)
           # except Exception as e:
              #  bot.reply_to(message, 'oooops')

        mess = "ПИШИ!!!"
        mesg = bot.send_message(call.message.chat.id, mess, parse_mode='html')
        bot.register_next_step_handler(mesg,collect)

    try:

        if call.data == "get_text":
            get_text()

        if call.data == 'confurm_order':
            user = user_dict[call.message.chat.id]
            post_req(user.text)

            mess = "гатова"
            inline_markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("отправить ещё", callback_data='get_text')
            inline_markup.add(button1)
            bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id, text=mess, parse_mode='html', reply_markup = inline_markup)
        
    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
