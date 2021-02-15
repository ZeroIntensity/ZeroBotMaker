## `randomnumber`
This will add a random number command to your bot. It has 4 arguments (`response`, `min`, `max`, `name`). The `reponse` argument is what the bot replies. You can pass in `{number}` to the `reponse` argument to get the random number. The `min` argument is the minimum number it can generate. The `max` argument is the maximum number it can generate. The `name` argument is the name of the command (default is `randomnumber`). Heres a quick example of how this would be used:

```py
from ZeroBotMaker.client import Client # Import the client

client = Client() # Initalize the client
client.randomnumber('Number: {number}', 1, 10) # Adds a random number command

client.build() # Creates the bot
```