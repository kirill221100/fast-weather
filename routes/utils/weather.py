import aiohttp, datetime, json
from redis_conf import redis
from core.config import Config as cfg


async def get_weather_data(city, mes_sys):
    result = await redis.get(city)
    if result:
        result = json.loads(result)
        time = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(seconds=result['timezone']))).strftime("%H:%M")
        return result, mes_sys, time
    url = ''
    for key, value in cfg.mes_sys.items():
        if value == mes_sys:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units={key}&lang=ru&appid={cfg.API}'
    async with aiohttp.ClientSession() as request:
        async with request.get(url) as r:
            result = await r.json()
    if result['cod'] == '404':
        return None
    await redis.set(name=city, value=json.dumps(result), ex=3600)
    time = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(seconds=result['timezone']))).strftime("%H:%M")

    return result, mes_sys, time


