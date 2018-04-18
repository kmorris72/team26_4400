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

	def populate(self, data):
		d = data
		self.label = Label(self, text=f"{d['PropertyName']} Details", font="Times 24")
		self.label.grid(row=0, column=0, sticky=W)

		self.name_label = Label(self, text=f"Name: {d['PropertyName']}", font="Times 12")
		self.name_label.grid(row=1, column=0, sticky=W)

		self.owner_label = Label(self, text=f"Owner: {d['Owner']}", font="Times 12")
		self.owner_label.grid(row=2, column=0, sticky=W)

		self.owner_email_laebl = Label(self, text=f"Owner Email: {d['Email']}", font="Times 12")
		self.owner_email_laebl.grid(row=3, column=0, sticky=W)

		self.addr_label = Label(self, text=f"Address: {d['Address']}", font="Times 12")
		self.addr_label.grid(row=4, column=0, sticky=W)

		self.city_label = Label(self, text=f"City: {d['City']}", font="Times 12")
		self.addr_label.grid(row=5, column=0, sticky=W)

		self.zip_label = Label(self, text=f"Zip: {d['Zip']}", font="Times 12")
		self.zip_label.grid(row=6, column=0, sticky=W)

		self.size_label = Label(self, text=f"Size (Acres): {d['Size']}", font="Times 12")
		self.size_label.grid(row=7, column=0, sticky=W)

		self.visits_label = Label(self, text=f"Visits: {d['Visits']}", font="Times 12")
		self.visits_label.grid(row=8, column=0, sticky=W)

		self.avg_rating_label = Label(self, text=f"Avg. Rating: {d['Avg Rating']}", font="Times 12")
		self.avg_rating_label.grid(row=9, column=0, sticky=W)

		self.type_label = Label(self, text=f"Type: {d['PropertyType']}", font="Times 12")
		self.type_label.grid(row=10, column=0, sticky=W)

		self.public_label = Label(self, text=f"Public: {d['Commercial']}", font="Times 12")
		self.public_label.grid(row=11, column=0, sticky=W)

		self.commercial_label = Label(self, text=f"Commercial: {d['Commercial']}", font="Times 12")
		self.commercial_label.grid(row=12, column=0, sticky=W)

		self.id_label = Label(self, text=f"ID: {d['ID']}", font="Times 12")
		self.id_label.grid(row=13, column=0, sticky=W)

		self.has_label = Label(self, text=f"Has: {d['Items']}", font="Times 12")
		self.has_label.grid(row=14, column=0, sticky=W)

		# TODO
		# Add if block to show the correct screen
		# Rating UI
		self.rate_label = Label(self, text="Rate Visit: ", font="Times 12")
		self.rate_label.grid(row=1, column=1)

		self.rate_entry = Entry(self)
		self.rate_entry.insert(0, "1-5")
		self.rate_entry.grid(row=2, column=1)

		# Buttons
		self.log_button = Button(self, text="Log Visit", font="Times 12", \
					command=lambda: print("Still gotta make this log visits"))
		self.log_button.grid(row=3, column=1)

		self.unlog_button = Button(self, text="Un-Log Visit", font="Times 12", \
					command=lambda: print("Still gotta make this unlog visits"))
		self.unlog_button.grid(row=4, column=1)

		self.back_button = Button(self, text="Back", font="Times 12", \
					command=lambda: back_go(self))
		self.back_button.grid(row=5, column=1)


	# Functions
	def back_go(self):
		self.master.master.show_window("VisitorHomeWindow")

		


