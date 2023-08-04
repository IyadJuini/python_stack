from flask import  render_template, redirect, request 
from flask_app import app
from flask_app.models.user_model import User
from datetime import datetime

@app.route('/')
def redirect_to_user():
    return redirect('/users')

@app.route('/users')
def dashboard():
    all_users = User.get_all()
    return render_template('users.html', users=all_users)

@app.route('/users/new')
def new_user():
    return render_template('create.html')

@app.route('/users/create', methods=['POST'])
def create_user():
    data_dict = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    user_id = User.create_user(data_dict)
    get_user = User.get_by_id(data_dict={'id':user_id})
    return render_template('view.html',user=get_user)

@app.route('/users/view/<int:user_id>')
def view_user(user_id):
    data_dict = {'id':user_id}
    the_user = User.get_by_id(data_dict)
    return render_template('view.html',user = the_user)
    

@app.route('/users/<int:user_id>/delete')
def delete(user_id):
    data_dict = {'id':user_id}
    User.delete(data_dict)
    return redirect('/users')

@app.route('/users/<int:user_id>/update')
def update(user_id):
    User.update({'id':user_id})
    return redirect('/users')

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    user = User.get_by_id({'id':user_id})
    return render_template('edit.html',user=user)

@app.route('/users/<int:user_id>/update', methods=['POST'])
def update_user(user_id):
    data_dict = {**request.form}
    data_dict['id'] = user_id
    User.update_user(data_dict)
    return redirect('/')
    
    
