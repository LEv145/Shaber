
from . import models
from aiohttp import web

class Wiki(models.BaseRedirect):
	async def get(self): return web.Response(
			text = 'Coming soon...')
