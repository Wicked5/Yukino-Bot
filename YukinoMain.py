#discord package. start of yuki bot
import discord
import asyncio 
import random
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import webgrab 
import wiki

#creates the bot as an object
client = commands.Bot(command_prefix = '.')          #discord.Client()



@client.command(name="hello")
async def hello(context):
    await context.message.channel.send("Hello!")

#target: allows for the mentioning of a member within a command also gives the parameter to the command
@client.command(name="hit")
async def hit(context, target: discord.Member):
    chance = random.randint(0, 1)
    if(chance == 0):
        hitembed = discord.Embed(title = "Fight!", description = context.author.name + " is hitting " + target.mention + " !")
        hitembed.set_image(url = "https://media1.tenor.com/images/6533150eda201b2046372388c69477f8/tenor.gif")
        await context.message.channel.send(embed = hitembed)
    else:
        hitembed = discord.Embed(title = "Fight!", description = context.author.name + " is hitting " + target.mention + " !")
        hitembed.set_image(url = "https://yaharibento.files.wordpress.com/2016/03/yahari-oregariu-anime-ep6-13-hikigaya-hachiman-yukinoshita-haruno-yukino.gif")
        await context.message.channel.send(embed = hitembed)

@client.command(name = "assist")
async def help(context):
    helpembed = discord.Embed(title = "Help", description = "Just look at #info-about-yukino-bot for now. If the bot branches out or becomes more complex, I'll develop this command")
    await context.message.channel.send(embed =  helpembed)

@client.command(name="ily")
async def ily(context):
    chance = random.randint(1,100)
    if(chance == 1):
        await context.message.channel.send("I love you too " + context.author.mention)
        ilyembed = discord.Embed()
        ilyembed.set_image(url= "https://media1.tenor.com/images/df345992e40f1daabaa6f224d41d5478/tenor.gif")
        await context.message.channel.send(embed = ilyembed)
    else:    
        await context.message.channel.send("How can you say something so bold " + context.author.mention + "?! Baka")
        ilyembed = discord.Embed()
        ilyembed.set_image(url= "https://static3.cbrimages.com/wordpress/wp-content/uploads/2020/10/my-youth-romantic-comedy-snafu-hachiman-yukino-confession.jpg")
        await context.message.channel.send(embed = ilyembed)

@client.command(name= "hug")
async def hug(context, target: discord.Member):
    chance = random.randint(0,1) 
    if(chance == 0):
        hugembed = discord.Embed(title = "Awwww <3", description = context.author.name + " is hugging " + target.mention + " !")
        hugembed.set_image(url = "https://media1.tenor.com/images/dec84ca72d99c93c8a46af5432f87d27/tenor.gif")
        await context.message.channel.send(embed = hugembed)
    else:
        hugembed = discord.Embed(title = "Awwww <3", description = context.author.name + " is hugging " + target.mention + " !")
        hugembed.set_image(url = "https://data.whicdn.com/images/59654020/original.gif")
        await context.message.channel.send(embed = hugembed)


@client.event
async def on_ready():
    embedgreet = discord.Embed(title = "Yukino Yukinoshita", description = "I am back online!", color= 0x0000ff)
    embedgreet.set_image(url = "https://64.media.tumblr.com/a52d16202fa47ae1db3bc9440d3a097d/7d2f7a3f5220113d-3c/s500x750/482eaeab6e7aed56e20b66cec378e6f284e8f515.gif")
    general = client.get_channel(793928470740336672)
    await general.send(embed=embedgreet)
    activity = discord.Game("Being Best Girl")
    await client.change_presence(activity= activity)

