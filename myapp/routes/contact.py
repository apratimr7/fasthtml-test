from fasthtml.common import *
from templates.base import base_template

def contact_route(rt):
  @rt("/contact")
  def get():
    content = Div("Welcome to the My Contact Page")
    return base_template(content)