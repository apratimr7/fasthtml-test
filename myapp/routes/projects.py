from fasthtml.common import *
from templates.base import base_template

def projects_route(rt):
  @rt("/projects")
  def get():
    content = Div("Welcome to the Projects Page")
    return base_template(content)