from flask import Blueprint, render_template, redirect, request, url_for
from app import db
from app.models import Post
from app.models import Category

categories_bp = Blueprint('categories', __name__)

#Listar las categorias
@categories_bp.route('/')
def listar_categories():
    categories = Category.query.all()
    return render_template('categories/listar_categories.html', categories=categories)

#Crear las categorias
@categories_bp.route('/new', methods=['GET','POST'])
def add_category():
    if request.method == 'POST':
        name = request.form['name']
        new_category = Category(name=name)
        db.session.add(new_category)
        db.session.commit()
        return redirect(url_for('categories.listar_categories'))
    #Aqui si es GET
    return render_template('categories/create_category.html')

@categories_bp.route('/update/<int:id>', methods=['GET','POST'])
def update_category(id):
    category = Category.query.get(id)
    if request.method == 'POST':
        category.name = request.form['name']
        db.session.commit()
        return redirect(url_for('categories.listar_categories'))
    #Aqui si es GET
    return render_template('categories/update_category.html', category=category)

@categories_bp.route('/delete/<int:id>')
def delete_category(id):
    category = Category.query.get(id)
    if category:
        db.session.delete(category)
        db.session.commit()
    return redirect(url_for('categories.listar_categories'))