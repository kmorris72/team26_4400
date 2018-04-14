from tkinter import *
from tkinter import ttk

class PendingCropsWindow:
    def __init__(self, master):
        self.master = master
        master.title("PendingCropsWindow")

        self.tablecontainer=Frame(master)
        self.tablecontainer.pack()

        self.label = Label(self.tablecontainer,
                           text="Pending Approval Animals/Crops",
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

        self.button_container = Frame(master)
        self.button_container.pack(pady=40 , padx = 20)

        self.approve_selection_button = Button(self.button_container,
                                   text="Approve \nSelection",
                                   padx=10,
                                   height = 2, width = 12)
        self.approve_selection_button.pack(pady = 5, padx = 10)


        self.delete_selection_button = Button(self.button_container,
                                       text="Delete Selection",
                                       padx=10)
        self.delete_selection_button.pack(pady = 5, padx = 10)
        self.back_button = Button(self.button_container,
                                         text="Back",
                                         padx=10,
                                         width=12)
        self.back_button.pack(pady = 5, padx = 5)

root = Tk()
my_gui = PendingCropsWindow(root)
root.mainloop()
