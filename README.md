# Last Updated: 2/14/21

This is a project that allows someone to create their own [discord.py](https://pypi.org/project/discord.py) bot using very basic Python.



**Note:** This is not a finished project, there are still plenty of features to be added. You can see them in the `Planned Features` section below.

## Credits
### Developer
This was developed by [ZeroIntensity](https://zintensity.net). It uses no dependencies (other than [discord.py](https://pypi.org/project/discord.py), which the created `bot.py` file uses.)

## Planned Features
- Allow commands to work with embeds
- More commands

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

Once you have done this, you can now add commands. To know what to add, look at the documentation.

