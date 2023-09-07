from flask import Blueprint

#crear y confugura el blueprint

mi_blueprint = Blueprint('mi_blueprint', __name__, url_prefix = '/ejemplo')

#crear ruta de blueprint
@mi_blueprint.route('/saludo')
def saludo():
    return 'balle esa radio'