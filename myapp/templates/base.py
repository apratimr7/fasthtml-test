from fasthtml.common import *
from templates.navbar import Navbar
# from templates import footer

# add all the custom scripts here
script = Script("""
{
    "imports": {
       "three": 
    "https://cdn.jsdelivr.net/npm/three@0.167.1/build/three.module.js",
      "three/addons/": 
    "https://cdn.jsdelivr.net/npm/three@0.167.1/examples/jsm/"
            }
}""" , type="importmap")

head = Head(
            Meta(charset="UTF-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            Link(rel="stylesheet", href="static/styles.css"),
            Title("My App"),script
            )

def base_template(content):
    # Add a script to create the 3D animation
    animation_script = Script(type="module", src = "static/js/stars.js")
    
    return Html(
        head,
        Body(
            Navbar(),  # Include navbar
            Div(content, id="main-content"),
            Canvas(animation_script,id="background-canvas"),
            # Footer()  # Include footer
        )
    )