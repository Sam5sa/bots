import requests
import datetime


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

endpoint = "https://api.nasa.gov/planetary/apod"
api_key = "Rb39uvdNUsLM36vrcoRWmTTe0bqsd6LLqR9JgyV5"
d = datetime.date.today()
str_yesterday = str(d.year)+"-"+str(d.month)+"-"+str(d.day-1)
query_params = {"api_key": api_key, "date": str_yesterday}
response = requests.get(endpoint, params=query_params)
print(response.json()["hdurl"])