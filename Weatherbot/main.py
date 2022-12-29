import time

import requests
from bs4 import BeautifulSoup
import telebot
from datetime import datetime, timedelta

bot = telebot.TeleBot('5856331325:AAFNFv-o3O4G-2drabTJmZ21EWNQIU6fsxY', parse_mode=None)
BOT_URL = "URL"

def info_dm():
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    html_doc = requests.get('https://www.gismeteo.ru/weather-krasnodar-5136/tomorrow/', headers=headers)
    info = BeautifulSoup(html_doc.text, 'html.parser')
    weather_dict = {}
    value_time_filter = []
    value_icon_filter = []
    value_temp_filter = []
    value_time = info.find('div', class_="widget-row widget-row-time")
    value_icon = info.find('div', class_="widget-row widget-row-icon")
    value_temp = info.find_all('span', class_="unit unit_temperature_c")
    for x in value_time:
        z=str(x.span.text).zfill(4)[0:2]+':00'
        value_time_filter.append(z)
    for x in value_icon:
        if x.div['data-text'] == 'Пасмурно, небольшой  дождь':
            z = 'Дождь'
            value_icon_filter.append(z)
        elif x.div['data-text'] == 'Пасмурно,  дождь':
            z = 'Дождь'
            value_icon_filter.append(z)
        elif x.div['data-text'] == 'Пасмурно, небольшие  осадки':
            z = 'Осадки'
            value_icon_filter.append(z)
        elif x.div['data-text'] == 'Малооблачно, небольшой  снег с дождём':
            z = 'Дождь'
            value_icon_filter.append(z)
        else:
            z=x.div['data-text']
            value_icon_filter.append(z)
    for x in value_temp:
        value_temp_filter.append(x.text)
    value_temp_filter = value_temp_filter[6:]
    for i in range(8):
        dict1 = {value_time_filter[i]:{'time':value_time_filter[i], 'icon':value_icon_filter[i], 'temp':value_temp_filter[i]}}
        weather_dict.update(dict1)
    return weather_dict
twomorrow_date = datetime.now() + timedelta(days=1)
twomorrow_day = twomorrow_date.strftime("%d.%m.%Y")
time_now = datetime.now()
current_time = time_now.strftime("%H:%M")
while True:
    time.sleep(35)
    if current_time == '14:56':
        x = info_dm()
        msg = f'Прогноз на:\n{twomorrow_day}\n{x["00:00"]["time"]}{x["00:00"]["temp"]: ^10}{x["00:00"]["icon"]}\n{x["03:00"]["time"]}{x["03:00"]["temp"]: ^10}{x["03:00"]["icon"]}\n{x["06:00"]["time"]}{x["06:00"]["temp"]: ^10}{x["06:00"]["icon"]}\n{x["09:00"]["time"]}{x["09:00"]["temp"]: ^10}{x["09:00"]["icon"]}\n{x["12:00"]["time"]}{x["12:00"]["temp"]: ^10}{x["12:00"]["icon"]}\n{x["15:00"]["time"]}{x["15:00"]["temp"]: ^10}{x["15:00"]["icon"]}\n{x["18:00"]["time"]}{x["18:00"]["temp"]: ^10}{x["18:00"]["icon"]}\n{x["21:00"]["time"]}{x["21:00"]["temp"]: ^10}{x["21:00"]["icon"]}\n'
        bot.send_message(-713231502, msg)


bot.infinity_polling()

