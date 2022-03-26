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

    def modify_memo(self, note_id, memo):
        "Finds note with its id and changes it"
        for note in self.notes:
            if note.id == note_id:
                note.memo = memo
                break

    def modify_tags(self, note_id, tags):
        "Finds note with its id and changes its tags"
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break
