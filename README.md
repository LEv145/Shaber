# Shaber
![Python](https://img.shields.io/badge/Python-3.8%5E-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green)

A wrapper for the [Spore API](http://www.spore.com/comm/samples) that simplifies and complements its functionality

# Features
- JSON instead of XML
- WebSocket Radio (Coming soon...)
- SporePedia (Coming soon...)
- WikiPedia[eng only] (Comins soon...)

## How is the wrapper different from the original api?
It's okay that you ask this question (to be honest, I would ask myself). There are not many differences at the moment, but in the future there will be many innovations listed above.

# Deploying on host
Although the wrapper is public and available by url, you can also place it on your server
- ### Install dependencies
```pip install -r requirements.txt```
- ### Rename `config.yml.example` to `config.yml` and setting up it (although you can just delete it)
```yml
log:
  enable: false

  format:
    "\n[%(asctime)s.%(msecs)03d] | %(message)s\n"

  dateFormat:
    "%Y/%m/%d %H:%M:%S"

  path:
    "logs/"
```
- ### Run the server
```python main.py```
By default the server will start: 0.0.0.0:8080
Optional parameters
```
--ip IP (0.0.0.0/localhost)
--port PORT (62340)
```

# Client libraries
There are currently no clients available. But you can become one of the first by following this [documentation](https://github.com/Sherolld/Shaber/blob/main/implementation.md). Don't miss this opportunity <3 Just contact me (if of course you have a desire to do this): Sherolld#6561

<details>
  <summary>P.S</summary>
    please don't look at the commits. i don't know how to use github or git, i just want to share code with people :D
</details>
