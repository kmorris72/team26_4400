from tkinter import *
from tkinter import ttk

class ApprovedCropsWindow:
    def __init__(self, master):
        self.master = master
        master.title("ApprovedCropsWindow")

        self.tablecontainer=Frame(master)
        self.tablecontainer.pack()

        self.label = Label(self.tablecontainer,
                           text="Approved Animals/Crops",
                           font="Times 32")
        self.label.pack()


        self.tree=ttk.Treeview(master, columns=('Name','Type'))
        self.tree.pack()
        self.tree.displaycolumns=("Name","Type")
        self.tree.column("Name", width=100 )
        self.tree.column("Type", width=100)
        self.tree.heading("Name", text="Name")
        self.tree.heading("Type", text="Type")
        self.tree['show'] = 'headings'

        self.two_container=Frame(master)
        self.two_container.pack()






        self.leftside=Frame(self.two_container)
        self.leftside.pack(side=LEFT)


        self.tkvar = StringVar(self.leftside)

        choices = { 'Type...','Fruit','Animal','Vegetable','Flower'}
        self.tkvar.set('Type...')

        self.popupMenu = OptionMenu(self.leftside, self.tkvar, *choices)
        self.popupMenu.pack(pady=5)



        self.entername = Entry(self.leftside,
                                font="Times 16",
                                width=12)
        self.entername.pack()
        self.approve_selection_button = Button(self.leftside,
                                   text="Add to Approved \nList",
                                   padx=20,
                                   pady=5,
                                   height= 3, width = 12)
        self.approve_selection_button.pack(padx=20,pady=5)


        self.tkvar2 = StringVar(self.two_container)

        choices = { 'Search by...','Name',"Type"}
        self.tkvar2.set('Search by...')

        self.popupMenu2 = OptionMenu(self.two_container, self.tkvar2, *choices)
        self.popupMenu2.pack(pady=5)


        self.searchterm = Entry(self.two_container,
                                font="Times 16",
                                width=12)
        self.searchterm.pack()
        self.search_button = Button(self.two_container,
                                   text="Search",
                                   padx=20,
                                   width=12)
        self.search_button.pack(side=RIGHT, padx=20)






        self.button_container = Frame(master)
        self.button_container.pack()


        self.delete_selection_button = Button(self.button_container,
                                       text="Delete Selection",
                                       padx=20)
        self.delete_selection_button.pack(pady=5)
        self.back_button = Button(self.button_container,
                                         text="Back",
                                         padx=10,
                                         width=12)
        self.back_button.pack(pady=5)

root = Tk()
my_gui = ApprovedCropsWindow(root)
root.mainloop()
