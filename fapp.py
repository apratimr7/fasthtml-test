from fasthtml.common import *
import pathlib as path

js = path.Path()
app, rt = fast_app(live=True)

head = Head(Title("My App"),Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/bulma@1.0.2/css/bulma.min.css"))

header = Header(
                Nav(
                    Div(
                        H1("Apratim Rastogi", Class="title is-3"),
                        Class="nav-brand"
                    ),
                    Div(
                        Ul(
                            Li(A("About", href="/about", Class="nav-link")),
                            Li(A("Projects", href="/projects", Class="nav-link")),
                            Li(A("Contact", href="/contact", Class="nav-link")),
                            Class="nav-links is-right"
                        ),
                        Class="nav-menu"
                    ),
                    Class="nav has-shadow"
                ),
                Class="hero-head"
            )

footer = Footer(
                P("Copyright 2023 Apratim Rastogi", Class="has-text-centered"),
                Class="footer"
            )

@rt("/")
def get():
    return Html(
        head,
        Body(header,
            Section(
                Div(
                    H1("Welcome to my portfolio", Class="title is-1"),
                    P("Click on the links above to navigate to different pages."),
                    Class="container"
                ),
                Class="hero-body"
            ),
            footer,
            Class="root",
        )
    )

@app.get("/about")
def about():
    return Html(
        head,
        Body(
            Header(
                Nav(
                    Div(
                        H1("Apratim Rastogi", Class="title is-3"),
                        Class="nav-brand"
                    ),
                    Div(
                        Ul(
                            Li(A("About", href="/about", Class="nav-link is-active")),
                            Li(A("Projects", href="/projects", Class="nav-link")),
                            Li(A("Contact", href="/contact", Class="nav-link")),
                            Class="nav-links is-right"
                        ),
                        Class="nav-menu"
                    ),
                    Class="nav has-shadow"
                ),
                Class="hero-head"
            ),
            Section(
                Div(
                    H1("About me", Class="title is-1"),
                    P("I'm a software developer with a passion for building innovative and scalable solutions."),
                    P("I have experience in a range of programming languages, including Python, JavaScript, and HTML/CSS."),
                    Class="container"
                ),
                Class="hero-body"
            ),
            Footer(
                P("Copyright 2023 Apratim Rastogi", Class="has-text-centered"),
                Class="footer"
            ),
            Class="root"
        )
    )

@app.get("/projects")
def projects():
    return Html(
        head,
        Body(
            Header(
                Nav(
                    Div(
                        H1("Apratim Rastogi", Class="title is-3"),
                        Class="nav-brand"
                    ),
                    Div(
                        Ul(
                            Li(A("About", href="/about", Class="nav-link")),
                            Li(A("Projects", href="/projects", Class="nav-link is-active")),
                            Li(A("Contact", href="/contact", Class="nav-link")),
                            Class="nav-links is-right"
                        ),
                        Class="nav-menu"
                    ),
                    Class="nav has-shadow"
                ),
                Class="hero-head"
            ),
            Section(
                Div(
                    H1("My Projects", Class="title is-1"),
                    P("Coming soon..."),
                    Class="container"
                ),
                Class="hero-body"
            ),
            Footer(
                P("Copyright 2023 Apratim Rastogi", Class="has-text-centered"),
                Class="footer"
            ),
            Class="root"
        )
    )

@app.get("/contact")
def contact():
    return Html(
        head,
        Body(
            Header(
                Nav(
                    Div(
                        H1("Apratim Rastogi", Class="title is-3"),
                        Class="nav-brand"
                    ),
                    Div(
                        Ul(
                            Li(A("About", href="/about", Class="nav-link")),
                            Li(A("Projects", href="/projects", Class="nav-link")),
                            Li(A("Contact", href="/contact", Class="nav-link is-active")),
                            Class="nav-links"
                        ),
                        Class="nav-menu"
                    ),
                    Class="nav has-shadow"
                ),
                Class="hero-head"
            ),

            Section(
                Div(
                    H1("Get in touch", Class="title is-1"),
                    P("Coming soon..."),
                    Class="container"
                ),
                Class="hero-body"
            ),
            Footer(
                P("Copyright 2023 Apratim Rastogi", Class="has-text-centered"),
                Class="footer"
            ),
            Class="root"
        )
    )

serve()