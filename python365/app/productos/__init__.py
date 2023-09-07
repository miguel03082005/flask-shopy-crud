from flask import Blueprint

productos_blueprint = Blueprint('productos', __name__, url_prefix = '/productos', template_folder = 'templates', static_folder='imagenes')

from . import routes