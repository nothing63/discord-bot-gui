import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bg_task = self.loop.create_task(self.my_background_task())

    async def my_background_task(self):
        await self.wait_until_ready()
        channel = self.get_channel(494160969107505156) # Channel ID
        while not self.is_closed():
            x = input("x: ")
            await channel.send(x)

client = MyClient()
client.run('token')