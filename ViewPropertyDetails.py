# Visitor View Property Details 
import datetime
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
ATTRS = 'Name, ID, Street, Size, City, Zip, PropertyType, IsPublic, IsCommercial'


class ViewPropertyDetails(Frame):
	def __init__(self, master, cursor):
		Frame.__init__(self, master)

		self.cursor = cursor
		
		# these are set by functions below
		self.uname = ""
		self.d = ""

	# this is necessary to update the widget text after
	# user has selected a property to view
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

	# show appropriate screen based on if user has visted the property or not
	def which_screen(self):

		# check if user has visited the selected property
		sql = f"SELECT Rating FROM Visit WHERE Username='{self.uname}' AND PropertyID='{self.d['ID']}'"
		self.cursor.execute(sql)
		data = self.cursor.fetchall()

		# program will complain if user has not visited it yet
		try:
			if data[0][0] in [1, 2, 3, 4, 5]:

				# necessary to avoid printing errors on first time
				# user accesses this screen
				try:
					self.rate_label.grid_forget()
					self.rate_entry.grid_forget()
					self.log_button.grid_forget()
				except: pass
				self.unlog_button = Button(self, text="Un-Log Visit", font="Times 12", \
							command=lambda: self.unlog_visit())
				self.unlog_button.grid(row=15, column=0)
		except:
			try:
				self.unlog_button.grid_forget()
			except: pass
			self.rate_label = Label(self, text="Rate Visit:", font="Times 12")
			self.rate_label.grid(row=15, column=0)

			self.rate_entry = Entry(self)
			self.rate_entry.insert(0, "1-5")
			self.rate_entry.grid(row=16, column=0)


			# Buttons
			self.log_button = Button(self, text="Log Visit", font="Times 12", \
						command=lambda: self.log_visit(self.rate_entry.get()))
			self.log_button.grid(row=17, column=0)

		self.back_button = Button(self, text="Back", font="Times 12", \
					command=lambda: self.back_go())
		self.back_button.grid(row=18, column=0)

	def back_go(self):
		self.master.master.show_window("VisitorHomeWindow")

	# passed by LoginWindow
	def set_uname(self, data):
		self.uname = data

	# insert rating into DB
	def log_visit(self, rating):
		if int(rating) not in [1, 2, 3, 4, 5]:
			self.master.master.show_window("ViewPropertyDetails")
			pass
		else:
			# insert rating
			sql = f"INSERT INTO Visit VALUES ('{self.uname}', '{self.d['ID']}', '{datetime.datetime.now()}', '{rating}')"
			self.cursor.execute(sql)
			
			# update VisitorHomeWindow table
			sql = f"SELECT {ATTRS}, COUNT(Rating), AVG(Rating) FROM Property LEFT OUTER JOIN \
					Visit ON ID=PropertyID GROUP BY Name"
			self.master.master.windows["VisitorHomeWindow"].populate_table(sql)
			
			# Return to VisitorHomeWindow because I don't want to yet bother with
			# updating the rating stats and refreshing this screen
			self.master.master.show_window("VisitorHomeWindow")

	# this works i think
	def unlog_visit(self):
		# remove visitor's rating
		sql = f"DELETE FROM Visit WHERE Username='{self.uname}' AND PropertyID='{self.d['ID']}'"
		self.cursor.execute(sql)

		# send user back because I don't want to mess with
		# updating the property and refreshing this screen at once
		sql = f"SELECT {ATTRS}, COUNT(Rating), AVG(Rating) FROM Property LEFT OUTER JOIN \
				Visit ON ID=PropertyID GROUP BY Name"
		self.master.master.windows["VisitorHomeWindow"].populate_table(sql)
		self.master.master.show_window("VisitorHomeWindow")