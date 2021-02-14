# Last Updated: 2/14/21

This is a project that allows someone to create their own [discord.py](https://pypi.org/project/discord.py) bot using very basic Python.



**Note:** This is not a finished project, there are still plenty of features to be added. You can see them in the `Planned Features` section below.

## Credits
### Developer
This was developed by [ZeroIntensity](https://zintensity.net). It uses no dependencies (other than [discord.py](https://pypi.org/project/discord.py), which the created `bot.py` file uses.)

## How to use
### Example
Heres a quick example for a basic bot:
```py
from ZeroBotMaker.client import Client # Import the client

client = Client() # Initalize the client

client.changeprefix('prefix!') # Change the prefix to prefix!
client.reply('hi there', 'hello') # Adds a reply command
client.randomnumber('number: {number}', 1, 10, 'random') # Adds a random number command
client.build() # Bulds the bot
```

### Getting started

In order to use this, you must initalize the `Client` object from the `client.py` file. The most preferred method is using this code:
```py
from ZeroBotMaker.client import Client
client = Client()
```

Once you have done this, you can now add commands. To know what to add, look at the `Methods` section below.

## Documentation

Welcome to the documentation. Here you will find how to use every feature this has to offer.

## `build`
The `build` method should be used in every single script that uses ZeroBotMaker. This is the function that creates the file which the code is stored in. The default file for it to be stored is `bot.py`, but you can change it with the `changefile` method. Heres a quick example of how this would be used:

```py
from ZeroBotMaker.client import Client # Import the client

client = Client() # Initalize the client

client.build() # Creates the bot
```

## `changeprefix`

The `changeprefix` function is used to change the prefix of the bot. The default prefix is `!`. Heres a quick example of how this would be used:

```py
from ZeroBotMaker.client import Client # Import the client

client = Client() # Initalize the client
client.changeprefix('newprefix!') # Changes the prefix

client.build() # Creates the bot
```

## `changefile`
This method is used to change the file where the code for the bot is stored. The default is `bot.py`. Heres a quick example of how this would be used:

```py
from ZeroBotMaker.client import Client # Import the client

client = Client() # Initalize the client
client.changefile('code.py') # Changes the file

client.build() # Creates the bot
```

## `ban`
The ban function is used to create a ban command within the bot. it requires 3 arguments (`response`, `failedresponse`, `name`). The `response` argument is what the bot says when it successfully bans the member. The `failedresponse` argument is what the bot says when the author fails to specify a member. The `name` argument is what the name of the command is (default is `ban`). Heres a quick example of how this would be used:

```py
from ZeroBotMaker.client import Client # Import the client

client = Client() # Initalize the client
client.ban('Banned {member}', 'Please specify a member') # Creates ban command

client.build() # Creates the bot
```

## `kick`
This method is the exact same as the `ban` method above, except it bans the member instead of kicking them (and things are renamed ofc)

## `purge`
This method will add a `purge` command to your bot. It has 2 arguments (`response`, `name`). The `reponse` argument is what the bot replies when it purges the messages. The `name` arguement is the name of the command (default is `purge`). Heres a quick example of how this would be used:

```py
from ZeroBotMaker.client import Client # Import the client

client = Client() # Initalize the client
client.purge('Purged {amount} messages') # Creates purge command

client.build() # Creates the bot
```

## `errorhandler`
This will add an error handler to your bot. I recommend adding this to your bot, as it's very helpful. The only argument this has is `reponse`, which is what the bot sends when a command has an error. You can use `{error}` to pass in the error. Heres a quick example of how this would be used:

```py
from ZeroBotMaker.client import Client # Import the client

client = Client() # Initalize the client
client.errorhandler('Error: {error}') # Adds an error handler

client.build() # Creates the bot
```

## `messagefilter`
You can use this to add a message filter to your bot. It has 2 arguments (`reponse`, `messages`). The response argument is what the bot says when someone says a phrase thats in the `messages` argument. The `messages` arguement is what messages you want the bot to block. Instead of passing in a `str` type object, you put in a `list` object for this one. Heres a quick example of how this would be used:

```py
from ZeroBotMaker.client import Client # Import the client

client = Client() # Initalize the client
client.messagefilter('{message.author.mention} you can\'t say that word!', ['zerointensity is bad','zerointensity isn\'t good']) # Adds a message filter

client.build() # Creates the bot
```

## `ping`
This method gets the bot's response time. It has 2 arguments, which are `response` and `name`. The `reponse` argument is what the bot replies. You can pass in `bot_ping` in the `reponse` argument to get the ping. The `name` arguement is what the command name is, the default is `ping`. Heres a quick example of how this would be used:

```py
from ZeroBotMaker.client import Client # Import the client

client = Client() # Initalize the client
client.ping('Pong! {bot_ping}ms')

client.build() # Creates the bot
```

## `reply`
A very simple command. Only arguments are `response` and `name`. `reponse` is what the bot replies, `name` is what the command name is (default is `reply`). Heres a quick example of how this would be used:

```py
from ZeroBotMaker.client import Client # Import the client

client = Client() # Initalize the client
client.reply('Hello!', 'hello')

client.build() # Creates the bot
```

## `snipe`
This adds a snipe system to your bot. It has 2 arguments, `failedresponse` and `name`. The `failedresponse` argument is what the bot says if there was nothing found to snipe. The `name` argument is the name of the command (default is `snipe`). Heres a quick example of how this would be used:

```py
from ZeroBotMaker.client import Client # Import the client

client = Client() # Initalize the client
client.snipe('Nothing to snipe') # Adds a snipe command

client.build() # Creates the bot
```

## `randomnumber`
This will add a random number command to your bot. It has 4 arguments (`response`, `min`, `max`, `name`). The `reponse` arguement is what the bot replies. You can pass in `{number}` to the `reponse` argument to get the random number. The `min` argument is the minimum number it can generate. The `max` argument is the maximum number it can generate. The `name` argument is the name of the command (default is `randomnumber`). Heres a quick example of how this would be used:

```py
from ZeroBotMaker.client import Client # Import the client

client = Client() # Initalize the client
client.randomnumber('Number: {number}', 1, 10) # Adds a random number command

client.build() # Creates the bot
```