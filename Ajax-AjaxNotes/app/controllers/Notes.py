from system.core.controller import *

class Notes(Controller):
    def __init__(self, action):
        super(Notes, self).__init__(action)
        self.load_model('Note')
        self.__db = self.models['Note']

    def index(self):
        notes = self.__db.get_notes()
        return self.load_view('notes.html', notes = notes)

    def add(self):
        self.__db.add_note(request.form)
        notes = self.__db.get_notes()
        return self.load_view('note.html', notes = notes)

    def delete(self, id):
        self.__db.delete_note(id)
        notes = self.__db.get_notes()
        return self.load_view('note.html', notes = notes)

    def update(self, id):
        self.__db.update_note(id, request.form)
        notes = self.__db.get_notes()
        return self.load_view('note.html', notes = notes)
