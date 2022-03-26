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
        
