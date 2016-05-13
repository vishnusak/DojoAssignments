from flask import Flask, render_template, redirect, request, session
import random as rd
import time as tm

app = Flask(__name__)
app.secret_key = "43987541uhjd98qh9438udj9832qure329j2d983"

@app.route('/')
def main():
    if 'gold' not in session:
        session['gold'] = 0
        session['activity'] = []

    return render_template('ninja.html', gold=session['gold'], activity_list=reversed(session['activity']))

@app.route('/process_money', methods=['POST'])
def process():
    if request.form['building'] == 'reset':
        session.pop('gold')
        return redirect('/')
    elif request.form['building'] == 'farm':
        earn = rd.randrange(9, 20) + 1
        activity = 'Earned {} golds from the farm!'.format(earn)
        color = 'green'
    elif request.form['building'] == 'cave':
        earn = rd.randrange(4, 10) + 1
        activity = 'Earned {} golds from the cave!'.format(earn)
        color = 'green'
    elif request.form['building'] == 'house':
        earn = rd.randrange(1, 5) + 1
        activity = 'Earned {} golds from the house!'.format(earn)
        color = 'green'
    elif request.form['building'] == 'casino':
        earn = rd.randrange(-51, 50) + 1
        if earn > 0:
            activity = 'Entered a casino and earned {} golds... Yay..'.format(earn)
            color = 'green'
        elif earn < 0:
            activity = 'Entered a casino and lost {} golds... Ouch..'.format(earn)
            color = 'red'
        else:
            activity = 'Entered a casino and came out without losing anything... Phew..'
            color = 'black'

    act = tm.localtime()
    hr = (act.tm_hour if (act.tm_hour < 12) else (act.tm_hour - 12))
    ap = ('PM' if (act.tm_hour/12) else 'AM')

    time = '({}/{}/{} {}:{} {})'.format(act.tm_year, act.tm_mon, act.tm_mday, hr, act.tm_min, ap)

    session['gold'] += earn

    session['activity'].append((activity, time, color))

    return redirect('/')

app.debug = True
app.run()
