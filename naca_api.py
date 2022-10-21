import requests
import datetime
from random import randint
import time

'''
endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
api_key = "Rb39uvdNUsLM36vrcoRWmTTe0bqsd6LLqR9JgyV5"
query_params = {"api_key": api_key, "earth_date": "2020-10-21"}
response = requests.get(endpoint, params=query_params)
#print(response.json())

photos = response.json()["photos"]
print(f"Найдено {len(photos)} фотографий.")

print(photos[1]["img_src"])
'''

def send_pic_url():
    endpoint = "https://api.nasa.gov/planetary/apod"
    api_key = "Rb39uvdNUsLM36vrcoRWmTTe0bqsd6LLqR9JgyV5"
    d = datetime.date.today()
    str_yesterday = str(d.year)+"-"+str(d.month)+"-"+str(d.day-1)
    query_params = {"api_key": api_key, "date": str_yesterday}
    response = requests.get(endpoint, params=query_params)
    return(response.json()["hdurl"])

def send_explanation():
    endpoint = "https://api.nasa.gov/planetary/apod"
    api_key = "Rb39uvdNUsLM36vrcoRWmTTe0bqsd6LLqR9JgyV5"
    d = datetime.date.today()
    str_yesterday = str(d.year)+"-"+str(d.month)+"-"+str(d.day-1)
    query_params = {"api_key": api_key, "date": str_yesterday}
    response = requests.get(endpoint, params=query_params)
    return(response.json()["explanation"])

def send_rand_pic():
    endpoint = "https://api.nasa.gov/planetary/apod"
    api_key = "Rb39uvdNUsLM36vrcoRWmTTe0bqsd6LLqR9JgyV5"
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
    return(url,exp)

