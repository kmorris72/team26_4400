# Visitor View Property Details 

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
interfacing with VisitorHome.py and App.py
'''

class ViewPropertyDetails(Frame):
	def __init__(self, master, cursor):
		Frame.__init__(self, master)

		self.cursor = db.cursor()

		##############
		# GUI MAKING #
		##############

		self.master = master
		master.title("<Property> Details")

		# Labels
		self.label = Label(master, text="<Property> Details", font="Times 24")
		self.label.grid(row=0, column=1)

		self.name_label = Label(master, text="Name: ", font="Times 12")
		self.name_label.grid(row=1, column=0)

		self.owner_label = Label(master, text="Owner: ", font="Times 12")
		self.owner_label.grid(row=2, column=0)

		self.owner_email_laebl = Label(master, text="Owner Email: ", font="Times 12")
		self.owner_email_laebl.grid(row=3, column=0)

		self.visits_label = Label(master, text="Visits: ", font="Times 12")
		self.visits_label.grid(row=4, column=0)

		self.addr_label = Label(master, text="Address: ", font="Times 12")
		self.addr_label.grid(row=5, column=0)

		self.city_label = Label(master, text="City: ", font="Times 12")
		self.addr_label.grid(row=6, column=0)

		self.zip_label = Label(master, text="Zip: ", font="Times 12")
		self.zip_label.grid(row=7, column=0)

		self.size_label = Label(master, text="Size (Acres): ", font="Times 12")
		self.size_label.grid(row=8, column=0)

		self.avg_rating_label = Label(master, text="Avg. Rating: ", font="Times 12")
		self.avg_rating_label.grid(row=9, column=0)

		self.type_label = Label(master, text="Type: ", font="Times 12")
		self.type_label.grid(row=10, column=0)

		self.public_label = Label(master, text="Public: ", font="Times 12")
		self.public_label.grid(row=11, column=0)

		self.commercial_label = Label(master, text="Commercial: ", font="Times 12")
		self.commercial_label.grid(row=12, column=0)

		self.id_label = Label(master, text="ID: ", font="Times 12")
		self.id_label.grid(row=13, column=0)

		self.has_label = Label(master, text="Has: ", font="Times 12")
		self.has_label.grid(row=14, column=0)

		# TODO
		# Add if block to show the correct screen
		# Rating UI
		self.rate_label = Label(master, text="Rate Visit: ", font="Times 12")
		self.rate_label.grid(row=16, column=0)

		self.rate_entry = Entry(master)
		self.rate_entry.insert(0, "1-5")
		self.rate_entry.grid(row=16, column=1)

		# Buttons
		self.log_button = Button(master, text="Log Visit", font="Times 12", \
					command=lambda: print("Still gotta make this log visits"))
		self.log_button.grid(row=17, column=1)

		self.unlog_button = Button(master, text="Un-Log Visit", font="Times 12", \
					command=lambda: print("Still gotta make this unlog visits"))
		self.unlog_button.grid(row=18, column=1)

		self.back_button = Button(master, text="Back", font="Times 12", \
					command=lambda: print("Still got to make this go back"))
		self.back_button.grid(row=19, column=1)

		

# everyone get your database before class can begin
db = sql.connect(host="academic-mysql.cc.gatech.edu",
					 user="cs4400_team_26",
					 passwd="YFxUWSqD",
					 db="cs4400_team_26")

# We give this to the window instance
cursor = db.cursor()

# make Tk instance
root = Tk()

# make VisitorHomeWindow instance
gui = ViewPropertyDetails(root, cursor)
# begin 
root.mainloop()