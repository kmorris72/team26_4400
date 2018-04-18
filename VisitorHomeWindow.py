# Visitor Functionality Window

import MySQLdb as sql
from tkinter import *
from tkinter import ttk
from LoginWindow import LoginWindow
from ViewPropertyDetails import ViewPropertyDetails
'''
TODO
get Visitor ID num and show it on label
Add "View Property" function
Add "View Visit History" function
CURRENTLY DOING
'''

ATTRS = 'Name, ID, Street, Size, City, Zip, PropertyType, IsPublic, IsCommercial'

# This class is the whole window and its functionality
class VisitorHomeWindow(Frame):
	def __init__(self, master, db_cursor):
		Frame.__init__(self, master)

		# a thing to allow access to DB
		self.cursor = db_cursor

		#############
		# FUNCTIONS #
		#############

		# generate table of tuples
		def populate_table(self, sql, tree, search_val):
		
			# remove all info currently in the table
			self.tree.delete(*tree.get_children())

			# How many children deep do we want to put
			# each tuple of the DB? `count` many
			count = 0 
			
			# This `if` runs after the user presses the `go_button`
			# and has chosen to either:
			# else: search by range on Visits or Avg. Rating
			# if: done any other kind of search or sort.
			if search_val == "":
				
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
			
			# User is searching (specifying a range) on Visits or Avg. Rating.
			else:

				# Merge tuples to pair our stats to their property
				data = cursor.fetchall()
				print(data)
				
				for tup in data:
					self.tree.insert('', count, text=tup[0], values=(tup[1], tup[2], tup[3], tup[4], 
								 tup[5], tup[6], tup[7], tup[8], tup[9], tup[10]))
				
					count += 1

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

			return populate_table(self, sql, self.tree, search_val="")

		# sends user to view a property details
		def view_prop_details(self):
			cur_item = self.tree.focus()
			self.master.master.propertyName = self.tree.item(cur_item)['text']

			# pass these as a dict maybe
			self.master.master.app_data = { 'PropertyName' : self.tree.item(cur_item)['text'],
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
			# sql = f"SELECT Owner, Email FROM User INNER JOIN Property ON \
			# 	   Owner=Username WHERE ID='{self.master.master.app_data['ID']}'"
			# self.cursor.execute(sql)
			# owner_deets = self.cursor.fetchall()
			# self.master.master.app_data['Owner'], self.master.master.app_data['Email'] = owner_deets[0][0], owner_deets[0][1]

			# get what the farm has
			# sql = f"SELECT ItemName FROM Has INNER JOIN Property ON \
			# 		ID=PropertyID WHERE ID='{self.master.master.app_data['ID']}'"
			# self.cursor.execute(sql)
			# data = self.cursor.fetchall()
			# self.master.master.app_data['Items'] = [x[0] for x in data]

			# ViewPropertyDetails.update(d)
			self.master.master.show_window("ViewPropertyDetails")

		def logout_go(self):
			self.master.master.show_window("LoginWindow")

		############
		#GUI MAKING#
		############
		
		self.label = Label(self,
						   text="Nice to see you <Visitor ID>",
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
		cols = ['#0', 'ID', 'Street', 'Size', 'City', 'Zip', 
				'Type', 'Public', 'Commercial', 'Visits', 'Avg Rating']	
		for c in cols:
			self.tree.column(f'{c}', width=75)

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

		#############################
		# Buttons. Glorious buttons.#
		#############################

		# View Property button
		self.view_prop_button = Button(self, text="View Selected Property", font="Times 12", \
									   command=lambda: view_prop_details(self))
		self.view_prop_button.pack()

		# View Visit History Button
		self.view_visit_hist_button = Button(self, text="View Visit History", font="Times12")
		self.view_visit_hist_button.pack()

		# Search/Sort By drop down
		# sort_var holds the value of the drop down
		self.sort_var = StringVar(self)

		# default value is Name
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
								command=lambda: sort_search_go(self))
		self.go_button.pack(side=LEFT)

		# logout buttons
		self.logout_button = Button(self, text="Logout", font="Times 12", \
									command=lambda: logout_go(self))
		self.logout_button.pack(side=RIGHT)

		self.sql = f"SELECT {ATTRS}, COUNT(Rating), AVG(Rating) FROM Property LEFT OUTER JOIN \
				Visit ON ID=PropertyID GROUP BY Name"
		populate_table(self, self.sql, self.tree, search_val="")