from datetime import datetime
from app import db

#modelos

class Cliente(db.Model):
    
    __tablename__ = "clientes"
    
    id = db.Column( db.Integer, primary_key = True)
    user = db.Column( db.String(100) , unique = True)
    email = db.Column( db.String(200) , unique = True)
    password =db.Column( db.String(200))
  
class Producto(db.Model):
    
    __tablename__ = "productos"

    id = db.Column( db.Integer , primary_key = True)
    nombre = db.Column( db.String(100) )
    precio = db.Column( db.Numeric (precision = 10, scale = 2))
    img =db.Column( db.String(200))

class Venta(db.Model):
    
    __tablename__ = "ventas"

    id = db.Column( db.Integer, primary_key = True)
    fecha = db.Column( db.DateTime, default = datetime.utcnow)
    id_cliente = db.Column (db.Integer, db.ForeignKey ('clientes.id'))

class Detalle(db.Model):
    
    __tablename__ = "detalles"

    id = db.Column( db.Integer, primary_key = True)
    cantidad = db.Column ( db.Integer)
    id_productofk = db.Column (db.Integer, db.ForeignKey ('productos.id'))
    id_ventafk = db.Column (db.Integer, db.ForeignKey ('ventas.id'))