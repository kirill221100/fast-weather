from fastapi import Request


class SettingsForm:
    def __init__(self, request: Request):
        self.request = request
        self.mes_sys: str = ''

    async def load_data(self):
        form = await self.request.form()
        self.mes_sys = form.get('options')
