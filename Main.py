import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("Clearing global commands...")

    try:
        bot.tree.clear_commands(guild=None)  # ❌ no await here
        await bot.tree.sync()  # ✅ still await this
        print("✅ Global commands cleared.")
    except Exception as e:
        print(f"❌ Failed to clear commands: {e}")

    await bot.close()

bot.run(TOKEN)
