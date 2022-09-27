import requests
from fastapi_utils.tasks import repeat_every
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from uvicorn import run
from core.config import Config as cfg
from routes.weather import router

app = FastAPI()

app.include_router(router)

app.mount('/static', StaticFiles(directory='static'), name='static')

app.add_middleware(SessionMiddleware, secret_key=cfg.SECRET_KEY)


@app.on_event('startup')
@repeat_every(seconds=600)
def get_currency_and_news():
    cfg.usd = round(
        requests.get(f'https://freecurrencyapi.net/api/v2/latest?apikey={cfg.CURRENCY_API}&base_currency=USD').json()
        ['data']['RUB'], 2)
    cfg.eur = round(
        requests.get(f'https://freecurrencyapi.net/api/v2/latest?apikey={cfg.CURRENCY_API}&base_currency=EUR').json()
        ['data']['RUB'], 2)
    cfg.news = requests.get(f'https://newsapi.org/v2/top-headlines?country=ru&apiKey={cfg.NEWS_API}').json()['articles']


if __name__ == '__main__':
    run("main:app", reload=True)
