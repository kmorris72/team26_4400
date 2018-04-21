from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox

COLUMN_NAMES = ["Name","Type"]

class AdminViewApprovedItemsWindow(Frame):
    def __init__(self, master,db_cursor):
        Frame.__init__(self, master)

        self.db_cursor

        self.tablecontainer=Frame(self)
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

        self.two_container=Frame(self)
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


        self.search_container = Frame(self.two_container)
        self.search_container.pack(side=RIGHT)

        self.search_by_var = StringVar(self)
        self.search_by_var.set(COLUMN_NAMES[0])

        self.search_by_drop_down = OptionMenu(self.search_container,
                                              self.search_by_var,
                                              *COLUMN_NAMES)
        self.search_by_drop_down.pack(side=TOP, pady=(0, 10))

        self.search_text= Entry(self.two_container,
                                font="Times 16",
                                width=12)
        self.search_text.pack()
        self.search_button = Button(self.two_container,
                                   text="Search",
                                   padx=20,
                                   width=12,
                                   command=self.search_button_clicked_handler)
        self.search_button.pack(side=RIGHT, padx=20)






        self.button_container = Frame(self)
        self.button_container.pack()


        self.delete_selection_button = Button(self.button_container,
                                       text="Delete Selection",
                                       padx=20,
                                       command=self.delete_button_clicked_handler)
        self.delete_selection_button.pack(pady=5)
        self.back_button = Button(self.button_container,
                                         text="Back",
                                         padx=10,
                                         width=12,
                                         command=self.back_button_clicked_handler)
        self.back_button.pack(pady=5)


        def delete_button_clicked_handler(self):
        should_delete = messagebox.askyesno("Alert", "Are You Sure You Want to Delete the Selected Item?")
        if should_delete:
            table_item = self.tree.focus()
            item_name = self.tree.item(table_item)["values"][0]
            delete_query = """DELETE FROM FarmItem
                              WHERE Name=\"{}\"""".format(item_name)
            self.db_cursor.execute(delete_query)
            self.tree.delete(table_item)
            messagebox.showinfo("Alert", "The Selected Item Has Been Deleted.")
        else:
            messagebox.showinfo("Alert", "Item Not Deleted.")


        def back_button_clicked_handler(self):
            self.master.master.show_window("LoginWindow")


        def populate_table(self):
            self.tree.delete(*self.tree.get_children())
            query = """SELECT Name, Type
                       FROM FarmItem
                       WHERE IsApproved=0"""
            self.db_cursor.execute(query)
            data = self.db_cursor.fetchall()
            for i in range(len(data)):
                row = (data[i][0], data[i][1])
                self.tree.insert("", i, values=row)

        def search_button_clicked_handler(self):
        search_attr = self.search_by_var.get()
        search_val = self.search_text.get()
        if search_attr == COLUMN_NAMES[0]:
            self.populate_table("""SELECT Name
                               FROM FarmItem
                               WHERE IsApproved=="Yes" AND FarmItem.Name=={}
                               GROUP BY FarmItem.Name""".format(search_attr, search_val))
        elif search_attr == COLUMN_NAMES[1]:
            self.populate_table("""SELECT Type
                               FROM FarmItem
                               WHERE IsApproved=="Yes" AND FarmItem.Type=={}
                               GROUP BY FarmItem.Type""".format(search_val))

root = Tk()
my_gui = ApprovedCropsWindow(root)
root.mainloop()
