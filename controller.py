import importlib, os

class PluginsController:
    def __init__(self):
        self.plugins = []
        self.commands = {}
        self.regexes = {}

        # open plugins folder, get the plugins
        plugin_files = [item.rsplit(".", 1)[0] for item in os.listdir("plugins") if item.endswith(".py")]
        for name in plugin_files:
            try:
                plugin = importlib.import_module("plugins." + name).export_plugin
                self.append(plugin)
            except AttributeError:
                pass

    def append(self, plugin):
        self.plugins.append(plugin)
        self.commands.update(plugin.commands)
