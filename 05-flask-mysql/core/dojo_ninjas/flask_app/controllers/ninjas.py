from flask import  render_template, redirect, request 
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas/create')
def ninja_dashboard():
    all_dojos = Dojo.get_all()
    
    return render_template('create_ninjas.html', dojos=all_dojos)

# @app.route('/dojo/create')
# def new_user():
#     return render_template('create.html')

@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    Ninja.create_ninja(request.form)
    return redirect('/')

# @app.route('/users/view/<int:user_id>')
# def view_user(user_id):
#     data_dict = {'id':user_id}
#     the_user = Dojo.get_by_id(data_dict)
#     return render_template('view.html',user = the_user)
    

# @app.route('/users/<int:user_id>/delete')
# def delete(user_id):
#     data_dict = {'id':user_id}
#     Dojo.delete(data_dict)
#     return redirect('/users')

# @app.route('/users/<int:user_id>/update')
# def update(user_id):
#     Dojo.update({'id':user_id})
#     return redirect('/users')

# @app.route('/users/<int:user_id>/edit')
# def edit_user(user_id):
#     dojo = Dojo.get_by_id({'id':user_id})
#     return render_template('edit.html',user=dojo)

# @app.route('/users/<int:user_id>/update', methods=['POST'])
# def update_user(user_id):
#     data_dict = {**request.form}
#     data_dict['id'] = user_id
#     Dojo.update_user(data_dict)
#     return redirect('/')
    
    
