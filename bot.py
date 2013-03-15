import humbug
import requests
import json
import config

from plugins.plugin import Plugin
from controller import PluginsController
plugins = PluginsController()

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

def receiver(message):
    if message['content'].startswith('**BOT**:'):
        return "Message ignored"
    for line in message['content'].split('\n\n'):
        msg = {
            "stream": message['display_recipient'],
            "subject": message['subject'],
            "sender": message['sender_email'],
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
    hb_client.call_on_each_message(receiver)
