import requests
import json

with open('config.json') as f:
  config = json.load(f)

name = str(config['BotName'])

print()

while True:
    message = str(input(": "))

    def send():
        url = str(config['DiscordWebhookURL'])

        data = {}
        data["username"] = name
        data["content"] = message

        requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})

        print()
        print("Message send correct")
        print()

    send()