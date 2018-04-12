
# Visitor Functionality Window
import MySQLdb as sql
from tkinter import *
from tkinter import ttk


class VisitorHomeWindow():
	def __init__(self, master, cursor):
		self.cursor = cursor
		self.master = master
		master.title("Visitor Home")

		self.label = Label(master,
						   text="Nice to see you <Visitor ID>",
						   font="Times 22")
		self.label.pack()

		self.tree = ttk.Treeview(master,
								 columns=('ID', 'Street', 'Size', 'City', 'Zip', 'Type', 'Public', 'Commercial'))
		self.tree.pack()

		self.tree.displaycolumns = ['ID', 'Street', 'Size', 'City', 'Zip', 'Type', 'Public', 'Commercial']

		cols = ['#0', 'ID', 'Street', 'Size', 'City', 'Zip', 'Type', 'Public', 'Commercial']
		for c in cols:
			self.tree.column('{}'.format(c), width=100)
		self.tree.heading('#0', text='Name')
		self.tree.heading('ID', text='ID')
		self.tree.heading('Street', text='Street')
		self.tree.heading('Size', text='Size')
		self.tree.heading('City', text='City')
		self.tree.heading('Zip', text='Zip')
		self.tree.heading('Type', text='Type')
		self.tree.heading('Public', text='Public')
		self.tree.heading('Commercial', text='Commercial')

		cursor.execute(sql)
		data = cursor.fetchall()
		count = 0 
		for tup in data:
			self.tree.insert('', count, text=tup[0], values=(tup[1], tup[2], tup[3], tup[4], tup[5], tup[6], tup[7], tup[8]))
			count += 1

		self.logout_button = Button(master,
									text="Logout",
									font="Times 12")
		self.logout_button.pack()


db = sql.connect(host="academic-mysql.cc.gatech.edu",
					 user="cs4400_team_26",
					 passwd="YFxUWSqD",
					 db="cs4400_team_26")
cursor = db.cursor()
sql = "SELECT Name, ID, Street, Size, City, Zip, PropertyType, IsPublic, IsCommercial FROM Property"


root = Tk()
gui = VisitorHomeWindow(root, cursor)
root.mainloop()
