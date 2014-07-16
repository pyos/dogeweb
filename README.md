## dogeweb

asyncio + anonymous functions + [the best language ever](https://pyos.github.io/dg/).

### Usage

```dg
import '/dogeweb'
import '/dogeweb/r'


app = dogeweb.app $ r.file
  '/', ~> 'Hello, World!'
```

See [this example](https://github.com/pyos/dogeweb/blob/master/examples/simple.dg)
for something slightly more complex.


### Usage, decorator-style

```python
import dg
import dogeweb

root = dogeweb.r.file()

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
