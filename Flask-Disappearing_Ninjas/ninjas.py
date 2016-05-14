from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "ds9832ur9843jj8394q9djjx983u"

@app.route('/')
def main():
    if 'display' not in session:
        session['display'] = ''

    if 'img_loc' not in session:
        session['img_loc'] = ''

    return render_template('ninja.html', img=session['img_loc'], disp=session['display'])

@app.route('/ninja/<color>')
def show(color):
    if session['display'] == '':
        session['display'] = 'show'

    if color == 'blue':
        session['img_loc'] = "../static/img/leonardo.jpg"
    elif color == 'red':
        session['img_loc'] = "../static/img/raphael.jpg"
    elif color == 'orange':
        session['img_loc'] = "../static/img/michelangelo.jpg"
    elif color == 'purple':
        session['img_loc'] = "../static/img/donatello.jpg"
    else:
        session['img_loc'] = "../static/img/notapril.jpg"

    return redirect('/')

app.run(debug=True)
