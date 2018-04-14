# Visitor Functionality Window

import MySQLdb as sql
from tkinter import *
from tkinter import ttk

'''
TODO
get Visitor ID num and show it on label
make the logout button actually logout and return user to login page
add "Sort By" drop down and function
add "Search By" input and function
Add ability to search by visit number range or avg rating range
Add ability to select a property
Add "View Property" button that goes to that propertie's page
Add "View Visit History" and function

CURRENTLY DOING
fixing the search on visits or avg visits
'''

ATTRS = 'Name, ID, Street, Size, City, Zip, PropertyType, IsPublic, IsCommercial'

# This class is the whole window and its functionality
class VisitorHomeWindow():
	def __init__(self, master, cursor):

		# a pointer?thing to allow access to DB
		self.cursor = cursor

		# 'master' should be a Tk() instance
		self.master = master
		master.title("Visitor Home")

		self.label = Label(master,
						   text="Nice to see you <Visitor ID>",
						   font="Times 22")
		# make Tkinter put the widget on the page
		self.label.pack()

		# make column IDs (cid). The "0th" column has a builtin cid "#0"
		self.tree = ttk.Treeview(master,
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
				cursor.execute(sql)

				# retrieve result of our query as tuples
				# Important! Query return vals should be 
				# in the same order as the columns.
				data = cursor.fetchall()

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

		# buttons
		# View Property button
		self.view_prop_button = Button(master, text="View Selected Property", font="Times 12")
		self.view_prop_button.pack()

		# View Visit History Button
		self.view_visit_hist_button = Button(master, text="View Visit History", font="Times12")
		self.view_visit_hist_button.pack()

		# Search/Sort By drop down
		# sort_var holds the value of the drop down
		self.sort_var = StringVar(master)

		# default value is Name
		self.sort_var.set("Name")
		self.sort_by = OptionMenu(master, self.sort_var, "Name", "City", "PropertyType", "Visits", "Avg. Rating")
		self.sort_by.pack(side=LEFT)

		# Search Input
		self.search_entry = Entry(master)
		self.search_entry.insert(0, "Search")
		self.search_entry.pack(side=LEFT)

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
					print(bounds[0], bounds[1])
					ov = "ac"
					if option_val == "Visits":
						ov = "cr"
					sql = f"SELECT {ATTRS}, COUNT(Rating) AS cr, AVG(Rating) AS ar FROM Property INNER JOIN \
							Visit ON ID=PropertyID GROUP BY Name ORDER BY {ov} HAVING {ov} > {bounds[0]}"

					return populate_table(self, sql, self.tree, search_val)
					
				# Searching by any other DB attribute.
				else:
					sql = f"SELECT {ATTRS}, COUNT(Rating), AVG(Rating) FROM Property INNER JOIN \
							Visit ON ID=PropertyID WHERE {option_val} LIKE '%{search_val}%' \
							GROUP BY Name ORDER BY {option_val}"

			# Not sorting by Visits or Avg. Rating and not searching anything.
			# So, sorting by anything other than visits or avg rating.
			elif option_val not in ["Visits", "Avg. Rating"]:
				sql = f"SELECT {ATTRS}, COUNT(Rating), AVG(Rating) FROM Property INNER JOIN \
						Visit ON ID=PropertyID GROUP BY Name ORDER BY {option_val}"

			# Sorting by Avg. Rating
			elif option_val == "Avg. Rating":
				sql = f"SELECT {ATTRS}, COUNT(Rating), AVG(Rating) AS ar FROM Property INNER JOIN \
						Visit ON ID=PropertyID GROUP BY Name ORDER BY ar DESC"
			
			# Sorting by Num Visits
			else:
				sql = f"SELECT {ATTRS}, COUNT(Rating) AS cr, AVG(Rating) FROM Property INNER JOIN \
						Visit ON ID=PropertyID GROUP BY Name ORDER BY cr DESC"

			return populate_table(self, sql, self.tree, search_val="")

		# lambda is necessary to avoid the function being called immediately
		self.go_button = Button(master, text="Sort/Search", 
								command=lambda: sort_search_go(self))
		self.go_button.pack(side=LEFT)

		# logout
		self.logout_button = Button(master,
									text="Logout",
									font="Times 12")
		self.logout_button.pack(side=RIGHT)

		sql = f"SELECT {ATTRS}, COUNT(Rating), AVG(Rating) FROM Property INNER JOIN \
				Visit ON ID=PropertyID GROUP BY Name"
		populate_table(self, sql, self.tree, search_val="")
		
db = sql.connect(host="academic-mysql.cc.gatech.edu",
					 user="cs4400_team_26",
					 passwd="YFxUWSqD",
					 db="cs4400_team_26")

# We give this to the window instance
cursor = db.cursor()

# make Tk instance
root = Tk()

# make VisitorHomeWindow instance
gui = VisitorHomeWindow(root, cursor)

# begin 
root.mainloop()