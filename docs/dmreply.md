## `dmreply`
This does the exact same thing as `reply` above, but instead of sending the message in the current channel, it sends the message in the author's DM's. Heres a quick example of how this would be used:

```py
from ZeroBotMaker.client import Client # Import the client

client = Client() # Initalize the client
client.dmreply('Good Morning','gm') # Adds a dm reply command

client.build() # Creates the bot
```