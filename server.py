from flask import Flask, request
import humbug
import requests
import json
import config

from plugins.plugin import Plugin
from controller import PluginsController
plugins = PluginsController()

app = Flask(__name__)

hb_client = humbug.Client(
    api_key = config.API_KEY,
    email = config.EMAIL,
    verbose = True)

def handle_message(message):
    text = message['content']
    if (text.startswith(config.PREFIX)):
        text = text[1:]
        try:
            (cmd, rest) = text.split(" ", 1)
        except ValueError:
            cmd = text
            rest = None
        if cmd in plugins.commands:
            return plugins.commands[cmd](hb_client, message, rest)

@app.route("/receiver", methods=["POST"])
def receiver():
    if ("<strong>BOT</strong>:" in request.json['lines'][0]):
        return "Message ignored."
    lines = request.json['lines']
    for paragraph in request.json['lines']:
        print paragraph
        for line in paragraph.split("<br>"):
            msg = {
                "stream": request.json['stream'],
                "subject": request.json['subject'],
                "sender": request.json['sender'],
                "content": line.strip()
            }

            result = handle_message(msg)

            if result:
                hb_client.send_message({
                    "type": "stream",
                    "to": msg['stream'],
                    "subject": msg['subject'],
                    "content": "**BOT**: @**%s** %s" % (msg['sender'], result)
                }) 

                # don't allow multi-line command spamming
                return "Command interpreted."

    return "Message received."

if __name__ == "__main__":
    app.debug = config.DEBUG
    app.run()
