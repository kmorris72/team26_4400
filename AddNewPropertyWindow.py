#NOTES:
#1. Still need to add definition of username for SQL queries
#2. Should anything be added to distinguish crop types for farms vs orchards in the code?

from tkinter import *
import tkinter.messagebox as messagebox
import MySQLdb as sql

db = sql.connect(host="academic-mysql.cc.gatech.edu",
				user="cs4400_team_26", passwd="YFxUWSqD",
				db="cs4400_team_26")

root = Tk()

# The options for the property type drop down.
PROP_TYPES = ["Farm", "Orchard", "Garden"]
# The values for "Public?" or "Commercial?".
PUB_COMM_VALUES = ["Yes", "No"]
# The two types of farm items.
ITEM_TYPES = ["Crop", "Animal"]

class AddNewPropertyWindow:
	def __init__(self, master):
		self.db_cursor = db.cursor()
		self.master = master
		master.title("Add New Property")

		Label(master, text="Add New Property", font="Times 36"). grid(row=0, columnspan=6)
		
		Label(master, text="Property Name:", font="Times 12").grid(row=1,column=0, sticky=E, padx=0)
		self.propertyName_entry = Entry(master, )#width=40)
		self.propertyName_entry.grid(row=1,column=1, columnspan=5, sticky=W+E)
		
		Label(master, text="Street Address:", font="Times 12").grid(row=2,column=0, sticky=E)
		self.address_entry = Entry(master, )#width=40)
		self.address_entry.grid(row=2,column=1, columnspan=5, sticky=W+E)

		Label(master, text="City:", font="Times 12").grid(row=3, column=0, sticky=E)
		self.city_entry = Entry(master, )#width=15)
		self.city_entry.grid(row=3, column=1, columnspan=2, sticky=W+E)
		
		Label(master, text="Zip:", font="Times 12").grid(row=4, column=0, sticky=E)
		self.zip_entry = Entry(master, )#width=10)
		self.zip_entry.grid(row=4, column=1, columnspan=2, sticky=W+E)

		Label(master, text="Acres:", font="Times 12").grid(row=5, column=0, sticky=E)
		self.acres_entry = Entry(master, )#width=10)
		self.acres_entry.grid(row=5,column=1,columnspan=2, sticky=W+E)

		self.prop_type_var = StringVar(master)
		#self.prop_type_var.set(PROP_TYPES[0])
		self.prop_type_var.trace("w", self.prop_type_changed_event_handler)
		Label(master, text="Property Type:", font="Times 12").grid(row=6, column=0, sticky=E)
		self.propertyType_entry = OptionMenu(master, self.prop_type_var, "Farm", "Garden", "Orchard")
		self.propertyType_entry.grid(row=6, column=1, sticky=W)

		animal_query = "SELECT Name FROM FarmItem WHERE Type=\"Animal\""
		self.animal = StringVar(master)
		self.db_cursor.execute(animal_query)
		animal_list = list(self.db_cursor.fetchall())
		for i in range(len(animal_list)):
			animal_list[i] = animal_list[i][0].strip("{").strip("}").strip()
		Label(master, text="Animal:", font="Times 12").grid(row=6, column=2, sticky=E)
		self.animal_entry = OptionMenu(master, self.animal, *animal_list)#list of animals as strings. can maybe pull from db...
		#self.animal_entry.grid(row=6, column=3, sticky=W)

		crop_query = "SELECT Name FROM FarmItem WHERE Type<>\"Animal\""
		self.db_cursor.execute(crop_query)
		crop_list = list(self.db_cursor.fetchall())
		for i in range(len(crop_list)):
			crop_list[i] = crop_list[i][0].strip("{").strip("}").strip()
		self.crop = StringVar(master)
		Label(master, text="Crop:", font="Times 12").grid(row=6, column=4, sticky=E)
		self.crop_entry = OptionMenu(master, self.crop, *crop_list)#list of crops as strings)
		self.crop_entry.grid(row=6, column=5, sticky=W)

		self.public = StringVar(master)
		Label(master, text="Public?", font="Times 12").grid(row=7, column=0, sticky=E)
		self.public_entry= OptionMenu(master, self.public, "Yes", "No")
		self.public_entry.grid(row=7, column=1, sticky=W)

		self.commercial = StringVar(master)
		Label(master, text="Commerical?", font="Times 12").grid(row=8, column=0, sticky=E)
		self.commercial_entry= OptionMenu(master, self.commercial, "Yes", "No")
		self.commercial_entry.grid(row=8, column=1, sticky=W)

		self.addPropButton = Button(master, text="Add Property",
								command=self.add_prop_event_handler)
		self.addPropButton.grid(row=9,column=1, sticky=W+E,columnspan=4)
		#addPropButton.bind("<Button-1>", self.add_prop_event_handler)

		self.cancelButton = Button(master, text="Cancel",
									command=self.cancel_event_handler)
		self.cancelButton.grid(row=9,column=5, columnspan=1, sticky=W+E)

	def prop_type_changed_event_handler(self, n, m, x):
		if (self.prop_type_var.get() == PROP_TYPES[0]):
			self.animal_entry.grid(row=6, column=3, sticky=W)
			#self.crop_entry.grid_forget()
			#self.crop_entry.grid(row=6, column=5, sticky=W)
		else:
			self.animal_entry.grid_forget()

	def cancel_event_handler(self):
			root.destroy()
	def add_prop_event_handler(self):
		no_empty_text = True 
		for entry in (self.propertyName_entry, self.address_entry, self.city_entry, self.zip_entry, 
			self.acres_entry, self.prop_type_var, self.commercial, self.public):
			if (entry.get().strip()==""):
				messagebox.showinfo("Alert", "Please fill out all fields.")	
				no_empty_text = False
				return
		if self.prop_type_var.get() == PROP_TYPES[1] or self.prop_type_var.get() == PROP_TYPES[2]:
			if (self.crop.get().strip()==""):
				messagebox.showinfo("Alert", "Please fill out all fields.")	
				no_empty_text = False
				return
		if self.prop_type_var.get() == PROP_TYPES[0]:
			if (self.animal.get().strip()==""):
				messagebox.showinfo("Alert", "Please fill out all fields.")	
				no_empty_text = False
				return

		prop_name = self.propertyName_entry.get().strip()
		duplicate_prop_name = False
		prop_name_query = "SELECT * FROM Property WHERE Name=\"{}\"".format(prop_name)
		self.db_cursor.execute(prop_name_query)
		if self.db_cursor.fetchall():
			messagebox.showinfo("Alert", "A property with that name already exists.")
			duplicate_prop_name = True

		prop_size = self.acres_entry.get()
		bad_size = False
		try:
			prop_size = float(prop_size)
		except:
			messagebox.showinfo("Alert", "Please make sure that the number of acres is expressed as a decimal number.")
			bad_size = True
		prop_zip = self.zip_entry.get()
		bad_zip = False
		try:
			prop_zip = int(prop_zip)
		except:
			messagebox.showinfo("Alert", "Please make sure that the zip code is expressed as a non-decimal number.")
			bad_zip = True

		highest_prop_id_query = "SELECT MAX(ID) FROM Property"
		self.db_cursor.execute(highest_prop_id_query)
		prop_id = self.db_cursor.fetchall()[0][0] + 1
		print(prop_id)

		is_commercial = 1 if self.commercial.get() == PUB_COMM_VALUES[0] else 0
		is_public = 1 if self.public.get() == PUB_COMM_VALUES[0] else 0
		prop_street = self.address_entry.get().strip()
		prop_city = self.city_entry.get().strip()
		prop_type = self.prop_type_var.get().upper()
		username = ""
		prop_insert_query = "INSERT INTO Property VALUES ({}, \"{}\", {}, {}, {}, \"{}\", \"{}\", {}, \"{}\", \"{}\", NULL)".format(prop_id, prop_name, prop_size, is_commercial, is_public, prop_street, prop_city, prop_zip, prop_type, username)
		self.db_cursor.execute(prop_insert_query)

		farm_item_name = ""
		if prop_type == PROP_TYPES[0].upper():
			animal_name = self.animal.get()
			animal_insert_query = "INSERT INTO Has VALUES ({}, \"{}\")".format(prop_id, animal_name)
			self.db_cursor.execute(animal_insert_query)
			if self.crop.get().strip() !="":
				crop_name = self.crop_var.get()
				crop_insert_query = "INSERT INTO Has VALUES ({}, \"{}\")".format(prop_id, crop_name)
				self.db_cursor.execute(crop_insert_query)
		else:
			crop_name = self.crop_var.get()
			crop_insert_query = "INSERT INTO Has VALUES ({}, \"{}\")".format(prop_id, crop_name)
			self.db_cursor.execute(crop_insert_query)


my_gui = AddNewPropertyWindow(root)
root.mainloop()
