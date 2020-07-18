import requests
import json
from tkinter import *

tk=Tk()

tk.title("GUI bot")

entry = Entry(tk, width=25, font=100)

with open('config.json') as f:
  config = json.load(f)

name = str(config['BotName'])

def main(arg=None):
  message = str(entry.get())
  entry.delete(first=0, last=END)

  url = str(config['DiscordWebhookURL'])

  data = {}
  data["username"] = name
  data["content"] = message

  requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})

  print()
  print('Message "{}" send correct'.format(message))

entry.focus()
entry.bind("<Return>", main)
entry.pack()

text = StringVar()
Label(tk, textvariable=text, font=100).pack()
text.set("Enter message and press return to send message")

tk.mainloop()