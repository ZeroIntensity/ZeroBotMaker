## `changeprefix`

The `changeprefix` function is used to change the prefix of the bot. The default prefix is `!`. Heres a quick example of how this would be used:

```py
from ZeroBotMaker.client import Client # Import the client

client = Client() # Initalize the client
client.changeprefix('newprefix!') # Changes the prefix

client.build() # Creates the bot
```