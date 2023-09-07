from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, NumberRange

class UserForm():
    user = StringField('Ingrese Nombre de Usuario:', validators=[InputRequired(message='nombre requerido')])
    email = StringField('Ingrese Email:', validators=[InputRequired(message='email requerido')])
    password = StringField('Ingrese Password:', validators=[InputRequired(message='password requerida')])

class NewClientForm(FlaskForm, UserForm):
    user = StringField('Ingrese Nombre de Usuario:', validators=[InputRequired(message='nombre requerido')])
    email = StringField('Ingrese Email:', validators=[InputRequired(message='email requerido')])
    password = StringField('Ingrese Password:', validators=[InputRequired(message='password requerida')])
    submit = SubmitField('Registrar')

class EditUserForm(FlaskForm, UserForm):
    submit = SubmitField('Registrar')