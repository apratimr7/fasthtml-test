from fasthtml.common import *
from templates.base import base_template

def home_route(rt):
  @rt("/")
  def get():
    content = H1("Welcome to the Home Page")
    return base_template(content)