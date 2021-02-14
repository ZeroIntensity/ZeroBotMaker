from ZeroBotMaker.client import Client # Import the client

client = Client() # Initalize the client

client.changeprefix('prefix!') # Change the prefix to prefix!
client.reply('hi there', 'hello') # Adds a reply command
client.randomnumber('number: {number}', 1, 10, 'random') # Adds a random number command
client.build() # Bulds the bot