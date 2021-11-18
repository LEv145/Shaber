
import os

import hcl

import aiofiles

#yes, i am an idiot and do not deny it
async def configLoad():
	async with aiofiles.open('./vars.hcl') as config:
		return hcl.loads(await config.read())
