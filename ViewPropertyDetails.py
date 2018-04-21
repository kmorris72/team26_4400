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
		self.from_hist = 0

	# this is necessary to update the widget text after
	# user has selected a property to view
	def populate(self, data):
		try:
			wids = [self.type_label, self.label, self.name_label, self.owner_label, self.owner_email_label, \
			self.addr_label, self.city_label, self.zip_label, self.size_label, self.visits_label, \
			self.avg_rating_label, self.public_label, self.commercial_label, self.id_label, \
			self.type_label, self.has_label]
			for w in wids:
				w.config(text="")
		except: pass #print('failed')

		# i'm sorry about all of these try except blocks
		# i know i'm better than this but time is short
		# and stress is high
		try:
			self.rate_label.grid_forget()
			self.rate_entry.grid_forget()
			self.log_button.grid_forget()
		except: pass

		try:
			self.unlog_button.grid_forget()
		except: pass

		try:
			self.back_button.grid_forget()
		except: pass

		self.d = data
		self.label = Label(self, text=f"{self.d['PropertyName']} Details", font="Times 24")
		self.label.grid(row=0, column=0, sticky=W)

		self.name_label = Label(self, text=f"Name: {self.d['PropertyName']}", font="Times 12")
		self.name_label.grid(row=1, column=0, sticky=W)

		self.owner_label = Label(self, text=f"Owner: {self.d['Owner']}", font="Times 12")
		self.owner_label.grid(row=2, column=0, sticky=W)

		self.owner_email_label = Label(self, text=f"Owner Email: {self.d['Email']}", font="Times 12")
		self.owner_email_label.grid(row=3, column=0, sticky=W)

		self.addr_label = Label(self, text=f"Address: {self.d['Address']}", font="Times 12")
		self.addr_label.grid(row=4, column=0, sticky=W)

		self.city_label = Label(self, text=f"City: {self.d['City']}", font="Times 12")
		self.city_label.grid(row=5, column=0, sticky=W)

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

		self.back_button = Button(self, text="Back", font="Times 12", \
					command=lambda: self.back_go())
		self.back_button.grid()

	# Functions

	# show appropriate screen based on if user has visted the property or not
	def which_screen(self):

		# check if user has visited the selected property
		sql = f"SELECT Rating FROM Visit WHERE Username='{self.uname}' AND PropertyID='{self.d['ID']}'"
		self.cursor.execute(sql)
		data = self.cursor.fetchall()
		#print(data)
		# program will complain if user has not visited it yet
		try:
			if data[0][0] in [1, 2, 3, 4, 5]:
		#		print("in if")
				# necessary to avoid printing errors on first time
				# user accesses this screen
				try:
					self.rate_label.grid_forget()
					self.rate_entry.grid_forget()
					self.log_button.grid_forget()
		#			print("i forgot the rating UI")
				except: pass #print("can't forget rating UI")
				self.unlog_button = Button(self, text="Un-Log Visit", font="Times 12", \
							command=lambda: self.unlog_visit())
				self.unlog_button.grid()
		except:
			#print("in except")
			try:
				self.unlog_button.grid_forget()
			#	print("I forgit the unlog")
			except: pass # print("can't forget unlog UI")
			self.rate_label = Label(self, text="Rate Visit:", font="Times 12")
			self.rate_label.grid()

			self.rate_entry = Entry(self)
			self.rate_entry.insert(0, "1-5")
			self.rate_entry.grid()

			# Buttons
			self.log_button = Button(self, text="Log Visit", font="Times 12", \
						command=lambda: self.log_visit(self.rate_entry.get()))
			self.log_button.grid()

	def back_go(self):
		try:
			self.rate_label.grid_forget()
			self.rate_entry.grid_forget()
			self.log_button.grid_forget()
		except:
			self.unlog_button.grid_forget()
		self.back_button.grid_forget()
		if (self.from_hist == 1):
			self.from_hist = 0
			self.master.master.windows["VisitHistory"].populate()
			self.master.master.show_window("VisitHistory")
		else:
			self.master.master.show_window("VisitorHomeWindow")

	# passed by LoginWindow
	def set_uname(self, data):
		self.uname = data

	# insert rating into DB
	def log_visit(self, rating):
		if int(rating) not in [1, 2, 3, 4, 5]:
			self.master.master.show_window("ViewPropertyDetails")
		else:
			self.rate_label.grid_forget()
			self.rate_entry.grid_forget()
			self.log_button.grid_forget()
			self.back_button.grid_forget()

			# insert rating
			sql = f"INSERT INTO Visit VALUES ('{self.uname}', '{self.d['ID']}', '{datetime.datetime.now()}', '{rating}')"
			self.cursor.execute(sql)
			
			# update VisitorHomeWindow table
			sql = f"SELECT {ATTRS}, COUNT(Rating), AVG(Rating) FROM Property LEFT OUTER JOIN \
				Visit ON ID=PropertyID GROUP BY Name"
			self.master.master.windows["VisitorHomeWindow"].populate_table(sql)
			
			# update property details
			sql = f"SELECT COUNT(Username), AVG(Rating) FROM Visit WHERE PropertyID='{self.d['ID']}' \
					AND Username='{self.uname}'"
			self.cursor.execute(sql)
			data = self.cursor.fetchall()
			self.d['Visits'] = data[0][0]
			self.d['Avg Rating'] = data[0][1]
			self.master.master.windows['ViewPropertyDetails'].grid_forget()
			self.populate(self.d)
			# self.which_screen()
			self.unlog_button = Button(self, text="Un-Log Visit", font="Times 12", \
									command=lambda: self.unlog_visit())
			self.unlog_button.grid()
			self.master.master.show_window("ViewPropertyDetails")

			# self.master.master.show_window("VisitorHomeWindow")

	def unlog_visit(self):
		self.unlog_button.grid_forget()
		self.back_button.grid_forget()

		# remove visitor's rating
		sql = f"DELETE FROM Visit WHERE Username='{self.uname}' AND PropertyID='{self.d['ID']}'"
		self.cursor.execute(sql)

		# update home window
		sql = f"SELECT {ATTRS}, COUNT(Rating), AVG(Rating) FROM Property LEFT OUTER JOIN \
				Visit ON ID=PropertyID GROUP BY Name"
		self.master.master.windows["VisitorHomeWindow"].populate_table(sql)
		
		# update details screen
		sql = f"SELECT COUNT(Username), AVG(Rating) FROM Visit WHERE PropertyID='{self.d['ID']}' \
				AND Username='{self.uname}'"
		self.cursor.execute(sql)
		data = self.cursor.fetchall()
		self.d['Visits'] = data[0][0]
		self.d['Avg Rating'] = data[0][1]		
		self.master.master.windows['ViewPropertyDetails'].grid_forget()
		self.populate(self.d)
		# self.which_screen()
		self.rate_label = Label(self, text="Rate Visit:", font="Times 12")
		self.rate_label.grid()
		self.rate_entry = Entry(self)
		self.rate_entry.insert(0, "1-5")
		self.rate_entry.grid()
		self.log_button = Button(self, text="Log Visit", font="Times 12", \
							command=lambda: self.log_visit(self.rate_entry.get()))
		self.log_button.grid()
		self.master.master.show_window("ViewPropertyDetails")

		# self.master.master.show_window("VisitorHomeWindow")