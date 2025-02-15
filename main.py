import os
import asyncio 
import discord 
from discord import Webhook
import aiohttp 

print("""
  _  ______   ___  _  ______ ___ _   _ ____  _  _____ 
 | |/ /  _ \ / _ \| |/ / ___|_ _| \ | / ___|| |/ /_ _|
 | ' /| |_) | | | | ' /\___ \| ||  \| \___ \| ' / | | 
 | . \|  _ <| |_| | . \ ___) | || |\  |___) | . \ | | 
 |_|\_\_| \_\\___/|_|\_\____/___|_| \_|____/|_|\_\___|
                                                      
""")

async def anything(url):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(url, session=session)
        title=input("Input title : ")
        embed = discord.Embed(title=title)
        name = input("Print message: ")
        embed.add_field(name=name, value='', inline=True)
        embed.set_image(url='https://media1.tenor.com/m/5Xw3hRmmtsoAAAAd/cover-page-hacker-man.gif')
        username = input("Set webhook name: ")
        
        count = int(input("How many times to send the embed? "))

        link = input("Your Discord link: ")

        for _ in range(count):
            await webhook.send(content=f"@everyone {link}", embed=embed, username=username)

        delete = input("Do you want to delete the webhook? (yes/no): ").strip().lower()
        if delete in ["yes", "y"]:
            await webhook.delete()
            print("Webhook has been deleted.")
        else:
            print("Webhook was not deleted.")

if __name__ == "__main__":
    url = input('Input webhook link: ')

    loop = asyncio.new_event_loop()
    loop.run_until_complete(anything(url))
    loop.close()
