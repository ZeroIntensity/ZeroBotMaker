## `ban`
The ban function is used to create a ban command within the bot. it requires 3 arguments (`response`, `failedresponse`, `name`). The `response` argument is what the bot says when it successfully bans the member. The `failedresponse` argument is what the bot says when the author fails to specify a member. The `name` argument is what the name of the command is (default is `ban`). Heres a quick example of how this would be used:

```py
from ZeroBotMaker.client import Client # Import the client

client = Client() # Initalize the client
client.ban('Banned {member}', 'Please specify a member') # Creates ban command

client.build() # Creates the bot
```