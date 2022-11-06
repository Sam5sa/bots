import telebot
import configparser
from telebot import types

config = configparser.ConfigParser()
config.read("config.ini")


bot = telebot.TeleBot(config["DialogGS_bot"]["api_token"])

def clear(message, n):
    i=0
    flag =0
    while (flag<n):
        try:
            bot.delete_message(message.chat.id,message.id-i)
            i += 1
            flag +=1
        except: i += 1