
import ujson
import xmltodict as xml

from aiohttp import web
from . import models

class Base(models.BaseRedirect, path = r'base/{page:.*}'):
	async def get(self): return web.json_response(ujson.loads(ujson.dumps(xml.parse(
			await self.baseRequest('spore', self.request.match_info['page'])))))
