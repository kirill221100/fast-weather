from fastapi import Request


class CityForm:
    def __init__(self, request: Request):
        self.request = request
        self.city: str = ''

    async def load_data(self):
        form = await self.request.form()
        self.city = form.get('city')

