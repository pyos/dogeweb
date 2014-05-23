import asyncio

import dg
import dogeweb

from dogeweb import r


def _sleep_handler(req):
    yield from asyncio.sleep(5)
    return 200, 'Done sleeping.\n'


app = dogeweb.app(r.dir(
  ('/request/', r.file(
    ('/method/',   lambda req: '{}\n'.format(req.method)),
    ('/path/',     lambda req: '{}\n'.format(req.path)),
    ('/payload/', r.method(
      ('GET',  lambda req: 'POST something here.\n'),
      ('POST', lambda req: '{}\n'.format(req.payload)))),
    ('/attr/<str:name>/', lambda req, name: '{}\n'.format(getattr(req, name, None))))),
  ('/static/', lambda req: req.static(req.path.lstrip('/'))),

  ('/route/', 'test_route', r.file(
    ('/parent/',   'parent',    lambda req: '{}\n'.format(req.parent)),
    ('/redirect/', 'redirect',  lambda req: req.redirect(req.url_for('.parent'))),
    ('/<int:id>/', 'something', lambda req, id: 'Got item #{}.\n'.format(id)),
    ('/first/',    'to_id_1',   lambda req: req.redirect(req.url_for('.something', id=1))))),

  ('/', r.file(
    ('/',             lambda req: somepage),
    ('/favicon.ico',  lambda req: req.redirect('/static/favicon.ico')),
    ('/async/sleep/', _sleep_handler)))))


app.run('0.0.0.0', 8000)
