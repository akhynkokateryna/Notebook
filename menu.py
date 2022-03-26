"Menu for Notebook"

import sys
from notebook import Notebook

class Menu:
    "Controls actions for notebook"

    def __init__(self):
        self.notebook = Notebook()
        self.actions = {1: self.show_notes,
                        2: self.add_note,
                        3: self.search_note_text,
                        4: self.search_note_id,
                        5: self.change_note,
                        6: self.change_tags,
                        7: self.quit}


    def show_options(self):
        "List of options"
        list_of_options = (""" Hi! Here is a list of possible actions
        1. Show notes
        2. Add note
        3. Search notes by using filter
        4. Search notes by id
        5. Change note
        6. Change note's tag
        7. Quit"""
        )
        print(list_of_options)


    def show_notes(self):
        "Shows all notes in the notebook"
        print("Here are the notes.")
        if len(self.notebook.notes) != 0:
            for note in self.notebook.notes:
                print(str(note))
        else:
            print("There are no notes yet.")


    def add_note(self):
        "Adds note to notebook"
        note = input("Enter the note: \n")
        self.notebook.new_note(note)
        print("Your note has been added to the notebook.")


    def change_tags(self):
        "Changes note's tags"
        note_id = int(input("Enter note's id: "))
        new_tags = input("Enter new tags: \n")
        self.notebook.modify_tags(note_id, new_tags)
        print("Tags have been modified.")


    def change_note(self):
        "Changes note's content"
        note_id = int(input("Enter note's id: "))
        new_note = input("Enter new note: \n")
        self.notebook.modify_memo(note_id, new_note)
        print("Note has been modified.")


    def search_note_text(self):
        "Searches for note in a notebook using a text filter"
        note_filter = input("Enter a filter (either tag or piece of a note): ")
        print(self.notebook.search(note_filter))


    def search_note_id(self):
        "Searches for note in a notebook using an id filter"
        note_id = int(input("Enter note's id: "))
        print(self.notebook._search_id(note_id))


    def quit(self):
        "Ends session"
        print("Thanks for the session today.")
        sys.exit()


    def run(self):
        "Executes the main actions"
        while True:
            self.show_options()
            option = int(input("Enter number of option: "))
            if option in self.actions:
                self.actions.get(option)()
            else:
                print("There is no such option.")
            print()


if __name__=="__main__":
    Menu().run()
