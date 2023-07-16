from flask import Flask

app = Flask(__name__)

#  http://127.0.0.1:5000


@app.route('/')
def index():
    return "Hello From Flask"

@app.route('/hi')
def hi():
    return "<h1>Hi 🧛‍♀️🧛‍♀️🧛‍♀️</h1>"



@app.route('/hi/<username>')
def hi_user(username):
    return f"<h1>Hi {username}🧛‍♀️🧛‍♀️🧛‍♀️</h1>"



@app.route('/info/<username>/<int:age>')
def user_info(username,age):
    return f""

if __name__ == '__main__':
    app.run()