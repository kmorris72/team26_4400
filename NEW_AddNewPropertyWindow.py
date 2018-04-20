from tkinter import *
import tkinter.messagebox as messagebox
import MySQLdb as sql

db = sql.connect(host="academic-mysql.cc.gatech.edu",
				user="cs4400_team_26", passwd="YFxUWSqD",
				db="cs4400_team_26")
#db_cursor = db.cursor()

root = Tk()

# The amount of padding between each label.
LABEL_PADDING = 2.4

# The options for the property type drop down.
PROP_TYPES = ["Farm", "Orchard", "Garden"]

# The values for "Public?" or "Commercial?".
PUB_COMM_VALUES = ["Yes", "No"]

# The two types of farm items.
ITEM_TYPES = ["Crop", "Animal"]

class AddNewPropertyWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.db_cursor = db.cursor()
        self.fuck_label = Label(self,text="Fuck")
        self.fuck_label.grid()
#        self.add_new_property_label = Label(self,
#        								text="Add New Property",
#        								font="Times 48")
#        self.add_new_property_label.pack(pady=(0,20))


my_gui = AddNewPropertyWindow(root)
root.mainloop()
