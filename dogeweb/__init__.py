import dg

from . import main, route, request, response, websocket


app      = main.Server
abort    = response.abort
redirect = response.redirect
static   = response.static
jsonify  = response.jsonify
r        = route


def property(get, set_=None, del_=None, doc=None):
    '''A replacement for `property` that does not, in fact, create a `property`.

        So `~> @x` becomes simply `self -> self.x`.

    '''
    def _property_error(_):
        assert False, 'cannot use this; `property` overriden by dogeweb'

    if set_ or del_ or doc:
        _property_error(None)

    try:
        get.setter  = _property_error
        get.deleter = _property_error
    except AttributeError:
        pass

    return get
