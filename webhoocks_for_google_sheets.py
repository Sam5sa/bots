import configparser
import requests


config = configparser.ConfigParser()
config.read("config.ini")


def post_req(name):
    endpoint = config["google_sheets_app"]["endpoint"]

    data = {'user_name':name}
    response = requests.post(endpoint, json=data)
    #print(response)
