import configparser
import requests


config = configparser.ConfigParser()
config.read("config.ini")


def post_req(id,name,phone,product):
    endpoint = config["google_sheets_app"]["endpoint"]

    data = {'id': id, 'user_name' : name, "phone" : phone, "product" : product}
    response = requests.post(endpoint, json=data)
    #print(response)
