## dogeweb

asyncio + anonymous functions + [the best language ever](https://pyos.github.io/dg/).

### Usage

```dg
import '/dogeweb'
import '/dogeweb/r'
import '/dogeweb/property'  # allows to use `~> @stuff` instead of `req -> req.stuff`


app = dogeweb.app $ r.path
  '/', ~> 'Hello, World!'
```

See [this example](https://github.com/pyos/dogeweb/blob/master/examples/simple.dg)
for something slightly more complex.


### Usage, decorator-style

```python
import dg
import dogeweb

root = dogeweb.r.path()

@root.route('/')
def hello(request):
    return 'Hello, World!'

app = dogeweb.app(root)
```

### Running in development

```dg
app.run '0.0.0.0' 8000  # dg
```

```python
app.run('0.0.0.0', 8000)  # python
```

### Running in production

```sh
gunicorn -k dogeweb.gunicorn.Worker helloworld:app
```

### TCP/2.0 support.

Er...I mean "WebSockets over HTTP over WebSockets over TLS over TCP".
Wait, no, was it SPDY?.. Nah, HTTP/2.0. Anyway, [h2py](https://github.com/pyos/h2py)
is required for this to work.

```python
import aiouv
# HTTP/2.0 is only supported over libuv event loops.
loop = aiouv.EventLoop()

app.run('0.0.0.0', 8000, loop=loop, http2=True)
```
