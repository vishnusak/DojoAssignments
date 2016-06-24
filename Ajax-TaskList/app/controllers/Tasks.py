from system.core.controller import *

class Tasks(Controller):
    def __init__(self, action):
        super(Tasks, self).__init__(action)
        self.load_model('Task')
        self.__db = self.models['Task']

    def index(self):
        tasks = self.__db.get_tasks()
        return self.load_view('tasklist.html', tasks = tasks)

    def add(self):
        self.__db.insert_task(request.form)
        tasks = self.__db.get_tasks()
        return self.load_view('list.html', tasks = tasks)

    def update(self, id):
        print("id  = {}").format(id)
        print("form = {}").format(request.form)
        print "~"*50
        self.__db.update_task(id, request.form)
        tasks = self.__db.get_tasks()
        return self.load_view('list.html', tasks = tasks)

    def delete(self, id):
        self.__db.delete_task(id)
        tasks = self.__db.get_tasks()
        return self.load_view('list.html', tasks = tasks)
