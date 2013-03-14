from plugin import Plugin
import requests
import re

export_plugin = Plugin()
@export_plugin.command(["lolcat", "lolcats"])
def lolcats(client, message, rest):
    res = requests.get("http://www.reddit.com/r/lolcats/.json").text
    cats = re.findall(r'"url": "([^"]+.jpe?g)"' res)
    from random import choice
    if len(a) > 0:
        return choice(cats)
    else:
        return ""
