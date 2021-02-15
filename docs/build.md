## `build`
The `build` method should be used in every single script that uses ZeroBotMaker. This is the function that creates the file which the code is stored in. The default file for it to be stored is `bot.py`, but you can change it with the `changefile` method. Heres a quick example of how this would be used:

```py
from ZeroBotMaker.client import Client # Import the client

client = Client() # Initalize the client

client.build() # Creates the bot
```