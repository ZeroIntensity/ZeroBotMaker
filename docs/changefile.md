## `changefile`
This method is used to change the file where the code for the bot is stored. The default is `bot.py`. Heres a quick example of how this would be used:

```py
from ZeroBotMaker.client import Client # Import the client

client = Client() # Initalize the client
client.changefile('code.py') # Changes the file

client.build() # Creates the bot
```
