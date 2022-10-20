import telebot
import configparser
from telebot import types

config = configparser.ConfigParser()
config.read("config.ini")

bot = telebot.TeleBot(config["pyrogram"]["api_token"])