from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/recipes/new')
def new_party():
    if not 'user_id' in session:
        return redirect('/')
    return render_template('new_recipe.html')

@app.route('/recipes/create', methods = ['POST'])
def add_recipe():
    print(request.form)
    if Recipe.validate(request.form):
        data = {
            **request.form,
            'user_id' : session['user_id']
        }
        Recipe.create(data)
        return redirect('/dashboard')
    return redirect('/recipes/new')


@app.route('/recipes/<int:recipe_id>/edit')
def edit_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect('/')
    recipe = Recipe.get_by_id({'id':recipe_id})
    return render_template('edit_recipe.html', recipe = recipe)

@app.route('/recipes/<int:recipe_id>/update', methods = ['POST'])
def update_recipe(recipe_id):
    if Recipe.validate(request.form):
        data = {
            **request.form,
            'id':recipe_id
        }
        Recipe.update(data)
        return redirect('/dashboard')
    return redirect(f'/recipes/{recipe_id}/edit')

@app.route('/recipes/<int:recipe_id>')
def show_one(recipe_id):
    if 'user_id' not in session:
        return redirect('/')
    logged_user = User.get_by_id({'id':session['user_id']})
    recipe = Recipe.get_by_id({'id':recipe_id})
    return render_template("one_recipe.html", recipe = recipe,user = logged_user)

@app.route('/my_recipes')
def my_recipes():
    if 'user_id' not in session:
        return redirect('/')
    user = User.get_by_id({'id':session['user_id']})
    recipes = Recipe.get_user_recipes({'user_id':session['user_id']})
    return render_template('my_recipes.html', user = user, recipes = recipes)

@app.route('/recipes/<int:recipe_id>/destroy', methods = ['POST'])
def cancel(recipe_id):
    Recipe.delete({'id':recipe_id})
    return redirect('/dashboard')