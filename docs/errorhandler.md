
## `errorhandler`
This will add an error handler to your bot. I recommend adding this to your bot, as it's very helpful. The only argument this has is `reponse`, which is what the bot sends when a command has an error. You can use `{error}` to pass in the error. Heres a quick example of how this would be used:

```py
from ZeroBotMaker.client import Client # Import the client

client = Client() # Initalize the client
client.errorhandler('Error: {error}') # Adds an error handler

client.build() # Creates the bot
```