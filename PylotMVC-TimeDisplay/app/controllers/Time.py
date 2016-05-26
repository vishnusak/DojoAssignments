from time import asctime
from system.core.controller import Controller

class Time(Controller):
    def __init__(self, action):
        super(Time, self).__init__(action)

    def index(self):
        cur_time = asctime()
        return self.load_view('time.html', time=cur_time)
