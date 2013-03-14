from plugin import Plugin
import requests
import json
import urllib

export_plugin = Plugin()
@export_plugin.command(["google", "g"])
def google(client, message, rest):
    url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&" + urllib.urlencode({'q': rest})
    res = json.loads(requests.get(url).text)
    res1 = res['responseData']['results'][0]
    return "[" + res1['title'].replace('<b>', '**').replace('</b>', '**') + "](" + res1['url'] + ")"
