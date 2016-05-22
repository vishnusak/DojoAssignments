from flask import Flask, redirect, render_template, session, request
from MySQLConnect import Sql
from datetime import datetime

app=Flask(__name__)
app.secret_key = 'sdc<iu3h32/uxwnuxwe{ehjfd87wq2?q9873987ew~497434.38u928'

db = Sql(host='localhost', db='mypagedb')

@app.route('/')
@app.route('/users', methods=['GET'])
def main():
    if 'users_in_db' not in session:
        session['users_in_db'] = []
    if 'u_id' not in session:
        session['u_id'] = []

    if session['users_in_db'] == []:
        get_users()

    return render_template('index.html')


@app.route('/users/new', methods=['GET'])
def add_user():
    return render_template('new.html')


@app.route('/users/create', methods=['POST'])
def create():
    inp = request.form
    user = {
        'fname': inp['fname'],
        'lname': inp['lname'],
        'email': inp['email']
    }

    db.create(user)
    get_users()
    user_id = db.read_one(user['email'])
    return redirect('/users/{}'.format(user_id))


@app.route('/users/<u_id>', methods=['GET'])
def show(u_id):
    u_id = int(u_id)
    user_pos = session['u_id'].index(u_id)

    user={
        'id': session['users_in_db'][user_pos]['id'],
        'name': session['users_in_db'][user_pos]['name'],
        'email': session['users_in_db'][user_pos]['email'],
        'created_at': session['users_in_db'][user_pos]['created_at']
    }

    return render_template('show.html', user=user)


@app.route('/users/<u_id>/edit', methods=['GET'])
def edit(u_id):
    u_id = int(u_id)
    user_pos = session['u_id'].index(u_id)

    user={
        'id': session['users_in_db'][user_pos]['id'],
        'fname': session['users_in_db'][user_pos]['fname'],
        'lname': session['users_in_db'][user_pos]['lname'],
        'email': session['users_in_db'][user_pos]['email']
    }

    return render_template('edit.html', user=user)


@app.route('/users/<u_id>/update', methods=['POST'])
def update(u_id):
    u_id = int(u_id)

    inp = request.form
    user = {
        'fname': inp['fname'],
        'lname': inp['lname'],
        'email': inp['email'],
        'id': u_id
    }

    db.update(user)

    return redirect('/users/{}'.format(u_id))

@app.route('/users/<u_id>/destroy', methods=['GET'])
def destroy(u_id):
    u_id = int(u_id)

    db.delete(u_id)
    get_users()

    return redirect('/users')

def get_users():
    user={
        'id': '',
        'name': '',
        'fname': '',
        'lname': '',
        'email': '',
        'created_at': ''
    }
    session['u_id'] = []
    session['users_in_db'] = []

    allrows = db.read()

    if allrows:
        for row in allrows:
            user = {}
            user['id']         = row[0]
            user['name']       = row[1]
            user['fname']      = row[2]
            user['lname']      = row[3]
            user['email']      = row[4]
            user['created_at'] = row[5].strftime('%B %d, %Y')

            session['u_id'].append(user['id'])
            session['users_in_db'].append(user)

if __name__ == '__main__':
    app.run(debug = True)
