'''
free cheeseburger mike, a Discord bot that generates Nitro codes using GX.
Copyright (C) 2023  Emily Daemon

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import discord
from discord.ext import commands
import requests
import uuid
import json
import sys
from http.client import responses
from datetime import datetime

intents = discord.Intents.default()
# command_prefix will never be used, but it's a necessary parameter
client = commands.Bot(command_prefix="!", intents=intents)

try:
    with open("config/config.json") as f:
        config = json.load(f)
except FileNotFoundError:
    print("Error: Config not found. Did you forget to copy config.def.json to config.json?")
    sys.exit()

@client.event
async def on_ready():
    await client.tree.sync()
    print("Logged in as "+str(client.user))

@client.tree.command(name = "gimme", description = "free cheeseburger mike")
async def give_command(interaction, private: bool = True):
    await interaction.response.defer(ephemeral=private)

    headers = {
        'Content-Type': 'application/json',
    }

    data = {
        'partnerUserId': str(uuid.uuid4()),
    }

    r = requests.post(config["gxurl"], headers=headers, json=data)

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    statusf = f"{r.status_code} {responses[r.status_code]}"
    print(f"[{timestamp}] {interaction.user} tried to generate code. got {statusf}")

    if r.status_code != 200:
        await interaction.followup.send(f"Error! Got HTTP status code `{statusf}`. Try again later.")
        return

    giftcode=r.json()["token"]
    output=config["gifturl"]+giftcode
    await interaction.followup.send(f"[Here you go mate, cheers \N{thumbs up sign}]({output})")

client.run(config["token"])
