from app import create_app
import os

env = os.environ.get("FLASK_ENV", "development")
app = create_app(env)

from websocketio import init_socket

init_socket(app).run(app)