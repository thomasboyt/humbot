from plugin import Plugin 
import requests

export_plugin = Plugin()
@export_plugin.command(["repo", "searchrepo"])
def search_repo(client, message, rest):
    r = requests.get("https://api.github.com/legacy/repos/search/%s" % rest)
    try:
        repo = r.json()['repositories'][0]
        url = "https://github.com/%s/%s" % (repo['owner'], repo['name'])
        result = "Found GitHub repository: [%s/%s](%s)" % (repo['owner'], repo['name'], url)
    except KeyError:
        result = "No repos found :("

    client.send_message({
        "type": "stream",
        "to": message['stream'],
        "subject": message['subject'],
        "content": "**BOT**: @**%s** %s" % (message['sender'], result)
    }) 
