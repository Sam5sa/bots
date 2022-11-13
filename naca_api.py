import requests
import datetime
from random import randint
import time
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

api_key = config["naca_api"]["key"]

def test():
    endpoint = "https://api.nasa.gov/planetary/apod"
    query_params = {"api_key": api_key}
    response = requests.get(endpoint, params=query_params)
    return(response.json())

def send_pic_url():
    endpoint = "https://api.nasa.gov/planetary/apod"
    d = datetime.date.today()
    str_yesterday = str(d.year)+"-"+str(d.month)+"-"+str(d.day-1)
    query_params = {"api_key": api_key, "date": str_yesterday}
    response = requests.get(endpoint, params=query_params)
    return(response.json()["hdurl"])

def send_explanation():
    endpoint = "https://api.nasa.gov/planetary/apod"
    d = datetime.date.today()
    str_yesterday = str(d.year)+"-"+str(d.month)+"-"+str(d.day-1)
    query_params = {"api_key": api_key, "date": str_yesterday}
    response = requests.get(endpoint, params=query_params)
    return(response.json()["explanation"])

def send_rand_pic():
    endpoint = "https://api.nasa.gov/planetary/apod"
    flag  = 0
    while (flag == 0) :
        year = randint(2019,2022)
        month = randint(1,12)
        day = randint(1,27)
        str_yesterday = str(year)+"-"+str(month)+"-"+str(day)
        query_params = {"api_key": api_key, "date": str_yesterday}
        response = requests.get(endpoint, params=query_params)
        flag = 1
        try:
            url = response.json()["hdurl"]
            exp = response.json()["explanation"]
        except: 
            flag = 0
            time.sleep(0.5)
            if (len(exp) > 1024): exp = exp[:1023]
    return(url,exp)


print(test())