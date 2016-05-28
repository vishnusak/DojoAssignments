from system.core.model import Model

class Course(Model):
    def __init__(self):
        super(Course, self).__init__()
        self.__query = ''
        self.__data = {}

    def run_query(self):
        return self.db.query_db(self.__query, self.__data)

    def get_all_courses(self):
        # self.__query = 'SELECT * FROM courses ORDER BY created_at DESC'
        self.__query = 'SELECT id, title, description, date_format(created_at, "%b %D %Y %l:%i%p") as created FROM courses ORDER BY created_at DESC'
        self.__data = {}
        return self.run_query()

    def get_course_by_id(self, id):
        self.__query = 'SELECT * FROM courses WHERE id = :course_id'
        self.__data = {
            'course_id': id
        }
        return self.run_query()

    def add_course(self, course):
        self.__query = 'INSERT INTO courses(title, description, created_at, updated_at) VALUES(:title, :description, NOW(), NOW())'
        self.__data = {
        'title': course['title'],
        'description': course['desc']
        }
        return self.run_query()

    def update_course(self, course):
        self.__query = 'UPDATE courses SET title=:title, description=:description, updated_at=NOW() WHERE id=:id'
        self.__data = {
        'title': course['title'],
        'description': course['desc'],
        'id': course['id']
        }
        return self.run_query()

    def delete_course(self, id):
        self.__query = 'DELETE FROM courses WHERE id = :id'
        self.__data = {
            'id': id
        }
        return self.run_query()
