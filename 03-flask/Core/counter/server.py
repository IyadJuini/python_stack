from flask import Flask , render_template, session, redirect

app = Flask(__name__)
app.secret_key = "jajano"


@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 1 
    return render_template('index.html')

@app.route('/count', methods=['POST'])
def count():
    session['counter'] = session['counter'] +1
    return render_template('index.html')

@app.route('/destroy')
def destroy():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug = True , port = 5006)
