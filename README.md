# Humbot

An IRC bot, but for [Humbug](http://humbughq.com). Made at [Hacker School](http://hackerschool.com).

## Installing and Use

Installing the dependencies is easy enough:

```
pip install -r requirements.txt
pip install https://humbughq.com/dist/api/python-humbug_0.1.4~hackerschool.tar.gz
```

Write a `config.py` file based on `config.sample.py` and launch the server with `python server.py`. Assuming your scraper is sending valid messages, it should start working immediately!

## Plugin Development

This is the fun part. Developing plugins is really easy! 

To start, `from plugin import Plugin`, make a new object of class `Plugin` called `export_plugin`.

### Adding Commands

```python
@export_plugin.command(['google', 'search'])
def google(client, message, rest):
    # implement a google search here
    return result
```

The list passed to the command decorator are commands that both call the `google` function. If your function returns a string, that string will be output in Humbug on the same subject and stream in this format:

```
**BOT**: @<sender name> <result>
```

If you'd like to send a different kind of message (such as a private message or a message to another stream), return `None` and instead use the `client` object that is passed as the first argument to all commands. See [the Humbug API docs](https://github.com/humbughq/python-humbug#using-the-api) for usage of that (it's not very complicated).

The other two arguments are `message`, which is a dict that contains the `sender`, `stream`, `subject`, and `content`, while `rest` is simply the "argument" to the command.

### Adding Regexes

*(soon)*

## Contributing

Whether you want to modify the core or add a plugin, please feel free to make a pull request! I'd love to see what you can come up with :)
