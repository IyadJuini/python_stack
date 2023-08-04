from flask import  render_template, redirect, request, session,flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def dashboard():    
    return render_template('index.html')

@app.route('/dashboard')
def redirection():
    if 'user_id' not in session:
        return redirect('/')
    logged_user = User.get_by_id({'id':session['user_id']})
    return render_template("dashboard.html", user= logged_user)

@app.route('/users/create', methods=['POST'])
def create():
    if User.validation_registration(request.form):
        pw_hashed = bcrypt.generate_password_hash(request.form['password'])
        data_dict = {**request.form,
                'password':pw_hashed}
        user_id = User.create(data_dict)
        session['user_id']=user_id
        return redirect('/dashboard')
    return redirect('/')

@app.route('/login', methods =['POST'])
def login():
    user_from_db = User.get_by_email({'email':request.form['email']})
    if user_from_db:
        if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
            # if we get False after checking the password
            flash("Wrong Password !!!","login")
            return redirect('/')
        session['user_id'] = user_from_db.id
        return redirect('/dashboard')
    flash("Wrong email !!!!","login")
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')