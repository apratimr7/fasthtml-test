from fasthtml.common import *
from templates.base import base_template

def about_route(rt):
  @rt("/about")
  def get():
    content = Div("Welcome to the about Page")
    return base_template(content)