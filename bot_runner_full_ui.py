import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from responses import (
    get_start_day_message,
    get_log_trade_message,
    get_rex_daily_message,
    get_rex_weekly_message
)

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot connecté en tant que {bot.user}")
    channel_id = 1360251758168903792
    channel = bot.get_channel(channel_id)
    if channel:
        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="📋 Start Day", style=discord.ButtonStyle.primary, custom_id="start_day_button"))
        view.add_item(discord.ui.Button(label="🖊️ Log Trade", style=discord.ButtonStyle.secondary, custom_id="log_trade_button"))
        view.add_item(discord.ui.Button(label="📘 End of Day", style=discord.ButtonStyle.success, custom_id="end_day_button", row=1))
        view.add_item(discord.ui.Button(label="📊 End of Week", style=discord.ButtonStyle.danger, custom_id="end_week_button", row=1))
        await channel.send("**Assistant IA Ready** ⚙️\nUtilise les boutons ci-dessous :", view=view)

@bot.event
async def on_interaction(interaction: discord.Interaction):
    cid = interaction.data.get("custom_id")
    if cid == "start_day_button":
        await interaction.response.send_message(get_start_day_message(), ephemeral=False)
    elif cid == "log_trade_button":
        await interaction.response.send_message(get_log_trade_message(), ephemeral=False)
    elif cid == "end_day_button":
        await interaction.response.send_message(get_rex_daily_message(), ephemeral=False)
    elif cid == "end_week_button":
        await interaction.response.send_message(get_rex_weekly_message(), ephemeral=False)

bot.run(TOKEN)
