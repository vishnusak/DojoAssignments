from system.core.model import Model

class Task(Model):
    def __init__(self):
        super(Task, self).__init__()
        self.__query = ''
        self.__data = {}

    def run_query(self, query, data):
        return self.db.query_db(query, data)

    def get_tasks(self):
        self.__query = "SELECT id, name, deleted FROM tasks"
        self.__data = {}
        return self.run_query(self.__query, self.__data)

    def update_task(self, id, form):
        print("id  = {}").format(id)
        print("form = {}").format(form)
        print "="*50
        self.__query = "UPDATE tasks SET name = :name WHERE id = :id"
        self.__data = {
            'id': id,
            'name': form['name']
        }
        return self.run_query(self.__query, self.__data)

    def delete_task(self, id):
        self.__query = "UPDATE tasks SET deleted = 1 WHERE id = :id"
        self.__data = {
            'id': id
        }
        return self.run_query(self.__query, self.__data)

    def insert_task(self, form):
        self.__query = "INSERT INTO tasks (name, deleted, created_at, modified_at) VALUES (:name, 0, NOW(), NOW())"
        self.__data = {
            'name': form['task']
        }
        return self.run_query(self.__query, self.__data)
