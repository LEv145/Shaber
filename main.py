
from argparse import ArgumentParser
from server import Shaber as server

parser = ArgumentParser(description = server.__name__ + ' | Spore API Wrapper')
parser.add_argument('--port', type = int, help = 'Port Server')
parser.add_argument('--ip', help = 'Server IP')

print('\33]0;%s\a' % parser.description, end = '', flush = True)
server().run(parser.parse_args().ip, parser.parse_args().port)

#fuck it all
