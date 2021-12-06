import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):

        if message.author == self.user:
            return
        if message.content == 'eh':
            await message.channel.send('ehhh https://tenor.com/view/pain-sad-anime-smoke-gif-20376521')
        if message.content == 'lol':
            await message.channel.send('https://cdn.discordapp.com/attachments/452219191580295168/916737920541536266/video0-5.mov')
        if message.content == 'mad?':
            await message.channel.send('https://cdn.discordapp.com/attachments/832423825076912128/907698339804479538/video0.mp4')
        if message.content == 'dobra ty też wypierdalasz':
            await message.channel.send('https://tenor.com/view/gears-of-war-gears-of-war-execution-gif-6187199')
        if message.content == 'DOBRA TY TEŻ WYPIERDALASZ':
            await message.channel.send('https://tenor.com/view/gears-of-war-gears-of-war-execution-gif-6187199')
        if message.content == 'ping':
            await message.channel.send('pong')
        if message.content == 'ping':
            await message.channel.send('pong')
        if message.content == 'ping':
            await message.channel.send('pong')
client = MyClient()
client.run('OTE2NzQ4MzA0NjU2NzY5MDQ0.YauqZA.gMVjScULR6UL6AbaL8TwmQpt5NQ')
