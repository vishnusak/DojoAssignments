# from flask import Flask, # create instance of flask server
#                   render_template, # render html
#                   redirect, # allow route redirecting
#                   session, # enable sessions
#                   request, # accept form data from front-end
#                   flash # flash messages to the front-end
#
# from MySQLConnect import Sql # connect to DB.
#                              # allows select and insert ops
#
# from Validations import e_validate, # validate email
#                         n_validate, # validate email
#                         p_validate  # validate password
#
# from flask.ext.bcrypt import Bcrypt # Bcrypt for encrypting the password

from flask import Flask, render_template, redirect, session, request, flash

from MySQLConnect import Sql

from Validations import e_validate, n_validate, p_validate

from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "32198e32u39831ois28h328eyd47"

db = Sql(host='localhost', db='mypagedb')

crypt = Bcrypt(app)

@app.route('/')
def main():
    if 'login_name' not in session:
        session['login_name'] = ""
        session['lclass'] = 'show'
        session['rclass'] = 'hide'

    return render_template('login.html')

@app.route('/login', methods=['POST'])
def user_login():
    inp = request.form
    flash_msg = False

    mail_is_valid = e_validate(inp['email'])
    if not mail_is_valid:
        flash("Invalid EMAIL id", 'login')
        flash_msg = True
    else:
        inp_email = inp['email']

    if not flash_msg:
        inp_pwd= inp['password']
        db_pwd = db.get_pwd(inp_email)

        if db_pwd:
            if crypt.check_password_hash(db_pwd, inp_pwd):
                session['login_name'] = db.get_name(inp_email)
            else:
                flash("Password mismatch. Please enter the correct password", 'login')
                flash_msg = True
        else:
            flash("User not found. You have to be a registered user to login", 'login')
            flash_msg = True

    if not flash_msg:
        return render_template('main.html')
    else:
        session['lclass'] = 'show'
        session['rclass'] = 'hide'
        return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    inp = request.form
    user= {}
    flash_msg = False

    name_is_valid = n_validate(inp['fname'])
    if type(name_is_valid) is str:
        flash("The FIRST NAME is too short. Should have more than 2 characters", 'register')
        flash_msg = True
    elif not name_is_valid:
        flash("The FIRST NAME is not valid. Make sure there are no numbers in the FIRST NAME", 'register')
        flash_msg = True
    else:
        user['fname'] = inp['fname']

    name_is_valid = n_validate(inp['lname'])
    if type(name_is_valid) is str:
        flash("The LAST NAME is too short. Should have more than 2 characters", 'register')
        flash_msg = True
    elif not name_is_valid:
        flash("The LAST NAME is not valid. Make sure there are no numbers in the LAST NAME", 'register')
        flash_msg = True
    else:
        user['lname'] = inp['lname']

    mail_is_valid = e_validate(inp['email'])
    if not mail_is_valid:
        flash("Invalid EMAIL id", 'register')
        flash_msg = True
    else:
        user['email'] = inp['email']

    pwd_is_valid = p_validate(inp['password'])
    if type(pwd_is_valid) is str:
        flash("PASSWORD is too short. Make sure it is atleast 8 characters long", 'register')
        flash_msg = True
    elif not pwd_is_valid:
        flash("PASSWORD should contain atleast 1 Uppercase character and atleast 1 number", 'register')
        flash_msg = True
    else:
        if inp['password'] == inp['password_c']:
            user['pwd'] = crypt.generate_password_hash(inp['password'])
        else:
            flash("PASSWORD confirmation doesn't match. Please type in the same password to confirm", 'register')
            flash_msg = True

    if not flash_msg:
        db.register(user)
        session['lclass'] = 'show'
        session['rclass'] = 'hide'
        session['login_name'] = "{} {}".format(user['fname'], user['lname'])
        return render_template('main.html')
    else:
        session['lclass'] = 'hide'
        session['rclass'] = 'show'
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
