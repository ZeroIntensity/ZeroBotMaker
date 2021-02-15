## `snipe`
This adds a snipe system to your bot. It has 2 arguments, `failedresponse` and `name`. The `failedresponse` argument is what the bot says if there was nothing found to snipe. The `name` argument is the name of the command (default is `snipe`). Heres a quick example of how this would be used:

```py
from ZeroBotMaker.client import Client # Import the client

client = Client() # Initalize the client
client.snipe('Nothing to snipe') # Adds a snipe command

client.build() # Creates the bot
```