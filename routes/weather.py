from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from .utils.weather import get_weather_data
from .forms.city_form import CityForm
from .forms.settings_form import SettingsForm
from core.config import Config as cfg


router = APIRouter()
templates = Jinja2Templates(directory='templates')


@router.get('/')
async def main_get(request: Request):
    if request.session.get('city'):
        data = get_weather_data(request.session.get('city'), request.session.get('mes_sys'))
        if not data:
            request.session.pop('city')
            return templates.TemplateResponse('weather.html',
                                              {'request': request, 'msg': 'Город не найден :('})
        return templates.TemplateResponse('weather.html', {'request': request,
                                                           'data': data[0],
                                                           'mes_sys': data[1],
                                                           'time': data[2],
                                                           'usd': cfg.usd,
                                                           'eur': cfg.eur,
                                                           'news': cfg.news})
    return templates.TemplateResponse('weather.html', {'request': request})


@router.post('/')
async def main_post(request: Request):
    form = CityForm(request)
    await form.load_data()
    request.session['city'] = form.city
    return RedirectResponse(request.url_for('main_get'), status_code=303)


@router.get('/options')
async def options_get(request: Request):
    return templates.TemplateResponse('options.html', {'request': request})


@router.post('/options')
async def options_post(request: Request):
    form = SettingsForm(request)
    await form.load_data()
    request.session['mes_sys'] = cfg.mes_sys.get(form.mes_sys)
    return RedirectResponse(request.url_for('main_get'), status_code=303)
