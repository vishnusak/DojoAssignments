from flask import Flask, redirect, request, session, render_template
import random

app = Flask(__name__)
# using a random string as the secret_key. No idea where this is used but I am guessing the server uses this in some way to generate the session ids
app.secret_key = "sdkfj4328dj732rywe98casaoufdsa8s"

@app.route('/')
def main():
    if 'number' not in session:
        # generate random number between 1 and 100
        session['number']= random.randrange(0, 100) + 1
        session['msg']   = ''
        session['m_id']  = ''
        session['form1'] = 'show'
        session['form2'] = 'hide'
        session['attempts'] = []

    return render_template('number.html', message=session['msg'], m_id=session['m_id'], form1=session['form1'], form2=session['form2'], guesses=session['attempts'])

@app.route('/check', methods=['POST'])
def check():
    guess = request.form['guess']
    if len(guess) == 0:
        guess = 0

    if (abs(int(guess) - session['number']) == 0):
        session['msg']   = "You hit it on the head. CONGRATULATIONS!!!"
        session['m_id']  = 'success'
        session['form1'] = 'hide'
        session['form2'] = 'show'
    elif (abs(int(guess) - session['number']) <= 2):
        session['msg']  = "Oooh!! Close ... but no cigar!!"
        session['m_id'] = 'hot'
    elif (abs(int(guess) - session['number']) <= 15):
        session['msg']  = "Yes! You are getting close now"
        session['m_id'] = 'close'
    else:
        session['msg']  = "Nope! Keep trying!!"
        session['m_id'] = 'nope'

    session['attempts'].append((session['m_id'],guess))

    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.pop('number')
    return redirect('/')

app.run(debug=True)
