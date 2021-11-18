
#why did you come here?
#it's just shit code, don't look at it

import api
import jinja2

import inspect
import logging

import utilities
import colorama

from datetime import date
from aiohttp import web

from colorama import Fore
from inspect import isclass

import aiohttp_jinja2 as aiojinja2

colorama.init(autoreset = True)

class Shaber(web.Application):
    def __init__(self):
        super().__init__(middlewares = (api.errorHandler,))

        #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        for i in inspect.getmembers(api.redirects, predicate = isclass):
            self.router.add_view('/' + i[1].path, i[1]) #fucking aiohttp views

    def run(self, host, port):
        log = utilities.configLoad()['log']

        print(f'Logging: {(state := log["enable"])}\n')

        '''AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'''

        state and logging.basicConfig(
            level = logging.INFO,
            format = log['format'],
            datefmt = log['dateFormat'],

            handlers = (
                logging.FileHandler(log['path'] + '%s.log' % \
                    date.today().strftime('%d_%b_%Y')),
                
                logging.StreamHandler()
            )
        ) #fucking logging

        print(Fore.BLUE + f''' _____  _             _                 
/  ___|| |           | |                
\ `--. | |__    __ _ | |__    ___  _ __ 
 `--. \| '_ \  / _` || '_ \  / _ \| '__|
/\__/ /| | | || (_| || |_) ||  __/| |   
\____/ |_| |_| \__,_||_.__/  \___||_|   
            {Fore.RESET}Version: {Fore.YELLOW}{api.__version__}{Fore.BLUE}
                                        \n''')

        #~oh, ~uh... hardcode
        aiojinja2.setup(self, loader = jinja2.FileSystemLoader('./api/templates'))
        web.run_app(self, host = host, port = port, access_log_format = '%a / %r / %s | %{User-Agent}i')
