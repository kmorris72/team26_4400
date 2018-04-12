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
'''

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
								 columns=('ID', 'Street', 'Size', 'City', 'Zip', 'Type', 'Public', 'Commercial', 'Visits', 'Avg Rating'))
		self.tree.pack()

		# tell Tkinter 'hey we want to see these'
		self.tree.displaycolumns = ['ID', 'Street', 'Size', 'City', 'Zip', 'Type', 'Public', 'Commercial', 'Visits', 'Avg Rating']

		# set default column width
		cols = ['#0', 'ID', 'Street', 'Size', 'City', 'Zip', 'Type', 'Public', 'Commercial', 'Visits', 'Avg Rating']
		for c in cols:
			self.tree.column(f'{c}', width=75)

		# Fill the column headers with text
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

		# see sql after class declaration
		cursor.execute(sql)

		# retrieve result of our query as tuples
		data = cursor.fetchall()

		# put our tuple results in the widget. 
		# Important! Query return vals should be in the same order as the columns
		count = 0 
		for tup in data:

			# Get the number of visits and their sum for every property
			visit_stats_sql = f"SELECT COUNT(Rating), SUM(Rating) FROM Visit WHERE PropertyID={tup[1]}"
			cursor.execute(visit_stats_sql)
			visit_tup =  cursor.fetchone()

			# avoid dividing by zero when a property has no visits
			try:
				visit_num, visit_avg = visit_tup[0], (visit_tup[1]/visit_tup[0])
			except:
				visit_num, visit_avg = visit_tup[0], "N/A"

			# Fill in a row of the table
			self.tree.insert('', count, text=tup[0], values=(tup[1], tup[2], tup[3], tup[4], tup[5], tup[6], tup[7], tup[8], visit_num, visit_avg))
			count += 1
			
			
		# buttons
		# View Property button
		self.view_prop_button = Button(master, text="View Selected Property", font="Times 12")
		self.view_prop_button.pack()

		# View Visit History Button
		self.view_visit_hist_button = Button(master, text="View Visit History", font="Times12")
		self.view_visit_hist_button.pack()

		# Search/Sort By drop down
		# search_var holds the value of the drop down
		self.search_var = StringVar(master)

		# default value is Name
		self.search_var.set("Name")
		self.search_by = OptionMenu(master, self.search_var, "Name", "City", "Type", "Visits", "Avg. Rating")
		self.search_by.pack(side=LEFT)

		# Search Input
		self.search_entry = Entry(master)
		self.search_entry.insert(0, "Search")
		self.search_entry.pack(side=LEFT)

		# Run the sort/search button
		# Get values to sort and maybe search by
		def sort_search_go(self):
			option_val = self.search_var.get()
			search_val = self.search_entry.get()
			print(option_val, search_val)

		# lambda is necessary to avoid the function being called immediately
		self.go_button = Button(master, text="Sort/Search", command=lambda: sort_search_go(self))
		self.go_button.pack(side=LEFT)

		# logout
		self.logout_button = Button(master,
									text="Logout",
									font="Times 12")
		self.logout_button.pack(side=RIGHT)

		
db = sql.connect(host="academic-mysql.cc.gatech.edu",
					 user="cs4400_team_26",
					 passwd="YFxUWSqD",
					 db="cs4400_team_26")
cursor = db.cursor()
sql = "SELECT Name, ID, Street, Size, City, Zip, PropertyType, IsPublic, IsCommercial FROM Property"

# make Tk instance
root = Tk()

# make VisitorHomeWindow instance
gui = VisitorHomeWindow(root, cursor)

# begin 
root.mainloop()