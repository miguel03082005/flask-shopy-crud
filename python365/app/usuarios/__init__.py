from flask import Blueprint

usuarios_blueprint = Blueprint('usuarios', __name__, url_prefix = '/usuarios', template_folder = 'templates')

from . import routes