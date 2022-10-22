from sqlite3 import adapt
import telebot
import configparser
from telebot import types
import requests


config = configparser.ConfigParser()
config.read("config.ini")

endpoint = config["google_sheets_app"]["endpoint"]

data = {'user_name':'Samsa'}
response = requests.post(endpoint, json=data)
print(response)
