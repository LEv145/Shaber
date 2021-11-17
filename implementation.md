Documentation on using the wrapper or creating a client for it

## Domain: [shaber.xyz](https://shaber.xyz/)

<ul class="nestedList home">
    <li><h3>GET > /:</h3>
        <ul>
             Description > Wrapper home page
        </ul>
    </li>
</ul>

GET > /base:
	Description > Use any currently available redirect from the original api: spore.com/comm/samples

	Return > `Json`:
		successfully(200): {data: data}
		error(error code): {error code: error message}

GET > /version:
	Description > Current version of the wrapper

	Return: String

GET > /pedia | wiki | radio:
	Description > Coming soon...		
