
from aiohttp import web

'''*evil developer sounds*'''
@web.middleware
async def errorHandler(request, handler): #fucking name
    try: #fucking try-return
        return await handler(request)
    except (Exception, web.HTTPException) as exception:
        return web.json_response({'error': 'Internal Server Error' if \
            type(exception).__name__ == 'ExpatError' else str(exception)}, 
                status = exception.status if hasattr(exception, 
                    'status') else 500) #fucking condition
