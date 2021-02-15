class Client:
  def __init__(self):
    self.file = 'bot.py'
    self.prefix = '!'
    self.precode = ''
    self.code = ''

  def changefile(self, name='bot.py'):
    self.file = name
  def build(self):
    self.precode = f'# This code was built with ZeroBotMaker using discord.py\nimport discord\nfrom discord.ext import commands\nimport random\nclient = commands.Bot(command_prefix = "{self.prefix}")\n'
    self.code = self.precode + self.code
    f = open(self.file, 'w+')
    f.write(self.code)
    f.close()


  def changeprefix(self, pre='!'):
    self.prefix = pre
  def randommessage(self, response, responses, name='randommessage'):
    self.code += f'''
@client.command()
async def {name}(ctx):
  choice = random.choice({responses})
  await ctx.send(f"{response}")
'''
  def reply(self, response, name='reply'):
    self.code += f'''
@client.command()
async def {name}(ctx):
  await ctx.send(f"{response}")
async def {name}(c
'''
  def dmreply(self, response, name='dmreply'):
    self.code += f'''
@client.command()
async def {name}(ctx):
  await ctx.author.send(f"{response}")
'''
  def ban(self, response, failedresponse, name='ban'):
    self.code += f'''
@client.command()
@commands.has_permissions(ban_members=True)
async def {name}(ctx, member: discord.Member = None, reason=None):
  if not member:
    await ctx.send(f"{failedresponse}")
  else:
    await ctx.send(f"{response}")
    await member.ban(reason=reason)'''

  def errorhandler(self, response):
    self.code += f'''
@client.event
async def on_command_error(ctx, error):
    await ctx.send("{response}")
  '''

  def messagefilter(self, response, messages):
    self.code += f'''
@client.event
async def on_message(message):
  filter = {messages}
  for i in filter:
    if i == message.content:
      await message.channel.send(f"{response}")
      await message.delete()
  await client.process_commands(message)'''

  def kick(self, response, failedresponse, name='kick'):
    self.code += f'''
@client.command()
@commands.has_permissions(kick_members=True)
async def {name}(ctx, member: discord.Member = None, reason=None):
  if not member:
    await ctx.send(f"{failedresponse}")
  else:
    await ctx.send(f"{response}")
    await member.kick(reason=reason)'''

  def ping(self, response, name='ping'):
    self.code += f'''
@client.command()
async def {name}(ctx):
  bot_ping = round(client.latency * 1000)
  await ctx.send(f"{response}")'''
  def purge(self, response, name='purge'):
    self.code += f'''
@client.command()
@commands.has_permissions(manage_messages=True)
async def {name}(ctx, amount=1):
  await ctx.channel.purge(limit=amount)
'''
  def snipe(self, failedresponse, name='snipe'):
    f = open('snipes.json', 'w+')
    f.close()
    self.code += f'''
import json

@client.event
async def on_message_delete(message):
  with open("snipes.json", "r") as f:
    snipes = json.load(f)''' + '''
  x = {
  "content": str(message.content),
  "author": str(message.author)
    }''' + f'''
  snipes[str(message.channel.id)] = x
  with open("snipes.json", "w") as f:
    json.dump(snipes, f) 

@client.command()  
async def {name}(ctx):
  try:
    with open("snipes.json", "r") as f:
      snipes = json.load(f)
      message = snipes[str(ctx.message.channel.id)]
  except:
    await ctx.send(f'{failedresponse}')
    return
  await ctx.send(message.get("content"))
'''
  def randomnumber(self, response, min, max, name='randomnumber'):
    self.code += f'''

@client.command()
async def {name}(ctx):
  number = random.randint({min}, {max})
  await ctx.send(f"{response}")
'''