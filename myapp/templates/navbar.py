from fasthtml.common import *

def Navbar():
    return Nav(
        Div( A("My 3D Portfolio", href="/"), Class="nav-brand"),
        Div(
            Ul(
            Li(A("Home", href="/")),
            Li(A("About", href="/about")),
            Li(A("Projects", href="/projects")),
            Class="nav-links",
            ),Class="nav"
          ),
    )