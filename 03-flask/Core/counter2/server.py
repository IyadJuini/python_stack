from flask import Flask , render_template, session, redirect, request

app = Flask (__name__)
app.secret_key = "gonfrks"


@app.route('/')
def index():
    session['visit_counter'] = session.get('visit_counter',0)
    return render_template("index.html", counter = session['visit_counter'])

@app.route('/destroy_session')
def destroy_session():
    # session['visit_counter']= 0
    session.clear()
    return redirect('/')

@app.route('/add1')
def button_click1():
    session['visit_counter'] = session.get('visit_counter')+1
    return redirect('/')

@app.route('/add2')
def button_click2():
    session['visit_counter'] = session.get('visit_counter')+2
    return redirect('/')

@app.route('/process', methods=["POST"])
def add():
    print("-"*20, request.form)
    session['visit_counter'] = session.get('visit_counter') + int(request.form['addNumber'])
    return redirect ('/')

if __name__ == '__main__' :
    app.run(debug=True, port=5005)