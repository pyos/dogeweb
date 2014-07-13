import dg
from . import main, route, request, response, websocket
from . import route as r
from .main import Server as app
from .response import abort, redirect, static, jsonify


def property(get, set_=None, del_=None, doc=None):
    def _property_error(_):
        raise AssertionError('cannot use this; `property` overriden by dogeweb')
    if set_ or del_ or doc:
        _property_error(None)
    try:
        get.setter  = _property_error
        get.deleter = _property_error
    except AttributeError:
        pass
    return get
