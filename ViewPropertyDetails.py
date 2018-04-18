# Visitor View Property Details 
import pickle
import MySQLdb as sql
from tkinter import *
from tkinter import ttk
''' TODO
get the property info
put property info next to labels
check if user has already rated a property
add rate your visit UI
add log visit function
add unlog visit function
add back button function
CURRENTLY DOING
passing data
'''

class ViewPropertyDetails(Frame):
	def __init__(self, master, cursor):
		Frame.__init__(self, master)

		self.cursor = cursor
		self.uname = ""
		self.d = ""
	def populate(self, data):
		self.d = data
		self.label = Label(self, text=f"{self.d['PropertyName']} Details", font="Times 24")
		self.label.grid(row=0, column=0, sticky=W)

		self.name_label = Label(self, text=f"Name: {self.d['PropertyName']}", font="Times 12")
		self.name_label.grid(row=1, column=0, sticky=W)

		self.owner_label = Label(self, text=f"Owner: {self.d['Owner']}", font="Times 12")
		self.owner_label.grid(row=2, column=0, sticky=W)

		self.owner_email_laebl = Label(self, text=f"Owner Email: {self.d['Email']}", font="Times 12")
		self.owner_email_laebl.grid(row=3, column=0, sticky=W)

		self.addr_label = Label(self, text=f"Address: {self.d['Address']}", font="Times 12")
		self.addr_label.grid(row=4, column=0, sticky=W)

		self.city_label = Label(self, text=f"City: {self.d['City']}", font="Times 12")
		self.addr_label.grid(row=5, column=0, sticky=W)

		self.zip_label = Label(self, text=f"Zip: {self.d['Zip']}", font="Times 12")
		self.zip_label.grid(row=6, column=0, sticky=W)

		self.size_label = Label(self, text=f"Size (Acres): {self.d['Size']}", font="Times 12")
		self.size_label.grid(row=7, column=0, sticky=W)

		self.visits_label = Label(self, text=f"Visits: {self.d['Visits']}", font="Times 12")
		self.visits_label.grid(row=8, column=0, sticky=W)

		self.avg_rating_label = Label(self, text=f"Avg. Rating: {self.d['Avg Rating']}", font="Times 12")
		self.avg_rating_label.grid(row=9, column=0, sticky=W)

		self.type_label = Label(self, text=f"Type: {self.d['PropertyType']}", font="Times 12")
		self.type_label.grid(row=10, column=0, sticky=W)

		self.public_label = Label(self, text=f"Public: {self.d['Commercial']}", font="Times 12")
		self.public_label.grid(row=11, column=0, sticky=W)

		self.commercial_label = Label(self, text=f"Commercial: {self.d['Commercial']}", font="Times 12")
		self.commercial_label.grid(row=12, column=0, sticky=W)

		self.id_label = Label(self, text=f"ID: {self.d['ID']}", font="Times 12")
		self.id_label.grid(row=13, column=0, sticky=W)

		self.has_label = Label(self, text=f"Has: {self.d['Items']}", font="Times 12")
		self.has_label.grid(row=14, column=0, sticky=W)

	# Functions
	def which_screen(self):
		# Rating UI
		sql = f"SELECT Rating FROM Visit WHERE Username='{self.uname}' AND PropertyID='{self.d['ID']}'"
		self.cursor.execute(sql)
		data = self.cursor.fetchall()
		print(data) 
		if data:
			self.rate_label = Label(self, text="Rate Visit:", font="Times 12")
			self.rate_label.grid(row=1, column=1)

			self.rate_entry = Entry(self)
			self.rate_entry.insert(0, "1-5")
			self.rate_entry.grid(row=2, column=1)


			# Buttons
			self.log_button = Button(self, text="Log Visit", font="Times 12", \
						command=lambda: log_visit(self, self.rate_entry.get()))
			self.log_button.grid(row=3, column=1)
		else:
			self.unlog_button = Button(self, text="Un-Log Visit", font="Times 12", \
						command=lambda: unlog_visit(self))
			self.unlog_button.grid(row=4, column=1)

		self.back_button = Button(self, text="Back", font="Times 12", \
					command=lambda: back_go(self))
		self.back_button.grid(row=5, column=1)

	def back_go(self):
		self.master.master.show_window("VisitorHomeWindow")

	def set_uname(self, data):
		self.uname = data

	def log_visit(self, rating):
		if int(rating) not in [1, 2, 3, 4, 5]:
			pass
		else:
			sql = f"INSERT INTO Visit VALUES ('{self.uname}', '{self.d['ID']}', NOW(), '{rating}'"
			self.cursor.execute(sql)
			self.master.master.windows["ViewPropertyDetails"].which_screen()

	def unlog_visit(self):
		sql = f"DELETE FROM Visit WHERE Username='{self.uname}' AND PropertyID='{self.d['PropertyID']}'"
		self.cursor.execute(sql)
		self.master.master.windows["ViewPropertyDetails"].which_screen()