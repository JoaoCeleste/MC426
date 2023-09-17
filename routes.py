from database import db
from models import User
from flask import Blueprint

routes = Blueprint('routes', __name__)

@routes.route('/')
def main():
    return '<h1>Hello World!</h2>'