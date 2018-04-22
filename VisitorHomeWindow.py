# Visitor Functionality Window

import MySQLdb as sql
from tkinter import *
from tkinter import ttk
from LoginWindow import LoginWindow
from VisitorViewPropertyDetails import VisitorViewPropertyDetails
'''
TODO
move functions out of __init__
'''

ATTRS = 'Name, ID, Street, Size, City, Zip, PropertyType, IsPublic, IsCommercial'

# This class is the whole window and its functionality
class VisitorHomeWindow(Frame):
	def __init__(self, master, db_cursor):
		Frame.__init__(self, master)

		# a thing to allow access to DB
		self.cursor = db_cursor

		self.uname = ""
		############
		#GUI MAKING#
		############
		
		self.label = Label(self,
						   text="",
						   font="Times 22")

		# make Tkinter put the widget on the page
		self.label.pack()

		# Time to make a "Table" with Treeview
		# make column IDs (cid). The "0th" column has a builtin cid "#0"
		self.tree = ttk.Treeview(self,
		columns=('ID', 'Street', 'Size', 'City', 'Zip', 
			     'Type', 'Public', 'Commercial', 'Visits', 'Avg Rating'))
		self.tree.pack()

		# tell Tkinter 'hey we want to see these'
		self.tree.displaycolumns = ['ID', 'Street', 'Size', 'City', 'Zip', 
									'Type', 'Public', 'Commercial', 'Visits', 'Avg Rating']

		# set default column width
		self.tree.column('#0', width=150)
		self.tree.column('ID', width=10)
		self.tree.column('Street', width=150)
		self.tree.column('Size', width=50)
		self.tree.column('City', width=70)
		self.tree.column('Zip', width=50)
		self.tree.column('Type', width=70)
		self.tree.column('Public', width=50)
		self.tree.column('Commercial', width=60)
		self.tree.column('Visits', width=50)
		self.tree.column('Avg Rating', width=100)

		# Fill the column headers with text.
		# there's probably a better way to do this.
		self.tree.heading('#0', text='Name')
		self.tree.heading('ID', text='ID')
		self.tree.heading('Street', text='Street')
		self.tree.heading('Size', text='Size')
		self.tree.heading('City', text='City')
		self.tree.heading('Zip', text='Zip')
		self.tree.heading('Type', text='Type')
		self.tree.heading('Public', text='Public')
		self.tree.heading('Commercial', text='Commercial')
		self.tree.heading('Visits', text='Visits')
		self.tree.heading('Avg Rating', text='Avg Rating')

		# View Property button
		self.view_prop_button = Button(self, text="View Selected Property", font="Times 12", \
									   command=lambda: self.view_prop_details())
		self.view_prop_button.pack()

		# View Visit History Button
		self.view_visit_hist_button = Button(self, text="View Visit History", font="Times12", \
											 command=lambda: self.visit_hist_go())
		self.view_visit_hist_button.pack()

		# Search/Sort By drop down
		# sort_var holds the value of the drop down
		self.sort_var = StringVar(self)

		# default sort value is Name
		self.sort_var.set("Name")
		self.sort_by = OptionMenu(self, self.sort_var, "Name", "City", "PropertyType", "Visits", "Avg. Rating")
		self.sort_by.pack(side=LEFT)

		# Search Input
		self.search_entry = Entry(self)
		self.search_entry.insert(0, "Search")
		self.search_entry.pack(side=LEFT)

		# Run a sort or search button
		# lambda is necessary to avoid the function being called immediately
		self.go_button = Button(self, text="Sort/Search", 
								command=lambda: self.sort_search_go())
		self.go_button.pack(side=LEFT)

		# logout buttons
		self.logout_button = Button(self, text="Logout", font="Times 12", \
									command=lambda: self.logout_go())
		self.logout_button.pack(side=RIGHT)

		self.sql = f"SELECT {ATTRS}, COUNT(Rating), AVG(Rating) FROM Property LEFT OUTER JOIN \
				Visit ON ID=PropertyID GROUP BY Name"
		self.populate_table(self.sql)

