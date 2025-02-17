import discord
from discord.ext import commands
from api_contents import api
from components.EventPaginator import EventPaginator


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

@bot.tree.command(name="hello", description="Say hello!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello, {interaction.user.mention}!")

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command(name='clear')
async def clear(ctx, amount):
    if not ctx.author.guild_permissions.manage_messages:
        await ctx.send("You do not have permission to use this command.")
        return
    if not amount.isdigit():
        await ctx.send("Please provide a valid number.")
        return
    amount = int(amount)
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"Cleared {amount} messages.")

# Endpoint to search for events in a specific city at a specific radius
@bot.command(name="events")
async def events(ctx: commands.Context):
    await ctx.send("Please enter the city name:")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg_city = await ctx.bot.wait_for("message", check=check, timeout=30.0)
    except asyncio.TimeoutError:
        await ctx.send("You took too long to respond. Command cancelled.")
        return
    city = msg_city.content.strip()

    await ctx.send("Please enter the search radius in kilometers:")
    try:
        msg_radius = await ctx.bot.wait_for("message", check=check, timeout=30.0)
    except asyncio.TimeoutError:
        await ctx.send("You took too long to respond. Command cancelled.")
        return
    try:
        radius_value = int(msg_radius.content.strip())
    except ValueError:
        await ctx.send("Invalid radius. Please enter a numeric value.")
        return

    events_list = api.specific_search(city, radius_value)
    if not events_list:
        await ctx.send("No events found nearby.")
        return

    view = EventPaginator(events_list, ctx.author)
    embed = view.get_current_page_embed()
    await ctx.send(embed=embed, view=view)



with open("api_contents/token.txt", "r") as file:
    TOKEN = file.read().strip()

bot.run(TOKEN)
