
import api

from . import models
from aiohttp import web

class Version(models.BaseRedirect):	
	async def get(self): return web.Response(
			text = api.__version__)
