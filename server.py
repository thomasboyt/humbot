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
        (cmd, rest) = text.split(" ", 1)
        if cmd in plugins.commands:
            plugins.commands[cmd](hb_client, message, rest)

@app.route("/receiver", methods=["POST"])
def receiver():
    if ("<strong>BOT</strong>:" in request.json['lines'][0]):
        return "Message ignored."
    for line in request.json['lines']:
        msg = {
            "stream": request.json['stream'],
            "subject": request.json['subject'],
            "sender": request.json['sender'],
            "content": line
        }

        handle_message(msg)

    return "Message received."

if __name__ == "__main__":
    app.debug = config.DEBUG
    app.run()
