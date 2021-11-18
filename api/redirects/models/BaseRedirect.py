
import aiohttp

from . import utilities
from aiohttp import web

#crutch and bike
#russian coders be like
class BaseRedirect(web.View): #fucking name
    def __init_subclass__(cls, path = None):
        cls.path = cls.__name__.lower() \
            if path is None else path

    #that's fucked up :/
    async def baseRequest(self, url, page): #fucking name
        async with aiohttp.ClientSession() as session:
            async with session.get((await utilities.configLoad())['urls'][url] \
                + page) as response: return str(await response.read(), 'utf_8')
