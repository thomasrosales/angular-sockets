from flask_socketio import SocketIO, emit, disconnect, Namespace

socket_io = SocketIO()


class MessageNameSpace(Namespace):
    def on_connect(self):
        print("[ CONNECTED ]")

    def on_disconnect(self):
        print("[ DISCONNECTED ]")
        disconnect()

    def on_message(self, payload, callback):
        print(f"[ EVENT ]: {payload} {callback} ")
        # emit("my response", {"data": "Connected"})


socket_io.on_namespace(MessageNameSpace("/test"))

# @socket_io.on("connect")
# def test_connect():
#     emit("my response", {"data": "Connected"})


# @socket_io.on("disconnect")
# def test_disconnect():
#     print("Client disconnected")
#     disconnect()


def init_socket(app):
    # SOCKET IO
    socket_io.init_app(app, cors_allowed_origins="*")
    return socket_io
