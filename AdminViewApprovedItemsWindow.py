from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox


# The values the user can search by.
SEARCH_BY = ["Name", "Type"]

# The types of items.
ITEM_TYPES = ["Animal", "Fruit", "Nut", "Flower", "Vegetable"]


class AdminViewApprovedItemsWindow(Frame):
    def __init__(self, master, db_cursor):
        Frame.__init__(self, master)

        self.db_cursor = db_cursor

        self.tablecontainer=Frame(self)
        self.tablecontainer.pack()

        self.label = Label(self.tablecontainer,
                           text="Approved Animals/Crops",
                           font="Times 32")
        self.label.pack()

        self.tree=ttk.Treeview(self, columns=('Name','Type'))
        self.tree.pack(pady=(0, 50))
        self.tree.displaycolumns=("Name","Type")
        self.tree.column("Name", width=100 )
        self.tree.column("Type", width=100)
        self.tree.heading("Name", text="Name")
        self.tree.heading("Type", text="Type")
        self.tree['show'] = 'headings'

        self.two_container=Frame(self)
        self.two_container.pack(padx=(30, 30))

        self.leftside = Frame(self.two_container)
        self.leftside.pack(side=LEFT, padx=(0, 50))

        self.add_label = Label(self.leftside,
                               text="Select Item Type You Wish to Add:",
                               font="Times 16")
        self.add_label.pack(pady=(0, 5))

        self.crop_choice_var = StringVar(self.leftside)
        self.crop_choice_var.set(ITEM_TYPES[0])

        self.crop_choice_drop_down = OptionMenu(self.leftside, self.crop_choice_var, *ITEM_TYPES)
        self.crop_choice_drop_down.pack(pady=5)

        self.entername = Entry(self.leftside,
                                font="Times 16",
                                width=12)
        self.entername.pack()

        self.approve_selection_button = Button(self.leftside,
                                   text="Add to Approved \nList",
                                   padx=20,
                                   pady=5,
                                   height= 3, width = 12,
                                   command=self.approve_selection_button_clicked_handler)
        self.approve_selection_button.pack(padx=20,pady=5)

        self.search_container = Frame(self.two_container)
        self.search_container.pack()

        self.search_by_var = StringVar(self.search_container)
        self.search_by_var.set(SEARCH_BY[0])
        self.search_by_var.trace("w", self.search_by_var_changed_handler)

        self.search_by_label = Label(self.search_container,
                                     text="Search by:",
                                     font="Times 16")
        self.search_by_label.pack(pady=(0, 10))

        self.search_by_drop_down = OptionMenu(self.search_container, self.search_by_var, *SEARCH_BY)
        self.search_by_drop_down.pack(pady=(0, 10))

        self.search_term = Entry(self.search_container,
                                font="Times 16",
                                width=12)
        self.search_term.pack()

        self.item_type_var = StringVar(self)
        self.item_type_var.set(ITEM_TYPES[0])

        self.search_item_type_drop_down = OptionMenu(self.search_container,
                                                     self.item_type_var,
                                                     *ITEM_TYPES)

        self.search_button = Button(self.two_container,
                                    text="Search",
                                    font="Times 16",
                                    command=self.search_button_clicked_handler)
        self.search_button.pack(pady=(20, 0))

        self.sort_container = Frame(self.two_container)
        self.sort_container.pack(pady=(20, 30))

        self.sort_by_label = Label(self.sort_container,
                                   text="Sort By:",
                                   font="Times 16")
        self.sort_by_label.pack(side=TOP, pady=(0, 10))

        self.sort_by_var = StringVar(self)
        self.sort_by_var.set(SEARCH_BY[0])

        self.sort_drop_down = OptionMenu(self.sort_container,
                                         self.sort_by_var,
                                         *SEARCH_BY)
        self.sort_drop_down.pack(side=TOP, pady=(0, 10))

        self.sort_button = Button(self.sort_container,
                                  text="Sort Table by Chosen Attribute",
                                  padx=10,
                                  command=self.sort_button_clicked_handler)
        self.sort_button.pack(side=TOP)

        self.button_container = Frame(self)
        self.button_container.pack(pady=(30, 0))

        self.delete_selection_button = Button(self.button_container,
                                       text="Delete Selection",
                                       padx=20,
                                       command=self.delete_selection_button_clicked_handler)
        self.delete_selection_button.pack(pady=5)

        self.back_button = Button(self.button_container,
                                         text="Back",
                                         padx=10,
                                         width=12,
                                         command=self.back_button_clicked_handler)
        self.back_button.pack(pady=5)


    def approve_selection_button_clicked_handler(self):
        should_approve = messagebox.askyesno("Alert", "Are You Sure You Want to Add this New Item?")
        if should_approve:
            item_data = (self.entername.get(), self.crop_choice_var.get().upper())
            approve_query = """INSERT INTO FarmItem
                               VALUES (\"{}\", 1, \"{}\")""".format(item_data[0], item_data[1])
            self.db_cursor.execute(approve_query)
            self.tree.insert("", 0, values=item_data)
            messagebox.showinfo("Alert", "The Item Has Been Added.")
        else:
            messagebox.showinfo("Alert", "Item Not Added.")


    def search_by_var_changed_handler(self, x, y, z):
        if self.search_by_var.get() == SEARCH_BY[0]:
            self.search_item_type_drop_down.pack_forget()
            self.search_term.pack()
        else:
            self.search_term.pack_forget()
            self.search_item_type_drop_down.pack()


    def sort_button_clicked_handler(self):
        sort_attr = self.sort_by_var.get()
        if sort_attr == SEARCH_BY[0]:
            self.populate_table("""SELECT Name, Type
                                   FROM FarmItem
                                   WHERE IsApproved=1
                                   ORDER BY Name""")
        else:
            self.populate_table("""SELECT Name, Type
                                   FROM FarmItem
                                   WHERE IsApproved=1
                                   ORDER BY FIELD(Type, \"ANIMAL\", \"FLOWER\", \"FRUIT\", \"NUT\", \"VEGETABLE\")""")


    def search_button_clicked_handler(self):
        search_attr = self.search_by_var.get()
        if search_attr == SEARCH_BY[0]:
            search_val = self.search_term.get().strip()
            self.populate_table("""SELECT Name, Type
                                   FROM FarmItem
                                   WHERE IsApproved=1 AND {}=\"{}\"""".format(search_attr, search_val))
        elif search_attr == SEARCH_BY[1]:
            search_val = self.item_type_var.get().upper()
            self.populate_table("""SELECT Name, Type
                                   FROM FarmItem
                                   WHERE IsApproved=1 AND {}=\"{}\"""".format(search_attr, search_val.upper()))


    def delete_selection_button_clicked_handler(self):
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
        self.master.master.show_window("AdminHomeWindow")


    def populate_table(self, query):
        self.tree.delete(*self.tree.get_children())
        self.db_cursor.execute(query)
        data = self.db_cursor.fetchall()
        for i in range(len(data)):
            row = (data[i][0], data[i][1])
            self.tree.insert("", i, values=row)

    
    def init_populate_table(self):
        self.populate_table("""SELECT Name, Type
                               FROM FarmItem
                               WHERE IsApproved=1""")
