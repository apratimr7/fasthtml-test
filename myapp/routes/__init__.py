from routes.about import *
from routes.contact import *
from routes.home import *
from routes.projects import *

def register_routes(rt):
  home_route(rt)
  about_route(rt)
  contact_route(rt)
  projects_route(rt)