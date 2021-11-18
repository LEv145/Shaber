
from . import (
		redirects, 
		utilities
	)

from .middlewares import *

#haha, classic
__version__ = '{build}.{year}.{patch}'.format(**utilities.VersionInfo(
		build = 1, year = 21, patch = 0)._asdict())
