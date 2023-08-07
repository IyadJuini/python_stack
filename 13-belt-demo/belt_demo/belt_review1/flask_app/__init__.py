from flask import Flask

# ! CHANGE DATABASE NAME
DATABASE = 'belt_demo_db'

app  = Flask(__name__)
app.secret_key = "shhhhhhhhhhhhhhh"