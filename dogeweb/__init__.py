import dg
from . import main, route, request, response, websocket

r       = route
app     = main.Server
abort   = response.ContextAware.abort
jsonify = response.jsonify
