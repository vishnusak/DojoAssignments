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

    def get_id(self, inp_email):
        query = "SELECT id FROM users WHERE email = '{}'".format(inp_email)

        result_size = self.cur.execute(query)

        if result_size == 1:
            result = self.cur.fetchone()[0]
        else:
            result = False

        return result

    def get_messages(self):
        query = "SELECT m.id, concat(u.first_name, ' ', u.last_name) as name, m.message_text, date_format(m.modified_at, '%M %D %Y'), m.modified_at as mdate FROM users u, messages m WHERE u.id = m.user_id ORDER BY m.modified_at DESC"

        result_size = self.cur.execute(query)

        if result_size > 0:
            result = self.cur.fetchall()
        else:
            result = False

        return result

    def insert_message(self, msg):
        query = "INSERT INTO messages (user_id, message_text, created_at, modified_at) VALUES('{}', '{}', NOW(), NOW())".format(msg['user_id'], msg['text'])

        self.cur.execute(query)
        self.con.commit()

    def delete_message(self, m_id):
        query = "DELETE from messages WHERE id = {}".format(m_id)

        self.cur.execute(query)
        self.con.commit()

    def get_comments(self, m_id):
        query = "SELECT c.id, concat(u.first_name, ' ', u.last_name) as name, c.comment_text, date_format(c.modified_at, '%M %D %Y') as cdate FROM comments c, users u WHERE c.message_id = {} and c.user_id = u.id ORDER BY c.modified_at DESC".format(m_id)

        result_size = self.cur.execute(query)

        if result_size > 0:
            result = self.cur.fetchall()
        else:
            result = False

        return result

    def insert_comment(self, cmt):
        query = "INSERT INTO comments (user_id, message_id, comment_text, created_at, modified_at) VALUES('{}', '{}', '{}', NOW(), NOW())".format(cmt['user_id'], cmt['message_id'], cmt['text'])

        self.cur.execute(query)
        self.con.commit()
