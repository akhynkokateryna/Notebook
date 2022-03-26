"Notebook"

import datetime

class Note:
    "Represents a note in a notebook"

    note_id = 0

    def __init__(self, memo, tags=""):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        Note.note_id += 1
        self.id = Note.note_id

    def match(self, search_filter:str):
        "Returns True if filter in memo or tags"
        return search_filter in self.memo or search_filter in self.tags

    def __str__(self):
        return f"""Your note:
        id = {self.id}
        memo = {self.memo}
        date = {self.creation_date}
        tags = {self.tags}"""


class Notebook:
    "Represents a container with all notes"

    def __init__(self):
        self.notes = []

    def search(self, note_filter:str):
        "Returns list of notes that contain given filter"
        return [note for note in self.notes if note.match(note_filter)]

    def new_note(self, memo, tags=""):
        "Adds note to notebook"
        self.notes.append(Note(memo, tags))

    def _search_id(self, note_id):
        "Returns note with given id"
        for note in self.notes:
            if note.id == note_id:
                return note

    def modify_memo(self, note_id, memo):
        "Finds note with its id and changes it"
        self._search_id(note_id).memo = memo

    def modify_tags(self, note_id, tags):
        "Finds note with its id and changes its tags"
        self._search_id(note_id).tags = tags
