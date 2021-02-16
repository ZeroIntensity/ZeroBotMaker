## `token`
Like the build method, the `token` method *should* be used in every script that uses ZeroBotMaker, but I didn't put it in the rest of the docs since it would create an unworking script as an example. This method has only 1 argument, which is the token. You can pass in `{os.environ.get("your token env key")}` if you don't want the token in plain text and want to load it from a `.env` file. Here's an example of how this would be used:

```py
from ZeroBotMaker.client import Client # Import the client

client = Client() # Initalize the client
client.token('{os.environ.get("TOKEN")}') # Adds a token from a .env file
client.build() # Creates the bot
```