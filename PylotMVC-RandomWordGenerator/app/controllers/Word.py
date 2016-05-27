from system.core.controller import Controller, request, redirect, session
import string as st
import random as rd

class Word(Controller):
    def __init__(self, action):
        super(Word, self).__init__(action)

    def index(self):
        if 'count' not in session:
            session['count'] = 0
        if 'word' not in session:
            session['word'] = ''

        return self.load_view('word.html', attempt=session['count'], word=session['word'])

    def gen(self):
        if session['word'] != '':
            session['word'] = ''

        for i in range(14):
            session['word'] += rd.choice(st.ascii_letters + st.digits)

        session['count'] += 1

        return redirect('/')
