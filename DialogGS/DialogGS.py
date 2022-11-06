from webhoocks_for_google_sheets import post_req

import telebot
import configparser
from telebot import types
import time

config = configparser.ConfigParser()
config.read("config.ini")


bot = telebot.TeleBot(config["DialogGS_bot"]["api_token"])

user_dict = {}


class User:
    def __init__(self, name):
        self.name = name
        self.phone = None
        self.product = None


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Здравствуйте, {message.from_user.first_name} {message.from_user.last_name}. Спасибо, что проявили к нам интерес)\nМы предоставляем услуги автоматизации бизнес-процессов.\nС радостью помогу вам:\nопределиться с выбором услуги\nрасскажу о компании\nотвечу на интересующие вопросы)'
    inline_markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Наши услуги", callback_data='deal_list')
    button2 = types.InlineKeyboardButton("узнать о нас больше", callback_data='info')
    button3 = types.InlineKeyboardButton("задать вопрос", callback_data='question')
    inline_markup.add(button1, button2,button3)
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup = inline_markup)

@bot.message_handler(commands=['clear'])
def clear(message):
    i=0
    flag =0
    while (flag<3):
        try:
            bot.delete_message(message.chat.id,message.id-i)
            i += 1
            flag +=1
        except: i += 1

'''
@bot.message_handler()
def get_text(message):
    post_req(message.text)
    mess = "Ваш заказ принят"
    inline_markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("В меню", callback_data='menu')
    inline_markup.add(button1)
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup = inline_markup)
'''

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.data == 'info':
            mess = 'Наша компания заботится о качестве оказываемых услуг.\nЛюбой заказ мы начинаем с БЕСПЛАТНОЙ консультации на которой разберём на атомы бизнес-логику ВАШЕГО дела.\nНа ней мы определим процессы, подлежащие оптимизации и ПОДАРИМ бота-визитку для вашего бизнеса!'
            inline_markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("В меню", callback_data='menu')
            inline_markup.add(button1)
            bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id, text=mess, parse_mode='html', reply_markup = inline_markup)

        if call.data == 'menu':
            mess = "Вы в главном меню"
            inline_markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Наши услуги", callback_data='deal_list')
            button2 = types.InlineKeyboardButton("узнать о нас больше", callback_data='info')
            button3 = types.InlineKeyboardButton("задать вопрос", callback_data='question')
            inline_markup.add(button1, button2,button3)
            bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id, text=mess, parse_mode='html', reply_markup = inline_markup)

        if call.data == 'deal_list':
            mess = "Наш список услуг:"
            inline_markup = types.InlineKeyboardMarkup()
            inline_markup.row_width = 1
            button1 = types.InlineKeyboardButton("БЕСПЛАТНАЯ консультация", callback_data='consult')
            button2 = types.InlineKeyboardButton("Автоматизация ведения сделок по црм системе", callback_data='CRM')
            button3 = types.InlineKeyboardButton("Автоматизация ведения клиентской БД", callback_data='clientDB')
            button4 = types.InlineKeyboardButton("Автоматизация ведения календаря деловых встреч", callback_data='meetings')
            button5 = types.InlineKeyboardButton("В меню", callback_data='menu')
            inline_markup.add(button1, button2, button3, button4, button5)
            bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id, text=mess, parse_mode='html', reply_markup = inline_markup)

        if call.data == 'consult':
            mess = 'Разберём на атомы бизнес-логику ВАШЕГО дела.\nНа ней мы определим процессы, подлежащие оптимизации и ПОДАРИМ бота-визитку для вашего бизнеса!'
            inline_markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Заказать", callback_data='order_consult')
            button2 = types.InlineKeyboardButton("К услугам", callback_data='deal_list')
            inline_markup.add(button1, button2)
            bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id, text=mess, parse_mode='html', reply_markup = inline_markup)

        if call.data == 'CRM':
            mess = 'Теряете клиентов в воронке продаж?\nНЕ УПУСТИТЕ не одного с нашей системой управления клиентами!'
            inline_markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Заказать", callback_data='order_CRM')
            button2 = types.InlineKeyboardButton("К услугам", callback_data='deal_list')
            inline_markup.add(button1, button2)
            bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id, text=mess, parse_mode='html', reply_markup = inline_markup)

        if call.data == 'clientDB':
            mess = 'Пользуетесь таблицами для ведения книги клиентов? \nМЫ сделаем процесс заполнения автоматическим, смотрите и наслаждайтесь!'
            inline_markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Заказать", callback_data='order_clientDB')
            button2 = types.InlineKeyboardButton("К услугам", callback_data='deal_list')
            inline_markup.add(button1, button2)
            bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id, text=mess, parse_mode='html', reply_markup = inline_markup)

        if call.data == "order_clientDB":
            def name_step(message):
                #try:
                    chat_id = message.chat.id
                    name = message.text
                    user = User(name)
                    user.product = "clientDB"
                    user_dict[chat_id] = user
                    msg = bot.send_message(chat_id, 'Пожалуйста, укажите телефон для связи с вами')
                    bot.register_next_step_handler(msg, phone_step)
                #except Exception as e:
                 #   bot.reply_to(message, 'oooops')

            def phone_step(message):
                try:
                    chat_id = message.chat.id
                    phone = message.text
                    user = user_dict[chat_id]
                    user.phone = phone
                    bot.send_message(chat_id,  "Уважаемый " + user.name + '\nВаш заказ: ' + user.product + '\nВ ближайшее время с вами свяжутся по телефону:' + str(user.phone))
                except Exception as e:
                    bot.reply_to(message, 'oooops')

            mess = "Напишите как к вам можно обращаться"
            mesg = bot.send_message(call.message.chat.id, mess, parse_mode='html')
            bot.register_next_step_handler(mesg,name_step)  

        if call.data == 'meetings':
            mess = 'Постоянной выгорание и усталость от невозможности успеть всё? Не пропустите не одной важной встречи и распланируйте свой день с помощью автоматического календаря!'
            inline_markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Заказать", callback_data='order_meetings')
            button2 = types.InlineKeyboardButton("К услугам", callback_data='deal_list')
            inline_markup.add(button1, button2)
            bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id, text=mess, parse_mode='html', reply_markup = inline_markup)

        
        
    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)