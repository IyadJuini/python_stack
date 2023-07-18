from flask import Flask , render_template, request, redirect, session

app  = Flask(__name__)
app.secret_key = "porcco"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['username']  = request.form['username']
    session['location']  = request.form['location']
    session['language']  = request.form['language']
    session['comments']  = request.form['comments']
    session['sex'] = request.form['sex']
    session['accept'] = request.form['accept']
    if session['accept'] == "on":
        session['accept'] = "you agree."
    else :
        session['accept'] = "You don't agree"  
        
    print(f"{session['username']} {session['location']} {session['language']} {session['comments']} ")
    return redirect("/display")

@app.route('/display')
def display():
    return render_template("display.html")

if __name__ =='__main__':
    app.run(debug = True, port=5000)

