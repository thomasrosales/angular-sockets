from flask_socketio import socketio
from app import create_app
import eventlet


sio = socketio.Server(async_mode="eventlet")
app = create_app("production")
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

if __name__ == "__main__":
    eventlet.wsgi.server(eventlet.listen(("", 8000)), app)
    # app.run(threaded=True)