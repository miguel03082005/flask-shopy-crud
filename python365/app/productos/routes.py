from . import productos_blueprint
from flask import render_template, redirect, flash
from .forms import NewProducForm, EditProductForm
import app
import os

#crear las rutas del blueprint

@productos_blueprint.route('/crear', methods = ['GET', 'POST'])
def crear():
    p = app.models.Producto()
    form = NewProducForm()
    if form.validate_on_submit():
        #el formulario va a llenar automaticamente

        form.populate_obj(p)
        p.img = form.img.data.filename
        app.db.session.add(p)
        app.db.session.commit()

        #ubicar el archivo imagen en la carpeta app/productos/imagenes

        file = form.img.data
        file.save(os.path.abspath(os.getcwd() + '/app/productos/imagenes/' + p.img))

        flash('Producto Registrado Exitosamente')
        return redirect('/productos/listar')
    return render_template('new.html', form = form)

@productos_blueprint.route('/listar')
def listar():
    #tarer los productos de la base

    productos = app.Producto.query.all()

    #mostrar la lista enviandole los productos

    return render_template ('listar.html', productos = productos)

@productos_blueprint.route('/edit/<producto_id>', methods = ['GET', 'POST'])
def edit(producto_id):

    #leseccionar el producto con el id

    p = app.models.Producto.query.get(producto_id)

    #crago el formulario con los atributos del producto

    form_edit = EditProductForm(obj = p)

    if form_edit.validate_on_submit():
        form_edit.populate_obj(p)
        app.db.session.commit()
        flash ('Producto Editado Exitosamente')
        return redirect('/productos/listar')
    
    return render_template('new.html', form = form_edit)
    
@productos_blueprint.route('/delete/<producto_id>', methods = ['GET', 'POST'])
def delete(producto_id):

    #seleccionar el producto a eliminar
    
    p = app.models.Producto.query.get(producto_id)

    #eliminar el producto

    app.db.session.delete(p)
    app.db.session.commit()

    flash('Producto Eliminado Exitosamente')

    return redirect('/productos/listar')