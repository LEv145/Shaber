# Documentation on using the wrapper or creating a client for it

## Domain: [shaber.xyz](https://shaber.xyz/)
	* GET > /:
		  Description > Wrapper home page

	* GET > /base:
		  Description > Use any currently available redirect from the original api: spore.com/comm/samples

		  Return > `Json`:
			  successfully(200): `{data: data}`
			  error(error code): `{error code: error message}`

	* GET > /version:
		  Description > Current version of the wrapper

		  Return: `String`

	* GET > /pedia | wiki | radio:
		  Description > Coming soon...		
