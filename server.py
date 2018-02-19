from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 1
    #session['counter'] += 1
    return render_template('index.html', counter = session['counter'])
    
@app.route('/reload', methods=['POST'])
def reload():

    session['counter'] += 2
    return redirect("/")

@app.route('/reset', methods=['POST'])
def reset():
    session['counter'] = 0
    return redirect ('/')

app.run(debug = True)