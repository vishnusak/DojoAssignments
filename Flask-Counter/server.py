from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

# still to figure out why we need the secret_key for using sessions
app.secret_key = "ajsfduqwm cxoi324y8wqudmcxas x"

@app.route('/')
def main():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template('counter.html', counter=session['count'])

@app.route('/by2')
def up_the_count():
    session['count'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session['count'] = 0
    return redirect('/')

app.debug = True
app.run()
