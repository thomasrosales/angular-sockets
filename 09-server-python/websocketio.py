from flask_socketio import SocketIO, emit, disconnect

socket_io = SocketIO()


@socket_io.on("connect")
def test_connect():
    emit("my response", {"data": "Connected"})


@socket_io.on("disconnect")
def test_disconnect():
    print("Client disconnected")
    disconnect()


def init_socket(app):
    # SOCKET IO
    socket_io.init_app(app, cors_allowed_origins="*")
    return socket_io
