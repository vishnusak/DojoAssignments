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

    def create(self, user):
        query = "INSERT INTO users (first_name, last_name, email, created_at, modified_at) VALUES('{}', '{}', '{}', NOW(), NOW())".format(user['fname'], user['lname'], user['email'])

        self.cur.execute(query)
        self.con.commit()

    def read(self,):
        query = "SELECT id, concat(first_name, ' ', last_name) as name, first_name, last_name, email, created_at FROM users"

        result_size = self.cur.execute(query)

        if result_size > 0:
            result = self.cur.fetchall()
        else:
            result = False

        return result

    def update(self, user):
        query = "UPDATE users SET first_name = '{}', last_name = '{}', email = '{}', modified_at = NOW() WHERE id = {}".format(user['fname'], user['lname'], user['email'], user['id'])

        self.cur.execute(query)
        self.con.commit()


    def delete(self, u_id):
        query = "DELETE FROM users WHERE id = {}".format(u_id)

        self.cur.execute(query)
        self.con.commit()

    def read_one(self, email):
        query = "SELECT id from users WHERE email = '{}'".format(email)

        result_size = self.cur.execute(query)

        if result_size > 0:
            result = self.cur.fetchone()[0]
        else:
            result = False

        return result
