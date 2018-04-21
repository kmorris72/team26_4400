from tkinter import *
from tkinter import ttk

class OwnerFunctionality :

	 def __init__(self, master):
        self.master = master
        master.title("Welcome!")

 		self.tablecontainer=Frame(master)
        self.tablecontainer.pack()

        self.label = Label(self.tablecontainer,
                           text="Your Properties",
                           font="Times 32")
		

		elf.tree=ttk.Treeview(self.tablecontainer, columns=("Name",'Address','City','Zip','Size','Type','Public','Commercial','ID','isValid','Visits', 'Avg. Rating'))
        self.tree.pack()
        self.tree.displaycolumns=("Name",'Address','City','Zip','Size','Type','Public','Commercial','ID','isValid','Visits', 'Avg. Rating')
        self.tree.column("Name", width=100 )
        self.tree.column('Address', width=100)
        self.tree.column('City', width=100)
        self.tree.column('Zip', width=100)
        self.tree.column('Size', width=100)
        self.tree.column('Type', width=100)
        self.tree.column('Public', width=100)
        self.tree.column('Commercial', width=100)
        self.tree.column('ID', width=100)
        self.tree.column('isValid', width=100)
        self.tree.column('Visits', width=100)
        self.tree.column('Avg. Rating', width=100)
        self.tree.heading("Name", text="Name")
        self.tree.heading("Address", text="Address")
        self.tree.heading("City", text="City")
        self.tree.heading("Zip", text="Zip")
        self.tree.heading("Size", text="Size")
        self.tree.heading("Type", text="Type")
        self.tree.heading("Public", text="Public")
        self.tree.heading("Commercial", text="Commercial")
        self.tree.heading("ID", text="ID")
        self.tree.heading("isValid", text="isValid")
        self.tree.heading("Visits", text="Visits")
        self.tree.heading("Avg. Rating", text="Avg. Rating")
        self.tree['show'] = 'headings'



        self.tkvar2 = StringVar(self.acontainer)
        choices = { 'Search by...',"Name","Size","Owner"}
        self.tkvar2.set('Search by...')

        self.popupMenu2 = OptionMenu(self.tkvar2, *choices)
        self.popupMenu2.pack(pady=5)



 
        self.addprop_button = Button(self.container3bb,
                                   text="Add Property",
                                   padx=10,
                                   height=2,width=12)

        self.addprop_button.pack(side=MIDDLE, pady=(55,10),padx=5)

        self.manprop_button = Button(self.container3bb,
                                   text="Manage Property",
                                   padx=10,
                                   height=2,width=12)

        self.manprop_button.pack(side=MIDDLE, pady=(55,10),padx=5)

        self.viewother_button = Button(self.container3bb,
                                   text="View Other Property",
                                   padx=10,
                                   height=2,width=12)

        self.viewother_button.pack(side=MIDDLE, pady=(55,10),padx=5)

        self.logout = Button(self.container3bb,
                                   text="logout",
                                   padx=10,
                                   height=2,width=12)

        self.logout.pack(side=RIGHT, pady=(55,10),padx=5)


        self.search_label = Label(self.password_container,
                                    text="Search Term:",
                                    font="Times 16")
        self.search_label.pack(side=LEFT)
        self.search_text = Entry(self.password_container,
                                   font="Times 16",
                                   width=30)
        self.search_textß.pack(side=LEFT)

