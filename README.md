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


#### Python interop

While not exactly recommeded, it's obviously possible.
[Here's that example rewritten in Python](https://github.com/pyos/dogeweb/blob/master/examples/simple.py).
