from fasthtml.common import *
import pathlib as path
# import json as

js = path.Path()
app, rt = fast_app(live=True)

@rt("/")
def get():
    return Html(
        Head(
            Title("My App"),
            Link(rel="stylesheet", href="styles.css"),
            Link(rel="stylesheet", href='https://fonts.googleapis.com/css?family=Poppins')
            ),
        Body(H1("Apratim Rastogi"),
            Div('Some Text', A('A test link',href="/test"))
        )
    )

@rt("/test")
def get():
    return Html(
        Head(Title("My App"),Link(rel="stylesheet", href="styles.css")),
        Body(H1("Apratim Rastogi"),
            Div('Some Text', A('Succesfull link',href="/")),
            Div("You can visit a different page"),A("Here",href="/diftest")
        )
    )

@app.get("/diftest")
def test():
    # Add a Three.js script tag
    script = Script("""
{
    "imports": {
       "three": 
    "https://cdn.jsdelivr.net/npm/three@0.167.1/build/three.module.js",
      "three/addons/": 
    "https://cdn.jsdelivr.net/npm/three@0.167.1/examples/jsm/"
            }
}""" , type="importmap")

    # Add a script to create the 3D animation
    animation_script = Script(type="module", src = "js/wormhole.js")

    # Add a canvas element to render the 3D animation
    canvas = Canvas(id="background-canvas")

    # Create a header with navigation menu
    header = Header(
        Div(
            H2("Apratim Rastogi", Class="title"),
            Class="title-container"
        ),
        Nav(
            Ul(
                Li(A("About", href="#about")),
                Li(A("Projects", href="#projects")),
                Li(A("Contact", href="#contact")),
                Class="nav-links"
            ),
            Class="nav"
        ),
        Class="header"
    )

    # Return the HTML response
    return Html(
        Head(
            Meta(charset="UTF-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            Link(rel="stylesheet", href="styles.css"),
            Title("My App"),script
            ),

        Body(header,canvas,
            Div(
                H1("Welcome to my portfolio"),
                Class="hero"
            ),
            Div(
                H2("About me"),
                P("I'm a software developer with a passion for building innovative and scalable solutions."),
                P("I have experience in a range of programming languages, including Python, JavaScript, and HTML/CSS."),
                Class="about",
            ),
             animation_script, 
            Class="root"
            )
    )

serve()