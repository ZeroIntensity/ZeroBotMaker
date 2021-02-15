## `messagefilter`
You can use this to add a message filter to your bot. It has 2 arguments (`reponse`, `messages`). The response argument is what the bot says when someone says a phrase thats in the `messages` argument. The `messages` argument is what messages you want the bot to block. Instead of passing in a `str` type object, you put in a `list` object for this one. Heres a quick example of how this would be used:

```py
from ZeroBotMaker.client import Client # Import the client

client = Client() # Initalize the client
client.messagefilter('{message.author.mention} you can\'t say that word!', ['zerointensity is bad','zerointensity isn\'t good']) # Adds a message filter

client.build() # Creates the bot
```