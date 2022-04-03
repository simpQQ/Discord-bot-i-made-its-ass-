import lightbulb
import hikari
import random
bot = lightbulb.BotApp(token='', prefix = "!")

@bot.listen(hikari.StartedEvent)
async def on_started(event):
  print("start")
bot

r1 = random.randint(1, 100)

print("Random number between 5 and 15 is % s" % (r1))

@bot.command
@lightbulb.command('kill', 'does what it says')
@lightbulb.implements(lightbulb.PrefixCommand)
async def kill(ctx: lightbulb.Context) -> None:
  await ctx.respond("*kills you*")
bot

@bot.command
@lightbulb.command('gay', 'you gay?')
@lightbulb.implements(lightbulb.PrefixCommand)
async def gay(ctx: lightbulb.Context) -> None:

  
  await ctx.respond("Your gay Percentage is % s" % (r1))

bot.run()