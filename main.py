import discord
from tkinter import *
import _thread

tk=Tk()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bg_task = self.loop.create_task(self.my_background_task())

    def x(arg=None):
        global m

        m = str(enterM.get())
        print(m)
        enterM.delete(first=0, last=END)

    async def my_background_task(self):
        await self.wait_until_ready()
        channel = self.get_channel(494160969107505156) # Channel ID
        while not self.is_closed():
            #x = input("x: ")
            await channel.send(m)

enterM = Entry(tk, width=20)
enterM.focus()
enterM.bind("<Return>",MyClient.x)
enterM.pack()

client = MyClient()

tk.mainloop()

client.run('NzAyOTg3MDQ1NjA5NTM3NjE3.XqKlSw.RVULHNTCN0vF7iAvit9INd1s2Pk')