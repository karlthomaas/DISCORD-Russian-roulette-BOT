import discord, random, time
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='.', intents=intents)
TOKEN = "" # token goes here

@client.event
async def on_ready():
    print("Bot is ready")

# everybody can use that command
@client.command()
async def spin(ctx, reason=None):
    kuulid = random.randint(1, 7) # 1 out of 6 is the chance of dying
    kuul = 1
    await ctx.send("Spinning...")
    time.sleep(2)
    if kuul == kuulid: # if random number is number one, then the gun goes off
        await ctx.send("Pow")
        await ctx.author.kick(reason=reason) # kicks the command author
    else:
        await ctx.send("Click.. revolver, didn't go off")

# only roles, who can kick people, can use this command
# you need to type ".fspin <@member>" and if the gun goes off, then the person get's kicked off
@client.command()
@commands.has_permissions(ban_members=True) 
async def fspin(ctx,member: discord.Member, *, reason=None):
    kuulid = random.randint(1, 7)
    kuul = 1
    await ctx.send("Spinning...")
    time.sleep(2)
    if kuul == kuulid:
        await ctx.send(f"Pow {member} has died.")
        await member.kick(reason=reason)
    else:
        await ctx.send("Click.. revolver, didn't go off")

@fspin.error
async def fspin_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"You don't have enough permissions {ctx.author}.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"You need to @ a victim.")


client.run(TOKEN)
