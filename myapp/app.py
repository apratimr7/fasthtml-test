from fasthtml.common import *
from routes import register_routes

app, rt = fast_app()

register_routes(rt)

serve()