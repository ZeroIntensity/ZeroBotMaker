## `purge`
This method will add a `purge` command to your bot. It has 2 arguments (`response`, `name`). The `reponse` argument is what the bot replies when it purges the messages. The `name` argument is the name of the command (default is `purge`). Heres a quick example of how this would be used:


```py
from ZeroBotMaker.client import Client # Import the client

client = Client() # Initalize the client
client.purge('Purged {amount} messages') # Creates purge command

client.build() # Creates the bot
```