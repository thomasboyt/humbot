class Plugin:
    def __init__(self):
        self.commands = {}
        self.regexes = {}

    def command(self, commands):
        def decorator(fn):
            for cmd in commands:
                self.commands[cmd] = fn
            return fn
        return decorator
    
class PluginsController:
    def __init__(self):
        self.plugins = []
        self.commands = {}
        self.regexes = {}

    def append(self, plugin):
        self.plugins.append(plugin)
        self.commands.update(plugin.commands)

#@plugin.regex(...)
#def url_preview(message, match):
