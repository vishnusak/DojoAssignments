from system.core.controller import Controller, request, redirect, session

class Survey(Controller):
    def __init__(self, action):
        super(Survey, self).__init__(action)

    def index(self):
        if 'submit' not in session:
            session['submit'] = 0
        if 'name' not in session:
            session['name'] = ''
        if 'language' not in session:
            session['language'] = ''
        if 'location' not in session:
            session['location'] = ''
        if 'comment' not in session:
            session['comment'] = ''

        return self.load_view('survey.html')

    def survey(self):
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']
        session['submit'] += 1
        
        return redirect('/view')

    def view(self):
        return self.load_view('survey_view.html')
