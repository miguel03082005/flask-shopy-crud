from . import usuarios_blueprint
from flask import render_template, redirect, flash
from .forms import NewClientForm, EditUserForm
import app
import os

#crear las rutas del blueprint

@usuarios_blueprint.route('/crear', methods = ['GET', 'POST'])
def crear():
    c = app.models.Cliente()
    form = NewClientForm()
    if form.validate_on_submit():

        #el formulario va a llenar automaticamente

        form.populate_obj(c)
        app.db.session.add(c)
        app.db.session.commit()

        return redirect('/usuarios/listar_clientes.html')
    return render_template('new.html', form = form)

@usuarios_blueprint.route('/listar')
def listar():
    #tarer los productos de la base

    clientes = app.Cliente.query.all()
    #return clientes
    #mostrar la lista enviandole los productos

    return render_template ('listar_clientes.html', clientes = clientes)

@usuarios_blueprint.route('/edit/<user_id>', methods = ['GET', 'POST'])
def edit(user_id):

    #leseccionar el producto con el id

    u = app.models.Cliente.query.get(user_id)

    #crago el formulario con los atributos del producto

    form_edit = EditUserForm(obj = u)

    if form_edit.validate_on_submit():
        form_edit.populate_obj(u)
        app.db.session.commit()
        flash ('Ususario Editado Exitosamente')
        return redirect('/usuarios/listar')
    
    return render_template('new.html', form = form_edit)
    
@usuarios_blueprint.route('/delete/<user_id>', methods = ['GET', 'POST'])
def delete(user_id):

    #seleccionar el producto a eliminar
    
    u = app.models.Cliente.query.get(user_id)

    #eliminar el producto

    app.db.session.delete(u)
    app.db.session.commit()

    flash('Ususario Eliminado Exitosamente')

    return redirect('/usuarios/listar')