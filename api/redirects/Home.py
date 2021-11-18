
from . import models
from aiohttp import web

import aiohttp_jinja2 as aiojinja2

'''i don't know html/css/js
rejoice at what you have'''

class Home(models.BaseRedirect, path = ''):
	@aiojinja2.template('index.html')
	async def get(self):
		return {}
