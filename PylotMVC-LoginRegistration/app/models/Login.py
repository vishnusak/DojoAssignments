from system.core.model import Model
import re

class Login(Model):
    def __init__(self):
        super(Login, self).__init__()
        self.__query = ''
        self.__data = {}

    def run_query(self, query, data={}):
        return self.db.query_db(query, data)

    def get_user(self, email):
        self.__query = "SELECT concat(first_name, ' ', last_name) as name, password FROM users WHERE email = :email"
        self.__data = {
            'email': email
        }
        return self.run_query(self.__query, self.__data)

    def register_user(self, user):
        self.__query = "INSERT INTO users (first_name, last_name, email, password, created_at, modified_at) VALUES(:first_name, :last_name, :email, :password, NOW(), NOW())"
        self.__data = {
            'first_name': user['fname'],
            'last_name': user['lname'],
            'email': user['email'],
            'password': user['pwd']
        }
        return self.run_query(self.__query, self.__data)

    def __name_validate(self, name):
        digit = re.compile('[0-9]')
        has_digit = digit.search(name)

        result = {
            'status': False,
            'msg': ''
        }

        if len(name) <= 2:
            result['msg'] = 'Name must be more than 2 chars'
        elif has_digit:
            result['msg'] = 'Name must not have numbers'
        else:
            result['status'] = True
            result['msg'] = ''

        return result

    def __email_validate(self, email):
        mail = re.compile(r'^[a-zA-Z0-9\._-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$')
        is_email = mail.match(email)

        result = {
            'status': False,
            'msg': ''
        }

        if is_email:
            result['status'] = True
            result['msg'] = ''
        else:
            result['msg'] = 'Invalid Email'

        return result

    def __r_pwd_validate(self, pwd, pwd_c):
        digit = re.compile('[0-9]')
        cap = re.compile('[A-Z]')
        has_digit = digit.search(pwd)
        has_cap = cap.search(pwd)

        result = {
            'status': False,
            'msg': ''
        }

        if len(pwd) < 8:
            result['msg'] = 'Password must be minimum 8 chars'
        elif not has_cap:
            result['msg'] = 'Password must have atleast 1 uppecase char'
        elif not has_digit:
            result['msg'] = 'Password must have atleast 1 digit'
        elif pwd != pwd_c:
            result['msg'] = "Password confirmation doesn't match"
        else:
            result['status'] = True
            result['msg'] = ''

        return result

    def __l_pwd_validate(self, pwd, pwd_hsh):
        digit = re.compile('[0-9]')
        cap = re.compile('[A-Z]')
        has_digit = digit.search(pwd)
        has_cap = cap.search(pwd)

        result = {
            'status': False,
            'msg': ''
        }

        if len(pwd) < 8:
            result['msg'] = 'Password must be minimum 8 chars'
        elif not has_cap:
            result['msg'] = 'Password must have atleast 1 uppecase char'
        elif not has_digit:
            result['msg'] = 'Password must have atleast 1 digit'
        elif not self.bcrypt.check_password_hash(pwd_hsh, pwd):
            result['msg'] = "Password mismatch"
        else:
            result['status'] = True
            result['msg'] = ''

        return result

    def login_validate(self, form):
        email_validity = self.__email_validate(form['email'])
        if email_validity['status']:
            user = self.get_user(form['email'])[0]
            pwd_validity = self.__l_pwd_validate(form['pwd'], user['password'])
            if pwd_validity['status']:
                pwd_validity['msg'] = user['name']
            return pwd_validity
        else:
            return email_validity

    def register_validate(self, form):
        fname_validity = self.__name_validate(form['fname'])
        if fname_validity['status']:
            lname_validity = self.__name_validate(form['lname'])
            if lname_validity['status']:
                email_validity = self.__email_validate(form['email'])
                if email_validity['status']:
                    user = self.get_user(form['email'])
                    print "user is", user
                    if not user:
                        pwd_validity = self.__r_pwd_validate(form['pwd'], form['pwd_c'])
                        if pwd_validity['status']:
                            user={
                                'fname': form['fname'],
                                'lname': form['lname'],
                                'email': form['email'],
                                'pwd': self.bcrypt.generate_password_hash(form['pwd']),
                            }
                            register = self.register_user(user)
                            return {'status': True, 'msg': '{} {}'.format(form['fname'], form['lname'])}
                        else:
                            return pwd_validity
                    else:
                        email_validity['status'] = False
                        email_validity['msg'] = "mail id already exists"
                        return email_validity
                else:
                    return email_validity
            else:
                return lname_validity
        else:
            return fname_validity
