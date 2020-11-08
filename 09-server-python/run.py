from app import create_app
from flask_socketio import SocketIO
import os

env = os.environ.get("FLASK_ENV", "development")
app = create_app(env)

socket_io = SocketIO()

# SOCKET IO
socket_io.init_app(app, cors_allowed_origins="*")


socket_io.run(app)