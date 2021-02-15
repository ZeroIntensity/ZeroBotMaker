## `ping`
This method gets the bot's response time. It has 2 arguments, which are `response` and `name`. The `reponse` argument is what the bot replies. You can pass in `bot_ping` in the `reponse` argument to get the ping. The `name` argument is what the command name is, the default is `ping`. Heres a quick example of how this would be used:

```py
from ZeroBotMaker.client import Client # Import the client

client = Client() # Initalize the client
client.ping('Pong! {bot_ping}ms')

client.build() # Creates the bot
```