from system.core.model import Model

class Note(Model):
    def __init__(self):
        super(Note, self).__init__()
        self.__query = ''
        self.__data = {}

    def run_query(self, query, data={}):
        return self.db.query_db(query, data)

    def get_notes(self):
        self.__query = "SELECT id, post as note from posts"
        self.__data = {}
        return self.run_query(self.__query, self.__data)

    def add_note(self, form):
        self.__query = "INSERT INTO posts (post, created_at, modified_at) VALUES (:note, NOW(), NOW())"
        self.__data = {
            'note': form['note']
        }
        return self.run_query(self.__query, self.__data)

    def delete_note(self, id):
        self.__query = "DELETE FROM posts WHERE id = :id"
        self.__data = {
            'id': id
        }
        return self.run_query(self.__query, self.__data)

    def update_note(self, id, form):
        self.__query = "UPDATE posts SET post = :note WHERE id = :id"
        self.__data = {
            'id': id,
            'note': form['note']
        }
        return self.run_query(self.__query, self.__data)
