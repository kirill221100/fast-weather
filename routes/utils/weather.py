import requests, datetime
from core.config import Config as cfg


def get_weather_data(city, mes_sys=None):
    url = ''
    for key, value in cfg.mes_sys.items():
        if value == mes_sys:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units={key}&lang=ru&appid={cfg.API}'
    if not url:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={cfg.API}'
    r = requests.get(url).json()
    if r['cod'] == '404':
        return None
    time = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(seconds=r['timezone']))).strftime("%H:%M")

    return r, mes_sys, time


