from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

# =============== INDEX PAGE ====================
@app.route('/')
def index():
    return render_template("index.html")


# ====================== DASHBOARD ====================
@app.route('/dashboard')
def dashboard():
    if not 'user_id' in session:
        return redirect('/')
    logged_user = User.get_by_id({'id':session['user_id']})
    recipes = Recipe.get_all()
    return render_template("dashboard.html", user = logged_user, recipes = recipes)

#  =========== REGISTER ====================
@app.route('/users/create', methods=['POST'])
def register():
    # 1 - Get the form data from the front-end
    print(request.form)
    # 2 - validate the form data
        # - if ddata is valid
    if User.validate(request.form):
        # Secure password - hash the password using bcrypt
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data = {
            **request.form,
            'password': pw_hash
        }
        # create the new user
        user_id = User.create(data)
        session['user_id'] = user_id
        return redirect('/dashboard')
    # - if data not valid
    return redirect('/')
        
# =======================login ======================
@app.route('/login',methods = ['POST'])
def login():
    # 1- Get user by email
    user = User.get_by_email({'email':request.form['email']})
    # if user does not exist : redirect to index and display errors
    if not user : 
        flash("invalid email/password", "login")
        return redirect('/')
    # if user exists: check password
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("invalid email/password", "login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')

#  ========== LOGOUT ===============================
@app.route('/logout', methods=['post'])
def logout():
    session.clear()
    return redirect('/')

        
