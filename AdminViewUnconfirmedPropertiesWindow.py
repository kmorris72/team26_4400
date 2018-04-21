from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox


# Property types for searching.
PROP_TYPES = ["FARM", "GARDEN", "ORCHARD"]

# Column names for the data table.
COLUMN_NAMES = ["Name", "Address", "City", "Zip", "Size", "Type", "Public", "Commercial",
                "ID", "Owner"]

# The names of the columns that can be used as search terms.
SEARCH_BY = ["Name", "Size", "Owner"]

# The attributes of a property as a string (used for queries).
PROP_ATTRS = "Name, Street, City, Zip, Size, PropertyType, IsPublic, IsCommercial, ID, Owner"


class AdminViewUnconfirmedPropertiesWindow(Frame):
    def __init__(self, master, db_cursor):

        Frame.__init__(self, master)

        self.db_cursor=db_cursor

        self.tablecontainer=Frame(self)
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

        self.button_container = Frame(self)
        self.button_container.pack(pady=(0, 30))

        self.search_container = Frame(self.button_container)
        self.search_container.pack(side=LEFT, padx=(50, 50))

        self.search_container_inner = Frame(self.search_container)
        self.search_container_inner.pack()

        self.search_by_label = Label(self.search_container_inner,
                                     text="Search By:",
                                     font="Times 16")
        self.search_by_label.pack(side=TOP, pady=(0, 10))

        self.search_by_var = StringVar(self)
        self.search_by_var.set(SEARCH_BY[0])
        self.search_by_var.trace("w", self.search_by_var_changed_handler)

        self.search_by_drop_down = OptionMenu(self.search_container_inner,
                                              self.search_by_var,
                                              *SEARCH_BY)
        self.search_by_drop_down.pack(side=TOP, pady=(0, 10))

        self.search_text = Entry(self.search_container_inner,
                                 font="Times 16",
                                 width=10)
        self.search_text.pack(side=TOP, pady=(0, 10))
        
        self.size_search_container = Frame(self.search_container_inner)

        self.size_search_low_end_label = Label(self.size_search_container,
                                           text="Lower End of Range:",
                                           font="Times 16")
        self.size_search_low_end_label.pack(pady=(0, 10))

        self.size_search_low_end_text = Entry(self.size_search_container,
                                          font="Times 16",
                                          width=10)
        self.size_search_low_end_text.pack(pady=(0, 10))

        self.size_search_high_end_label = Label(self.size_search_container,
                                           text="Higher End of Range:",
                                           font="Times 16")
        self.size_search_high_end_label.pack(pady=(0, 10))

        self.size_search_high_end_text = Entry(self.size_search_container,
                                          font="Times 16",
                                          width=10)
        self.size_search_high_end_text.pack(pady=(0, 10))

        self.search_button = Button(self.search_container,
                                    text="Search Properties",
                                    padx=10,
                                    command=self.search_button_click_handler)
        self.search_button.pack(side=TOP, pady=(10, 10))

        self.manage_prop_button = Button(self.button_container,
                                         text="Manage Selected Property",
                                         padx=10)
        self.manage_prop_button.pack(side=LEFT, padx=(0, 50))

        self.back_button = Button(self.button_container,
                                  text="Back",
                                  padx=10,
                                  command=self.back_button_clicked_handler)
        self.back_button.pack(side=RIGHT, padx=(0, 50))


    def search_by_var_changed_handler(self, x, y, z):
        if self.search_by_var.get() == SEARCH_BY[1]:
            self.search_text.pack_forget()
            self.size_search_container.pack()
        else:
            self.size_search_container.pack_forget()
            self.search_text.pack()


    def search_button_click_handler(self):
        search_attr = self.search_by_var.get()
        search_val = self.search_text.get().strip()
        if search_attr == SEARCH_BY[0]:
            self.populate_table("""SELECT {}
                                   FROM Property
                                   WHERE ApprovedBy IS NULL AND {}=\"{}\"""".format(PROP_ATTRS, search_attr, search_val))
        elif search_attr == SEARCH_BY[1]:
            try:
                lower_bound = float(self.size_search_low_end_text.get())
                upper_bound = float(self.size_search_high_end_text.get())
                self.populate_table("""SELECT {}
                                       FROM Property
                                       WHERE ApprovedBy IS NULL AND Size>={} AND Size<={}""".format(PROP_ATTRS, lower_bound, upper_bound))
            except:
                messagebox.showinfo("Alert", "Please Enter Numbers for the Bounds for the Size.")
        elif search_attr == SEARCH_BY[2]:
            self.populate_table("""SELECT {}
                                   FROM Property
                                   WHERE ApprovedBy IS NULL AND Owner=\"{}\"""".format(PROP_ATTRS, search_val))


    def manage_prop_button_clicked_handler(self):
        table_item = self.tree.focus()
        property_id = self.tree.item(table_item)["values"][8]
        self.master.master.show_window("AdminManagePropertyWindow")


    def back_button_clicked_handler(self):
        self.master.master.show_window("AdminHomeWindow")


    def populate_table(self, query):
        self.tree.delete(*self.tree.get_children())
        self.db_cursor.execute(query)
        data = self.db_cursor.fetchall()
        for i in range(len(data)):
            row = (data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], "Yes" if data[i][6] == 1 else "No", "Yes" if data[i][7] == 1 else "No", data[i][8], data[i][9])
            self.tree.insert("", i, values=row)


    def init_populate_table(self):
        self.populate_table("""SELECT {}
                               FROM Property
                               WHERE ApprovedBy IS NULL""".format(PROP_ATTRS))