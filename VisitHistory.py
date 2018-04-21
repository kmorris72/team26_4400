import MySQLdb as sql
from tkinter import *
from tkinter import ttk

''' TODO
populate table based on data PASSED HERE
'''

ATTRS = 'Street, Size, City, Zip, PropertyType, IsPublic, IsCommercial'

class VisitHistory(Frame):
	def __init__(self, master, db_cursor):
		Frame.__init__(self, master)

		self.cursor = db_cursor
		self.uname = ""

		self.title = Label(self, text="Your Visit History", font="Times 24")
		self.title.pack()

		self.tree = ttk.Treeview(self, columns=("Date Logged", "Rating"))
		self.tree.pack()

		self.tree.displaycolumns = ["Date Logged", "Rating"]
		cols = ["#0", "Date Logged", "Rating"]
		self.tree.column('#0', width=150)
		self.tree.column('Date Logged', width=140)
		self.tree.column('Rating', width=50)

		self.tree.heading("#0", text="Name")
		self.tree.heading("Date Logged", text="Date Logged")
		self.tree.heading("Rating", text="Rating")

		self.view_prop_button = Button(self, text="View Property", command=lambda: self.view_prop_go())
		self.view_prop_button.pack()

		self.back_button = Button(self, text="Back", command=lambda: self.back())
		self.back_button.pack()

	# almost the same as view_prop_details in VisitorHomeWindow
	# which means that this probably doesn't need to be repeated,
	# but ctrl+c ctrl+v baby (these last weeks are kind of hectic)! 
	def view_prop_go(self):
		cur_item = self.tree.focus()
		data = self.tree.item(cur_item)
		property_name = data['text']
		ID = data['values'][2]

		# INNER JOIN would be fine too
		sql = f"SELECT {ATTRS}, COUNT(Rating), AVG(Rating) FROM Property LEFT OUTER JOIN \
				Visit ON ID='{ID}'"
		self.cursor.execute(sql)
		data = self.cursor.fetchone()
		app_data = {'PropertyName': property_name,
					'ID': ID,
					'Address': data[0],
					'Size': data[1],
					'City': data[2],
					'Zip': data[3],
					'PropertyType': data[4],
					'Public': data[5],
					'Commercial': data[6],
					'Visits': data[7],
					'Avg Rating': data[8]}
		
		# get owner name and email
		sql = f"SELECT Owner, Email FROM User INNER JOIN Property ON \
			   Owner=Username WHERE ID='{app_data['ID']}'"
		self.cursor.execute(sql)
		owner_deets = self.cursor.fetchall()
		app_data['Owner'], app_data['Email'] = owner_deets[0][0], owner_deets[0][1]

		# get what the farm has
		sql = f"SELECT ItemName FROM Has INNER JOIN Property ON \
				ID=PropertyID WHERE ID='{app_data['ID']}'"
		self.cursor.execute(sql)
		data = self.cursor.fetchall()
		app_data['Items'] = [x[0] for x in data]

		self.master.master.windows["ViewPropertyDetails"].populate(app_data)
		self.master.master.windows["ViewPropertyDetails"].which_screen()
		self.master.master.windows["ViewPropertyDetails"].from_hist = 1
		self.master.master.show_window("ViewPropertyDetails")

	def back(self):
		# update history
		self.populate()
		self.master.master.show_window("VisitorHomeWindow")

	def populate(self):
		sql = f"SELECT Name, VisitDate, Rating, ID FROM Visit INNER JOIN Property ON PropertyID=ID \
				WHERE Username='{self.uname}' GROUP BY Name"
		# remove all info currently in the table
		self.tree.delete(*self.tree.get_children())

		# How many children deep do we want to put
		# each tuple of the DB? `count` many
		count = 0 
		
		# Pass SQL to MySQL
		self.cursor.execute(sql)

		# retrieve result of our query as tuples
		# Important! Query return vals should be 
		# in the same order as the columns.
		data = self.cursor.fetchall()
		# put our tuple results in the widget. 
		for tup in data:

			# Fill in a row of the table with a tuple's values. 
			self.tree.insert('', count, text=tup[0], values=(tup[1], tup[2], tup[3]))
			
			# Put the next tuple as the child of the one just processed.
			count += 1