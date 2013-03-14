from plugin import Plugin
import requests
import re
import urllib

export_plugin = Plugin()
@export_plugin.command(["weather"])
def google(client, message, rest):
    woeid = 12761346
    url = "http://weather.yahooapis.com/forecastrss?" + urllib.urlencode({'w': woeid})
    source = requests.get(url).text
    m = re.search("<b>Current Conditions:</b><br />\n([^<]+)<BR />", source, re.I)
    return m.groups()[0]
