"""Main Address Book application
Bridge functions to connect gui and database.
"""

import sys
sys.path.insert(0, 'GUI')
import tkinter as Tk
import db
import new
from PIL import ImageTk, Image

def get_contact(contact):
    """Returns a contact."""
    entry = []

    try:
        if contact.split()[1]:
            entry.append(contact.split()[0])
            entry.append(contact.split()[1])
    except:
        entry.append('')
        entry.append(contact.split()[0])

    for row in db.get_entry(db.get_id(entry)):
        return row


def add_contact(contact):
    """Adds a contact to the database."""
    db.insert_entry(contact)


def remove_contact(contact):
    """Removes a contact."""
    entry = []
    try:
        entry.append(contact.split()[0])
    except:
        entry.append('')

    try:
        entry.append(contact.split()[1])
    except:
        entry.append('')

    db.delete_entry(db.get_id(entry))


def edit_contact(entry_id, contact):
    """Edits a contact.

    Keyword arguments:
    entry_id -- rowid for contact entry
    contact -- List containing contact entry information
    """
    db.edit_entry(entry_id, contact)


def search(search_string, sort):
    """Searches the database and returns the results."""
    return db.search_entry(search_string, sort)


if __name__ == "__main__":
    root = Tk.Tk()
    root.title('Address Book')
    img_file = Image.open('D:\\AddressBook-in-Python\\GUI\\photos\\office-flat-lay-composition-with-2177727.jpg')
    bg = ImageTk.PhotoImage(img_file)
    bgl = Tk.Label(root, image=bg)
    bgl.place(x=0, y=0)
    new.New_AddBookWindow(root)
    root.mainloop()
