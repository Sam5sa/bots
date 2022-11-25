import configparser
import requests
import telebot
from telebot import types
import json
import time
from py4j.java_gateway import JavaGateway

config = configparser.ConfigParser()
config.read("config.ini")

bot = telebot.TeleBot(config["DialogGS_bot"]["api_token"])
endpoint = config["google_calendar_app"]["endpoint"]
work_time = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']


def collect_data():
    response = requests.get(endpoint)
    data = response.json()["events"]
    return data

def str_to_floattime(time):
    if (time[1] == ":"): 
        return float(time[0])+float(time[2:])/60
    else:
        return float(time[:2])+float(time[3:])/60

def floattime_to_str(time):
    if (time < 10): 
        hours =  str(time // 1)[0]
    else:
        hours =  str(time // 1)[:2]
    
    if  (int(time % 1 * 10) * 6 == 0): 
        mins = "00"
    else:
        mins = str(int(time % 1 * 10) * 6)
    return hours + ":" + mins
    

def get_free_table_time(table):
    open_time = "08:00"
    close_time = "22:00"
    ordet_time_delta = "04:00"
    free_time = []
    ordered_start_time = []
    events = collect_data()
    for event in events:
        #print(event)
        if (event.get("title") == table): ordered_start_time.append(event.get("start_time"))
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

def get_free_table_time_var(table):
    events = collect_data()
    order_time = []
    
    for event in events:
        #print(event)
        if (event.get("title") == table): 
            order_time.append(event.get("start_time"))
            for t in range(1,8):
                order_time.append(floattime_to_str(str_to_floattime(event.get("start_time"))+0.5*t))
                order_time.append(floattime_to_str(str_to_floattime(event.get("start_time"))-0.5*t))
    return sorted(list(set(work_time) - set(order_time)))
    

def get_all_free_time():
    a_set = set()
    free_time_array = []
    for table in range(1,3):
        #print(get_free_table_time (str(table)))
        a_set.update(set(get_free_table_time (str(table))))
        free_time_array.append(get_free_table_time (str(table)))
    a_set = sorted(list(a_set))
    return a_set, free_time_array

    

@bot.message_handler(commands=['start'])
def start(message):
    mess = "ТЫК"
    inline_markup = types.InlineKeyboardMarkup()
    cdata = '{"metod": "select_time"}'
    button1 = types.InlineKeyboardButton("выбрать время", callback_data=cdata)
    inline_markup.add(button1)
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup = inline_markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if json.loads(call.data)["metod"] == 'select_time':
            mess = "Выберите время"
            inline_markup = types.InlineKeyboardMarkup()
            all_time,array_tt = get_all_free_time()
            #array = get_work_time_array()
            for time in all_time:
                cdata = '{"metod": "select_table", "time":"' + time + '", "table": "table"}'
                #print(cdata)
                but = types.InlineKeyboardButton(time, callback_data=cdata)
                inline_markup.add(but)
            bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id, text=mess, parse_mode='html', reply_markup = inline_markup)

        if json.loads(call.data)["metod"] == "select_table":
            mess = "выберите стол"
            inline_markup = types.InlineKeyboardMarkup()
            cdata = '{"metod": "select_time"}'
            button1 = types.InlineKeyboardButton("к выбору времени", callback_data=cdata)
            inline_markup.add(button1)
            #tables = get_all_tables_array()
            all_time,array_tt = get_all_free_time()
            for i in range(len(array_tt)):
                if json.loads(call.data)["time"] in array_tt[i]:
                    cdata = json.loads(call.data)
                    cdata["table"], cdata["metod"] = str(i+1), "order_table"
                    cdata = json.dumps(cdata)
                    but = types.InlineKeyboardButton(str(i+1), callback_data=cdata)
                    inline_markup.add(but)
            bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id, text=mess, parse_mode='html', reply_markup = inline_markup)

        if json.loads(call.data)["metod"] == "order_table":
            start = "2022-11-10T" + json.loads(call.data)["time"] + ":00+04:00"
            end =  "2022-11-10T" + floattime_to_str(str_to_floattime(json.loads(call.data)["time"])+4) + ":00+04:00"
            tbl = json.loads(call.data)["table"]
            data = {'start_time': start, 'end_time': end,'table' : tbl}
            response = requests.post(endpoint, json=data)
            print(response)
            print(data)

    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)


#start = time.time()
#print(get_free_table_time_var("3"))     
#end = time.time() - start
#print(end)



