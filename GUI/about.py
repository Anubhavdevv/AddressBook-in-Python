"""Address Book About page """
import tkinter as Tk
class About_Window(object):

    def __init__(self, master):
        top = self.top = Tk.Toplevel(master)
        self.master = master
        top.title("About Us")
        self.master.geometry("750x600")
        self.master.resizable(False, False)
        # Team Cowsay logo
        self.photo = Tk.PhotoImage(master=top, file="D:\\AddressBook-in-Python\\GUI\photos\\teams.gif")
        self.photo_label = Tk.Label(top, image=self.photo)
        self.photo_label.grid(row=0, column=0)

        # Application information
        self.label = Tk.Label(top, text="Address Book by Team kratos")
        self.label.grid(row=1, column=0, padx=10, pady=10)
