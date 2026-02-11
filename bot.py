import discord
from discord.ext import commands
from flask import Flask
import threading
import os

# Tiny web server for Render health checks
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive! 🚀"

def run_flask():
    port = int(os.environ.get("PORT", 5000))  # Render provides this env var
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)

# Run Flask in a separate thread so it doesn't block the bot
threading.Thread(target=run_flask, daemon=True).start()

# Your normal bot code
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # if needed

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('Bot is ready! 🎉')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! 🏓')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}! 👋')

# Run bot with token from env var (safer)
bot.run(os.environ['DISCORD_TOKEN'])
