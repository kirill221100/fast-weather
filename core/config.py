import os


class Config:
    mes_sys = {
        'standart': {'speed': 'метр/сек.', 'sign': 'K'},
        'imperial': {'speed': 'миль/час', 'sign': '℉'},
        'metric': {'speed': 'метр/сек.', 'sign': '℃'}
    }
    SECRET_KEY: str = os.environ.get('SECRET_KEY')
    API: str = os.environ.get("API")
    NEWS_API: str = os.environ.get("NEWS_API")
    CURRENCY_API: str = os.environ.get('CURRENCY_API')
    usd: float = None
    eur: float = None
    news: dict = None
    redis_url: str = os.environ.get('REDIS_URL')
    redis_password: str = os.environ.get('REDIS_PASSWORD')
