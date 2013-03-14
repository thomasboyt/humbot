from plugin import Plugin
import requests
import re

export_plugin = Plugin()
@export_plugin.command(["lolcat", "lolcats"])
def lolcats(client, message, rest):
    res = requests.get("http://www.reddit.com/r/lolcats/.json").text
    cats = re.findall(r'"url": "([^"]+.jpe?g)"', res)
    if len(cats) > 0:
        from random import choice
        return choice(cats)
