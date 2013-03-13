# yoinked from Skybot: https://raw.github.com/rmmh/skybot/master/plugins/pyexec.py
from plugin import Plugin
import requests

export_plugin = Plugin()
@export_plugin.command(["python", "py", "pyexec"])
def pyexec(client, message, rest):
    res = requests.get("http://eval.appspot.com/eval", params={'statement': rest}).text

    res = res.splitlines()
    if len(res) > 5:
        res = res[:5]
    res = "\n".join(res)
    res = "\n~~~\n%s\n~~~" % res
    return res
