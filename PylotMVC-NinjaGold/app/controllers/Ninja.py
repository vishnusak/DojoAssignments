from system.core.controller import Controller, redirect, request, session
from random import randint
from time import strftime
from json import dumps

class Ninja(Controller):
    def __init__(self, action):
        super(Ninja, self).__init__(action)

    def reset(self):
        session.clear()
        return redirect('/')

    def index(self):
        if 'score' not in session:
            session['score'] = 0
        if 'activities' not in session:
            session['activities'] = []

        return self.load_view('ninjagold.html')

    def process(self, building):
        activity = {}
        if building == 'farm':
            score = randint(10, 20)
            activity['color'] = 'green'
            activity['msg'] = 'Earned {} golds from the farm!'.format(score)
        elif building == 'cave':
            score = randint(5, 10)
            activity['color'] = 'green'
            activity['msg'] = 'Earned {} golds from the cave!'.format(score)
        elif building == 'house':
            score = randint(2, 5)
            activity['color'] = 'green'
            activity['msg'] = 'Earned {} golds from the house!'.format(score)
        else:
            score = randint(-50, 50)
            if score > 0:
                activity['color'] = 'green'
                activity['msg'] = 'Yay! Won {} golds at the casino!'.format(score)
            elif score == 0:
                activity['color'] = 'black'
                activity['msg'] = "Well! Atleast didn't lose anything at the casino!"
            else:
                activity['color'] = 'red'
                activity['msg'] = "Entered the casino and lost {} golds... Ouch!".format(abs(score))

        activity['time'] = strftime('%Y/%m/%d %I:%M %p')
        session['score'] += score
        activity['score'] = session['score']
        session['activities'].insert(0, activity)

        return dumps(activity)
