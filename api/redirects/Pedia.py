
from . import models
from aiohttp import web

class Pedia(models.BaseRedirect): #fucking name
	async def get(self): return web.Response(
			text = 'Coming soon...')
