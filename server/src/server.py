from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import FileResponse


def get_home(req):
  return FileResponse("index.html")

def get_product(req):
  return FileResponse("product.html")
    
def get_kvp(req):
  return FileResponse("KVP.html")

def get_UI(req):
  return FileResponse("UI.html")

def get_IA(req):
  return FileResponse("IA.html")

''' Route Configurations '''
if __name__ == '__main__':
  config = Configurator()

  config.add_route('get_home', '/')
  config.add_view(get_home, route_name='get_home')
  
  config.add_route('get_product', '/product')
  config.add_view(get_product, route_name='get_product')
  
  config.add_route('get_kvp', '/kvp')
  config.add_view(get_kvp, route_name='get_kvp')
  
  config.add_route('get_UI', '/UI')
  config.add_view(get_UI, route_name='get_UI')
  
  config.add_route('get_IA', '/IA')
  config.add_view(get_IA, route_name='get_IA')

  config.add_static_view(name='/', path='./public', cache_max_age=3600)

  app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 6000, app)
  server.serve_forever()