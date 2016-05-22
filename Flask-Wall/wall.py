from flask import Flask, redirect, render_template, session, request
from flask.ext.bcrypt import Bcrypt
from MySQLConnect import Sql
from datetime import datetime

# Create the server instacce
app = Flask(__name__)

# Secret key is necessary for session/cookies to work
app.secret_key = "82ymy\84myr4y4x7ymudjmm?948mc8mx`98u4m7h9uc9x3,1309iu"

# Create an object via which DB queries are executed
db = Sql(host='localhost', db='wall-test')

# Create an object via which password encryption and checking is done
crypt = Bcrypt(app)

# =====================================================================
# Start setting up routes
# =====================================================================

# Route for Logout
@app.route('/logout', methods=['POST', 'GET'])
def logout():
    session.clear()
    return redirect('/')

# =====================================================================

# Route for registration page
@app.route('/register', methods=['POST'])
def register():
    inp = request.form
    err = {
            'count': 0,
            'fname': '',
            'lname': '',
            'email': '',
            'password': '' ,
            'password_c': ''
    }
    user = {}

    user['fname'] = inp['fname']
    user['lname'] = inp['lname']
    user['email'] = inp['email']
    user['pwd'] = crypt.generate_password_hash(inp['password'])

    db.register(user)
    session['login_name'] = "{} {}".format(user['fname'], user['lname'])
    session['email'] = user['email']
    session['u_id'] = db.get_id(user['email'])

    return redirect('/wall')

# =====================================================================

# Route for login page
@app.route('/login', methods=['POST'])
def login():
    session['login_err'] = {}
    inp = request.form
    err = {
            'count': 0,
            'email': '',
            'password': ''
    }
    user = {}

    inp_email = inp['email']
    inp_pwd = inp['password']

    db_pwd = db.get_pwd(inp_email)

    if db_pwd:
        if crypt.check_password_hash(db_pwd, inp_pwd):
            session['login_name'] = db.get_name(inp_email)
            session['email'] = inp_email
            session['u_id'] = db.get_id(inp_email)

            return redirect('/wall')
        else:
            session['login_err']['pwd'] = "Password mismatch."
            return redirect('/')
    else:
        session['login_err']['user'] = "User not found. Please register to login"
        return redirect('/')

# =====================================================================

# Main route. Kicks off the application
@app.route('/')
def wall_login():
    # initialize the session variables here
    if 'login_name' not in session:
        session['login_name'] = ''

    if 'email' not in session:
        session['email'] = ''
    elif (session['email'] != ''):
        return redirect('/wall')

    if 'u_id' not in session:
        session['u_id'] = ''

    if 'login_err' not in session:
        session['login_err'] = {}

    if 'messages' not in session:
        session['messages'] = []

    if 'comments' not in session:
        session['comments'] = []

    return render_template('login.html')

# =====================================================================

# Route for handling message posting on the wall
@app.route('/in_message', methods=['POST'])
def in_message():
    inp = request.form

    msg = {
        'user_id': '',
        'text': ''
    }

    msg['user_id'] = session['u_id']
    msg['text'] = inp['in_message_text']

    db.insert_message(msg)

    retrieve_messages()
    return render_template('messages.html')

# =====================================================================

# Route for handling deleting messages from the wall
# Singed in users can delete their own messages if they are posted within last 30 mins
@app.route('/del_message', methods=['POST'])
def del_message():
    inp = request.form

    db.delete_message(inp['msg_id'])

    retrieve_messages()
    return render_template('messages.html')

# =====================================================================

# Route for handling posting comments for exiting messages
@app.route('/post_comment', methods=['POST'])
def post_comment():
    inp = request.form

    if 'in_comment_text' in inp:
        cmt = {
            'user_id': '',
            'message_id': '',
            'text': ''
        }

        cmt['user_id'] = session['u_id']
        cmt['message_id'] = inp['msg_id']
        cmt['text'] = inp['in_comment_text']

        db.insert_comment(cmt)

    retrieve_comments(inp['msg_id'])
    return render_template('comments.html')

# =====================================================================

# Route for displaying the main page of the wall after login
@app.route('/wall', methods=['POST', 'GET'])
def wall_main():
    if request.method == 'GET':
        if (session['email'] == '') or ('email' not in session):
            return redirect('/')

    retrieve_messages()
    session['comments'] = []
    return render_template('wall.html')

# =====================================================================

# =====================================================================
# Start defining internal functions
# =====================================================================

# Function to retrieve all existing messages to be displayed on the wall
def retrieve_messages():
    session['messages'] = []
    # "messages" will be a tuple of tuples
    messages = db.get_messages()

    if messages:
        for msg_row in messages:
            msg = {
                'user': '',
                'id': '',
                'text': '',
                'date': '',
                'del': ''
            }

            msg['id'] = msg_row[0]
            msg['user'] = msg_row[1]
            msg['text'] = msg_row[2]
            msg['date'] = msg_row[3]
            diff = datetime.now() - msg_row[4]
            if diff.total_seconds() > 1800:
                msg['del'] = False
            else:
                msg['del'] = True
            session['messages'].append(msg)

# =====================================================================

# Function to retrieve all existing comments for a given message
def retrieve_comments(m_id):
    session['comments'] = []
    # "comments" will be a tuple of tuples
    comments = db.get_comments(m_id)

    if comments:
        for cmt_row in comments:
            cmt = {
                'user': '',
                'id': '',
                'text': '',
                'date': ''
            }

            cmt['id'] = cmt_row[0]
            cmt['user'] = cmt_row[1]
            cmt['text'] = cmt_row[2]
            cmt['date'] = cmt_row[3]
            session['comments'].append(cmt)

# =====================================================================

if __name__ == "__main__":
    # host='0.0.0.0' opens the server to accept requests from any machine on the connected network instead of just from loclhost
    app.run(host='0.0.0.0', debug = True)
