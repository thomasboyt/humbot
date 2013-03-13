from flask import Flask, request
import humbug
import requests
import json
import config

from plugin import Plugin, PluginsController
plugins = PluginsController()

app = Flask(__name__)

hb_client = humbug.Client(
    api_key = config.API_KEY,
    email = config.EMAIL,
    verbose = True)

github = Plugin()
@github.command(["repo", "searchrepo"])
def search_repo(client, message, rest):
    r = requests.get("https://api.github.com/legacy/repos/search/%s" % rest)
    repo = r.json()['repositories'][0]
    url = "https://github.com/%s/%s" % (repo['owner'], repo['name'])
    result = "Found GitHub repository: [%s/%s](%s)" % (repo['owner'], repo['name'], url)

    client.send_message({
        "type": "stream",
        "to": message['stream'],
        "subject": message['subject'],
        "content": "**BOT**: @**%s** %s" % (message['sender'], result)
    }) 
plugins.append(github)

def handle_message(message):
    text = message['content']
    if (text.startswith(config.PREFIX)):
        text = text[1:]
        (cmd, rest) = text.split(" ", 1)
        if cmd in plugins.commands:
            print message
            print rest
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
    app.debug = CONFIG.debug
    app.run()
