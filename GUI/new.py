"""New Address Book Window"""
import tkinter as Tk
import db
import gui
import newcw
from PIL import ImageTk, Image
from tkinter import messagebox
import datetime

date = datetime.datetime.now().date()
date = str(date)
class New_AddBookWindow(object):

	def ok(self):
		"""Open the user specified address book."""
		book_name = self.book_name.get()

		if len(book_name) > 1:
			db.db_init(book_name)
			root = Tk.Tk()
			self.master.withdraw()
			root.protocol("WM_DELETE_WINDOW", exit)
			gui.mainWindow(root)
			root.mainloop()
			sys.exit()

		else: 
			self.c=newcw.ConfirmationWindow(self.master)


	def exit():
		root.destroy()


	def close_window(self):
		self.master.destroy()


	def __init__(self, master):
		self.new = master
		self.master = master
		self.master.title('New Address Book')
		self.master.geometry('906x571+350+200')
		self.master.resizable(False, False)
		self.date_label = Tk.Label(text="Today's Date: "+date, font="arial 12 bold", fg="orange", bg="white")
		self.date_label.place(x="600", y="80")
		self.book_name_label = Tk.Label(self.master, fg='blue', font='Arial 10 bold', text = 'COLLEGE MINI PROJECT')
		self.book_name_label.grid(rowspan=1, padx=(0, 140), pady=(15, 0))
		self.book_name_label = Tk.Label(self.master, fg='blue', font=("Helvetica", 20), text='Address Book Name:')
		self.book_name_label.grid(rowspan=3, padx=(20, 170), pady=(100, 0))
		self.book_name_label = Tk.Label(self.master, fg='blue', font='Arial 12 bold', text='Devloped By: Anubhav')
		self.book_name_label.grid(columnspan=5, padx=(400, 0), pady=(50, 0))
		self.instruction_message = Tk.Label(self.master, fg='red', bg="yellow", font=("Helvetica bold", 18), text = 'Enter the name of the new address book')
		self.instruction_message.grid(row = 1,columnspan=2, padx=(300, 0), pady=(0, 400))
		self.book_name = Tk.Entry(self.master, font=("Helvetica", 15))
		self.book_name.grid(row = 1 , column = 1, padx = 150, pady=(90, 0), ipady=5)

		self.cancel_button = Tk.Button(self.master, text = 'Cancel', fg='green', bg="yellow", command = self.close_window )
		self.cancel_button.grid(row = 1, column = 1, padx=(170, 0), pady=(250, 80))

		self.ok_button = Tk.Button(self.master, text= 'Ok', fg='green', bg="yellow", command = self.ok )
		self.ok_button.grid(row = 1, column = 1, sticky = Tk.E, padx=(0, 345), pady=(250, 80))
		self.master.mainloop()