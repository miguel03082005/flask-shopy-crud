from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from flask_bootstrap import Bootstrap


#blueprint

from .mi_blueprint import mi_blueprint
from app.productos import productos_blueprint
from app.usuarios import usuarios_blueprint

#creacion y configuracion de la app

app = Flask(__name__)
app.config.from_object(Config)
b = Bootstrap(app)

#registro de blueprints

app.register_blueprint(mi_blueprint)
app.register_blueprint(productos_blueprint)
app.register_blueprint(usuarios_blueprint)

#crear objetos de SQLAlchemy y migrate

db = SQLAlchemy(app)
migrate = Migrate(app , db)

from .models import Producto, Cliente, Venta, Detalle

@app.route('/KIRITO')
def KIRITO():
    return render_template('KIRITO.html')
