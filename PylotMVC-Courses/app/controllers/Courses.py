from system.core.controller import Controller, session, redirect, request
from json import dumps

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        self.load_model('Course')
        self.__db=self.models['Course']

    def index(self):
        return self.load_view('course.html')

    def add(self):
        inp = request.form
        self.__db.add_course(inp)
        return dumps(self.get_all())

    def get_all(self):
        courses = self.__db.get_all_courses()
        return courses

    def load(self):
        return dumps(self.get_all())

    def show(self, id):
        course = self.__db.get_course_by_id(id)
        return self.load_view('remove.html', course=course[0])

    def remove(self, id):
        print(id)
        self.__db.delete_course(id)
        return redirect('/')
