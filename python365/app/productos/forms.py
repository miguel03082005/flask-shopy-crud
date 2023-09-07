from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired, NumberRange

class ProductForm():
    nombre = StringField('Ingrese Producto:', validators=[InputRequired(message='nombre requerido')])
    precio = IntegerField('Ingrese Precio:', validators=[InputRequired(message='precio requerido'), NumberRange(message='precio fuera de rango', min= 50, max=1000000)])

class NewProducForm(FlaskForm, ProductForm):
    nombre = StringField('Ingrese Producto:', validators=[InputRequired(message='nombre requerido')])
    precio = IntegerField('Ingrese Precio:', validators=[InputRequired(message='precio requerido'), NumberRange(message='precio fuera de rango', min= 50, max=1000000)])
    img = FileField('Ingrese Imagen del Producto:', validators=[FileRequired(message='ingrese un archivo'), FileAllowed(['jpg', 'png', 'jpeg'], message='solo se admiten imagenes')])
    
class EditProductForm(FlaskForm, ProductForm):
    submit = SubmitField('Registrar')