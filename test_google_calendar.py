import configparser
import requests
import telebot
from telebot import types

config = configparser.ConfigParser()
config.read("config.ini")

bot = telebot.TeleBot(config["DialogGS_bot"]["api_token"])
endpoint = config["google_calendar_app"]["endpoint"]

def collect_data():
    response = requests.get(endpoint)
    data = response.json()["events"]
    return data

def str_to_floattime(time):
    if (float(time[0]) == 0): 
        return float(time[1])+float(time[3:])/60
    else:
        return float(time[:2])+float(time[3:])/60

def floattime_to_str(time):
    if (time < 10): 
        hours =  "0" + str(time // 1)[:1]
    else:
        hours =  str(time // 1)[:2]
    
    if  (int(time % 1 * 10) * 6 == 0): 
        mins = "00"
    else:
        mins = str(int(time % 1 * 10) * 6)
    return hours + ":" + mins
    

def get_free_time():
    open_time = "08:00"
    close_time = "22:00"
    ordet_time_delta = "04:00"
    free_time = []
    ordered_start_time = []
    events = collect_data()
    for event in events:
        print(event)
        ordered_start_time.append(event.get("start_time"))
    time = str_to_floattime(open_time)
    while (time < str_to_floattime(close_time)):
        flag = 0
        for t in ordered_start_time:
            if (time+str_to_floattime(ordet_time_delta) > str_to_floattime(t)) and (time < str_to_floattime(t)+str_to_floattime(ordet_time_delta)):
                flag = 1
        if (flag == 0): 
            free_time.append(floattime_to_str(time))
        time += 0.5
    
    return free_time

    

@bot.message_handler(commands=['start'])
def start(message):
    mess = "ТЫК"
    inline_markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("ТЫК", callback_data='click')
    inline_markup.add(button1)
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup = inline_markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
         if call.data == 'click':
            mess = collect_data()
            inline_markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("ТЫК", callback_data='click')
            inline_markup.add(button1)
            try: 
                bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id, text=mess, parse_mode='html', reply_markup = inline_markup)
            except:
                bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id, text="response", parse_mode='html', reply_markup = inline_markup)
    except Exception as e:
        print(repr(e))

#bot.polling(none_stop=True)

print(get_free_time())
