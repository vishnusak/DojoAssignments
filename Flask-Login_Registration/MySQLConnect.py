import MySQLdb as ms

class Sql(object):
    """ Sql: Class to provide an abstraction for connecting and querying against MySQL server """
    def __init__(self, host, db, user='root', pwd='1979', port=3306):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        self.port = port

        self.con = ms.connect(host=self.host, user=self.user, passwd=self.pwd, db=self.db, port=self.port)

        self.cur = self.con.cursor()

    def get_pwd(self, inp_email):
        query = "SELECT password FROM users WHERE email = '{}'".format(inp_email)

        result_size = self.cur.execute(query)

        if result_size == 1:
            result = self.cur.fetchone()[0]
        else:
            result = False

        return result

    def get_name(self, inp_email):
        query = "SELECT concat(first_name, ' ', last_name) FROM users WHERE email = '{}'".format(inp_email)

        result_size = self.cur.execute(query)

        if result_size == 1:
            result = self.cur.fetchone()[0]
        else:
            result = False

        return result

    def register(self, user):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, modified_at) VALUES('{}', '{}', '{}', '{}', NOW(), NOW())".format(user['fname'], user['lname'], user['email'], user['pwd'])

        self.cur.execute(query)
        self.con.commit()
