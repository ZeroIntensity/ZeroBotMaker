
## `reply`
A very simple command. Only arguments are `response` and `name`. `reponse` is what the bot replies, `name` is what the command name is (default is `reply`). Heres a quick example of how this would be used:

```py
from ZeroBotMaker.client import Client # Import the client

client = Client() # Initalize the client
client.reply('Hello!', 'hello')

client.build() # Creates the bot
```