##################################
# PUTTING THE 'FUN' IN FUNCTIONS #
##################################

	# Run the sort/search button
	# Get values to sort and maybe search by
	def sort_search_go(self):

		# Value of the dropdown sort by menu
		option_val = self.sort_var.get()

		# This is the value of the `search_entry` entry box.
		search_val = self.search_entry.get()
		sql = ""

		# User is specifying a search (`SELECT A FROM R WHERE B LIKE` query)
		if search_val not in  ["", "Search"]:
		
			# Searching by Visits or Avg. Rating
			if option_val in ["Visits", "Avg. Rating"]:
				bounds = search_val.split(",")

				# used as an alias in SQL
				ov = "ar"
				if option_val == "Visits":
					ov = "cr"

				sql = f"SELECT {ATTRS}, COUNT(Rating) AS cr, AVG(Rating) AS ar FROM Property LEFT OUTER JOIN \
						Visit ON ID=PropertyID GROUP BY Name HAVING ({ov} > '{bounds[0]}' AND \
						{ov} < '{bounds[1]}') ORDER BY {ov} DESC"
				
			# Searching by any other DB attribute.
			else:
				sql = f"SELECT {ATTRS}, COUNT(Rating), AVG(Rating) FROM Property LEFT OUTER JOIN \
						Visit ON ID=PropertyID WHERE {option_val} LIKE '%{search_val}%' \
						GROUP BY Name ORDER BY {option_val}"


		# Not sorting by Visits or Avg. Rating and not searching anything.
		# So, sorting by anything other than visits or avg rating.
		elif option_val not in ["Visits", "Avg. Rating"]:
			sql = f"SELECT {ATTRS}, COUNT(Rating), AVG(Rating) FROM Property LEFT OUTER JOIN \
					Visit ON ID=PropertyID GROUP BY Name ORDER BY {option_val}"

		# Sorting by Avg. Rating
		elif option_val == "Avg. Rating":
			sql = f"SELECT {ATTRS}, COUNT(Rating), AVG(Rating) AS ar FROM Property LEFT OUTER JOIN \
					Visit ON ID=PropertyID GROUP BY Name ORDER BY ar DESC"
		
		# Sorting by Num Visits
		else:
			sql = f"SELECT {ATTRS}, COUNT(Rating) AS cr, AVG(Rating) FROM Property LEFT OUTER JOIN \
					Visit ON ID=PropertyID GROUP BY Name ORDER BY cr DESC"

		return self.populate_table(sql)

	# passed by LoginWindow
	def set_uname(self, data):
		self.uname = data

	# generate table of tuples
	def populate_table(self, sql):
	
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
			self.tree.insert('', count, text=tup[0], values=(tup[1], tup[2], tup[3], tup[4], 
							 tup[5], tup[6], tup[7], tup[8], tup[9], tup[10]))
			
			# Put the next tuple as the child of the one just processed.
			count += 1

	# sends user to view a property details
	def view_prop_details(self):
		cur_item = self.tree.focus()

		app_data = { 'PropertyName' : self.tree.item(cur_item)['text'],
					'ID' : self.tree.item(cur_item)['values'][0],
					'Address' : self.tree.item(cur_item)['values'][1],
					'Size' : self.tree.item(cur_item)['values'][2],
					'City' : self.tree.item(cur_item)['values'][3],
					'Zip' : self.tree.item(cur_item)['values'][4],
					'PropertyType' : self.tree.item(cur_item)['values'][5],
					'Public' : self.tree.item(cur_item)['values'][6],
					'Commercial' : self.tree.item(cur_item)['values'][7],
					'Visits' : self.tree.item(cur_item)['values'][8],
					'Avg Rating' : self.tree.item(cur_item)['values'][9],
		}

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

		#print(app_data)
		self.master.master.windows["VisitorViewPropertyDetails"].populate(app_data)
		self.master.master.windows["VisitorViewPropertyDetails"].which_screen()
		self.master.master.show_window("VisitorViewPropertyDetails")

	def logout_go(self):
		self.master.master.show_window("LoginWindow")

	def visit_hist_go(self):
		# print(self.uname) 
		self.master.master.windows["VisitHistory"].uname = self.uname
		self.master.master.windows["VisitHistory"].populate()
		self.master.master.show_window("VisitHistory")

	def set_welcome(self, uname):
		self.uname = uname
		self.label.config(text=f"Nice to see you {self.uname}")