from tkinter import *
from tkinter import ttk

class unconfirmedpropertieswindow:
    def __init__(self, master):
        self.master = master
        master.title("Unconfirmed Properties")

        self.tablecontainer=Frame(master)
        self.tablecontainer.pack()

        self.label = Label(self.tablecontainer,
                           text="Unconfirmed Properties",
                           font="Times 32")
        self.label.pack()



        self.tree=ttk.Treeview(self.tablecontainer, columns=('Name','Address','City','Zip','Size','Type','Public','Commercial','ID',"Owner"))
        self.tree.pack()
        self.tree.displaycolumns=("Name",'Address','City','Zip','Size','Type','Public','Commercial','ID',"Owner")
        self.tree.column("Name", width=100 )
        self.tree.column('Address', width=100)
        self.tree.column('City', width=100)
        self.tree.column('Zip', width=100)
        self.tree.column('Size', width=100)
        self.tree.column('Type', width=100)
        self.tree.column('Public', width=100)
        self.tree.column('Commercial', width=100)
        self.tree.column('ID', width=100)
        self.tree.column("Owner", width=100)
        self.tree.heading("Name", text="Name")
        self.tree.heading("Address", text="Address")
        self.tree.heading("City", text="City")
        self.tree.heading("Zip", text="Zip")
        self.tree.heading("Size", text="Size")
        self.tree.heading("Type", text="Type")
        self.tree.heading("Public", text="Public")
        self.tree.heading("Commercial", text="Commercial")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Owner", text="Owner")
        self.tree['show'] = 'headings'


        self.two_container=Frame(master)
        self.two_container.pack()

        self.acontainer=Frame(self.two_container)
        self.acontainer.pack(side=LEFT, pady=(0,10),padx=5)

        self.tkvar2 = StringVar(self.acontainer)
        choices = { 'Search by...',"Name","Size","Owner"}
        self.tkvar2.set('Search by...')

        self.popupMenu2 = OptionMenu(self.acontainer, self.tkvar2, *choices)
        self.popupMenu2.pack(pady=5)


        self.searchterm = Entry(self.acontainer,
                                font="Times 16",
                                width=12)
        self.searchterm.pack()

        self.search_properties_button = Button(self.acontainer,
                                   text="Search Properties",
                                   padx=10,
                                   width = 12)
        self.search_properties_button.pack()

        self.manage_selected_property_button = Button(self.two_container,
                                   text="Manage Selected \nProperty",
                                   padx=10,
                                   height=2,width=12)
        self.manage_selected_property_button.pack(side=LEFT, pady=(55,10),padx=5)



        self.back_button = Button(self.two_container,
                                       text="Back",
                                       padx=10,
                                       width=12)
        self.back_button.pack(pady=(70,10),padx=5)



        self.two_container=Frame(master)
        self.two_container.pack()


root = Tk()
my_gui = unconfirmedpropertieswindow(root)
root.mainloop()
