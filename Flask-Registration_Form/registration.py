from flask import Flask, render_template, request, session, flash, redirect
from datetime import date
import re

app = Flask(__name__)

app.secret_key = "qp2349829m3m7m984qyrx87xry732xr48774ryt"

NUM    = re.compile('[0-9]')
U_CASE = re.compile('[A-Z]')
EMAIL  = re.compile('[a-zA-Z0-9\._-]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9]+')

@app.route('/')
def main():
    if ('flash' not in session):
        session['flash'] = 0

    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    session['flash'] = 0
    validate_name(request.form)
    validate_email(request.form)
    validate_pwd(request.form)
    validate_date(request.form)

    if (session['flash'] == 0):
        flash("Thanks for submitting your information", 'success')

    return redirect('/')

def validate_name(form):
    f_n = form['fname']
    l_n = form['lname']

    if (len(f_n) == 0):
        flash("First Name can't be left empty", 'fname')
        session['flash'] += 1
    else:
        if (NUM.search(f_n) != None):
            flash("Name field can't have numbers", 'fname')
            session['flash'] += 1

    if (len(l_n) == 0):
        flash("Last Name can't be left empty", 'lname')
        session['flash'] += 1
    else:
        if (NUM.search(l_n) != None):
            flash("Name field can't have numbers", 'lname')
            session['flash'] += 1

    return

def validate_email(form):
    e_m = form['email']

    if (len(e_m) == 0):
        flash("Email can't be left empty", 'email')
        session['flash'] += 1
    else:
        if (EMAIL.match(e_m) == None):
            flash("Invalid Email", 'email')
            session['flash'] += 1

    return

def validate_pwd(form):
    p_w = form['pwd']
    p_wc = form['pwd_c']

    if (len(p_w) < 8):
        flash("The password should be minimum 8 characters long", 'pwd')
        session['flash'] += 1
    elif (NUM.search(p_w) == None):
        flash("Password should have atleast 1 numeric value", 'pwd')
        session['flash'] += 1
    elif (U_CASE.search(p_w) == None):
        flash("Password should have atleast 1 UPPER case character", 'pwd')
        session['flash'] += 1

    if (p_wc != p_w):
        flash("Please type in the same password twice to confirm", 'pwd')
        session['flash'] += 1

    return

def validate_date(form):
    y = form['year']
    d = form['day']
    m = form['month']
    i_date = ''

    try:
        i_date = date(int(y), int(m), int(d))
    except Exception, err:
        flash("Invalid date - '{}'".format(err), 'dob')
        session['flash'] += 1

    if (i_date):
        today = date.today()
        diff = today - i_date
        if (diff.days <= 0):
            flash("Birthday must be in the past. Please enter a valid DOB", 'dob')
            session['flash'] += 1

    return

app.run(debug=True)
