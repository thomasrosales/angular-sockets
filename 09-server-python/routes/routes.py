from flask import Blueprint, request
from utils.requests import get_url_params
from flask_cors import CORS


websocket = Blueprint(
    "websocket", __name__, template_folder="templates", static_folder="static"
)

CORS(websocket)


# Create your end-points here.


@websocket.route("/", methods=["POST"])
def test():
    pass
