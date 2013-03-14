# Humbot

An IRC bot, but for [Humbug](http://humbughq.com). Made at [Hacker School](http://hackerschool.com).

## Installing and Use

Right now, Humbug doesn't have a read API, which makes this a little more complicated than an IRC bot would be. Right now, Humbot itself doesn't read the chat, but relies on an external scraper such as [Humbug Spy](https://github.com/thomasboyt/humbug-spy). 

If you'd like to develop your own scraper (that doesn't, say, require your browser to be open 24/7!), you can do so by scraping however you like and then POSTing a JSON string to Humbot's `/receiver/` endpoint in this format:

```json
{
  "sender": "sender's username",
  "stream": "current stream",
  "subject": "current subject",
  "message": "current message"
}
```

Anyways, once you have whatever scraper you'd like set up, installing the dependencies is easy enough:

```
pip install -r requirements.txt
pip install -e git://github.com/humbughq/python-humbug.git#egg=humbug
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
