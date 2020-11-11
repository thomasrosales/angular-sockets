from flask import Blueprint, request
from utils.requests import get_url_params
from flask_cors import CORS
from flask import jsonify


websocket = Blueprint(
    "websocket", __name__, template_folder="templates", static_folder="static"
)

CORS(websocket)


# Create your end-points here.


@websocket.route("healthcheck", methods=["GET"])
def test():
    return jsonify({"[WORKING]": "OK, 200"}), 200
