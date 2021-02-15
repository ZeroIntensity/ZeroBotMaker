
## `randommessage`

The `randommessage` method adds a randomized message command to your bot. It has 3 arguments (`response`, `responses`, and `name`). The `response` argument is what the bot replies when a user runs the command. You can pass in `{choice}` to this argument to get the choice. The `responses` argument should be a `list` type object and will have all the choices the bot can choose from to be stored in the `choice` variable. The `name` argument is the name of the command that can be run (default is `randommessage`). Heres a quick example of how this would be used:

```py
from ZeroBotMaker.client import Client # Import the client

client = Client() # Initalize the client
client.randommessage('{choice}',['hey','hi','go away'],'greeting') # Adds a randommessage command

client.build() # Creates the bot
```