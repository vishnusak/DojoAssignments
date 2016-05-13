from flask import Flask, render_template

myapp = Flask(__name__)

@myapp.route('/')
def main():
    return render_template('index.html')

@myapp.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@myapp.route('/dojos/new')
def new():
    return render_template('dojos.html')

myapp.debug = True
myapp.run()
