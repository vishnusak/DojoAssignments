from system.core.controller import *

class Logins(Controller):
    def __init__(self, action):
        super(Logins, self).__init__(action)
        self.load_model('Login')
        self.__db = self.models['Login']

    def index(self):
        return self.load_view('login.html')

    def login(self):
        success = {
            'action': '',
            'user': ''
        }

        user_login = self.__db.login_validate(request.form)

        if user_login['status']:
            success['action'] = 'login'
            success['user'] = user_login['msg']
            return self.load_view('index.html', success = success)
        else:
            flash(user_login['msg'], 'login')
            return self.load_view('login.html')

    def register(self):
        success = {
            'action': '',
            'user': ''
        }

        user_register = self.__db.register_validate(request.form)
        print "user register", user_register
        if user_register['status']:
            success['action'] = 'register'
            success['user'] = user_register['msg']
            return self.load_view('index.html', success = success)
        else:
            flash(user_register['msg'], 'register')
            return self.load_view('login.html')
