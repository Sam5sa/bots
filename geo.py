import telebot
import configparser
from telebot import types

config = configparser.ConfigParser()
config.read("config.ini")

bot = telebot.TeleBot(config["pyrogram"]["api_token"])

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')

@bot.message_handler(commands=["geo"])
def geo(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=False)
    keyboard.add(button_geo)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и передай мне свое местоположение", reply_markup=keyboard)

@bot.message_handler(content_types=["location"])
def location(message):
    if message.location is not None:
        bot.send_message(message.chat.id, message.location)
        bot.send_message(message.chat.id,"latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))

bot.polling()