@client.event
async def on_message(message):
    '''if(message.content.lower().find("happy birthday") > -1):
        ctx = await client.get_context(message)
        await ctx.send("Thank you very much {}!".format(message.author.mention))'''

    if(message.content.lower() == "yahallose"):
        ctx = await client.get_context(message)
        pic = random.randint(1, 3) #had to rename random to pic. interfered with line 149, yukino = random.randint(1,3)

        if(pic == 1): 
            await ctx.send("Yui says fuck you " + message.author.mention)
        elif(pic == 2):
            await ctx.send("You shouldn't say something like that")
        else:
            await ctx.send("{}-lose".format(message.author))
    
    if(message.content.lower() == "nya"):
        ctx = await client.get_context(message)
        nyaembed = discord.Embed()
        nyaembed.set_image(url = "https://media1.tenor.com/images/87cfa037a49aa3d8636cefd6e3d46b20/tenor.gif")
        await ctx.send(embed = nyaembed)

    if message.content.startswith(".counting"):
        chance1 = random.randint(1,2) #determines who goes first
        chance2 = random.randint(1,3) #determines how many numbers bot counts
        counter = 0 #what number the game is on
        turn = 0 

        if(chance1 == 1): #bots turn
            await message.channel.send("Game to 21. I'll start first\n{}\nPick 1, 2, or 3".format(chance2))
            counter += chance2
            turn += 1
        else: #person's turn
            await message.channel.send("Game to 21. You start first. Pick 1, 2, or 3")
            
            def fine(m): #boolean return to check if contents of message is good to use for the bot. If not then it won't count the message. 
                         #We want to check that the message is from the originator and if they use the correct numbers. Bot keeps checking for proper message
                return m.author == message.author and (m.content == "1" or m.content == "2" or m.content.lower() == "3")
            
            try:
                choice = await client.wait_for('message', check = fine, timeout = 8.0)
            except asyncio.TimeoutError:
                return await message.channel.send("If you don't know how to play, check pin in channel")
            
            counter += int(choice.content) 
            turn += 2
            await message.channel.send("The count after your turn is: {}".format(counter))
        
        while(counter < 21):
            if(turn % 2 == 0):          #bots turn
                if(counter == 14 or counter == 15 or counter == 16):
                    counter = 17
                    turn += 1
                    await message.channel.send("The counter is now: {}\nYour turn".format(counter))
                elif(counter == 18 or counter == 19 or counter == 20):
                    await message.channel.send("I won. Good luck next time")
                    break
                else:
                    chance2 = random.randint(1,3)
                    counter += chance2
                    turn += 1
                    await message.channel.send("The counter is now: {}\nYour turn".format(counter))
            
            if(turn % 2 == 1): 
                try:
                    choice = await client.wait_for('message', check = fine, timeout = 8.0)
                except asyncio.TimeoutError:
                    return await message.channel.send("If you don't know how to play, check pin in channel")
            
                counter += int(choice.content) 
                turn += 1
                await message.channel.send("The count after your turn is: {}".format(counter))

            if(counter == 21):
                await message.channel.send("Congrats, you won!")
                

    if message.content.startswith(".rps"):
        await message.channel.send("Rock, paper, scissors, shoot!")
    
        def valid(m):
            return m.author == message.author and (m.content.lower() == "rock" or m.content.lower() == "paper" or m.content.lower() == "scissors")
        
        try:
            choice = await client.wait_for('message', check = valid, timeout = 5.0)
        except asyncio.TimeoutError:
            return await message.channel.send("Don't bother me if you're not gonna take this seriously. Baka")

        yukino = random.randint(1,3)
        player = 0

        if(choice.content.lower() == "rock"): 
            player = 1
        elif(choice.content.lower() == "paper"):
            player = 2
        else:
            player = 3
    
        if((player == 1 and yukino == 3) or (player == 2 and yukino == 1) or (player == 3 and yukino == 2)):
            await message.channel.send("You won")
        elif((player == 1 and yukino == 2) or (player == 2 and yukino == 3) or (player == 3 and yukino == 1)):
            await message.channel.send("You lost")
        else:
            await message.channel.send("We tied")

    if message.content.startswith(".search"):
        await message.channel.send("Enter a topic you'd like to learn more about!")
        topic = ""
    
        def correct(m):
            return m.author == message.author
    
        try:
            topic = await client.wait_for('message', check = correct, timeout = 10.0)
        except asyncio.TimeoutError:
            return await message.channel.send("Please don't use this command if you're not serious.")

        information = wiki.look_up(topic.content)
        await message.channel.send(information)

    if message.content.startswith(".ranime"):
        await message.channel.send(webgrab.generate())

    await client.process_commands(message) #commands won't work if you don't have this here since on_message event blocks everything off





client.run("NzYyNDMzMzMyODQzNTExODQw.X3pFXw.8xWjeyT3sJ1QSn2peu8Tg4QwDwI")