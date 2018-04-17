from tkinter import *
from tkinter import ttk
import MySQLdb

class ApprovedCropsWindow:
    def __init__(self, master):
        self.master = master
        master.title("ApprovedCropsWindow")



        self.propertyname = Entry(self.two_container,
                                font="Times 16",
                                width=12)
        self.propertyname.pack()


        self.address = Entry(self.two_container,
                                font="Times 16",
                                width=12)
        self.address.pack()


        self.city = Entry(self.two_container,
                                font="Times 16",
                                width=12)
        self.city.pack()



        self.size = Entry(self.two_container,
                                font="Times 16",
                                width=12)
        self.size.pack()

        self.id = 
        self.crops=ttk.Treeview(self.tablecontainer, 
        	columns = ('Crops');
        	
        	self.crops.pack();


        self.tkvar = StringVar(self.leftside)
         
        self.cropsadd = Entry(self.two_container,
                                font="Times 16",
                                width=12)
        self.cropsadd.pack()


        choices = { 'Type...','Fruit','Animal','Vegetable','Flower'}
        self.tkvar.set('Type...')

        self.submitreques = Button(self.acontainer,
                                   text="Submit Request",
                                   padx=10,
                                   width = 12)
        self.submitreques.pack()


       self.submitchanges = Button(self.acontainer,
                                   text="Save Changes",
                                   padx=10,
                                   width = 12)
        self.submitchanges.pack()

        self.leave = Button(self.acontainer,
                                   text="Go Back (Doesn't Save)",
                                   padx=10,
                                   width = 12)
        self.leave.pack()