from flask import Blueprint
from src.database.data import getDataBase


main = Blueprint("route_origin",__name__)

@main.route("/")
def init():
    return getDataBase()


