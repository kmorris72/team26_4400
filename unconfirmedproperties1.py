from tkinter import *
from tkinter import ttk


# Property types for searching.
PROP_TYPES = ["FARM", "GARDEN", "ORCHARD"]

# Column names for the data table.
COLUMN_NAMES = ["Name", "Address", "City", "Zip", "Size", "Type", "Public", "Commercial",
                "ID", "Owner"]

# The names of the columns that can be used as search terms.
SEARCH_BY = ["Name", "Zip", "Type", "Owner"]

# The attributes of a property as a string (used for queries).
PROP_ATTRS = "ID, Name, Size, IsCommercial, IsPublic, Street, City, Zip, PropertyType, Owner, ApprovedBy"


class AdminViewUnconfirmedPropertiesWindow(Frame):
    def __init__(self, master,db_cursor):

        Frame.__init__(self, master)

        self.db_cursor=db_cursor

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


        self.button_container = Frame(self)
        self.button_container.pack(pady=(0, 30))

        self.sort_container = Frame(self.button_container)
        self.sort_container.pack(side=LEFT, padx=(50, 0))

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
                                  command=self.sort_button_click_handler)
        self.sort_button.pack(side=TOP)

        self.search_container = Frame(self.button_container)
        self.search_container.pack(side=LEFT, padx=(50, 50))

        self.search_button = Button(self.search_container,
                                    text="Search Properties",
                                    padx=10,
                                    command=self.search_button_click_handler)
        self.search_button.pack(side=TOP, pady=(0, 10))

        self.search_by_label = Label(self.search_container,
                                     text="Search By:",
                                     font="Times 16")
        self.search_by_label.pack(side=TOP, pady=(0, 10))

        self.search_by_var = StringVar(self)
        self.search_by_var.set(SEARCH_BY[0])
        self.search_by_var.trace("w", self.search_by_var_changed_handler)

        self.search_by_drop_down = OptionMenu(self.search_container,
                                              self.search_by_var,
                                              *SEARCH_BY)
        self.search_by_drop_down.pack(side=TOP, pady=(0, 10))

        self.search_text = Entry(self.search_container,
                                 font="Times 16",
                                 width=10)
        self.search_text.pack(side=TOP, pady=(0, 10))

        self.search_by_type_var = StringVar(self)
        self.search_by_type_var.set(PROP_TYPES[0])

        self.search_by_type_drop_down = OptionMenu(self.search_container,
                                                   self.search_by_type_var,
                                                   *PROP_TYPES)

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
        search_by_var = self.search_by_var.get()
        if search_by_var == SEARCH_BY[2]:
            self.search_text.pack_forget()
            self.search_by_type_drop_down.pack()
        else:
            self.search_by_type_drop_down.pack_forget()
            self.search_text.pack()


    def sort_button_click_handler(self):
        sort_attr = self.sort_by_var.get()
        if sort_attr == SEARCH_BY[0] or sort_attr == SEARCH_BY[1]:
            self.populate_table("""SELECT {}
                                   FROM Property
                                   ON ID=PropertyID
                                   WHERE ApprovedBy IS NULL
                                   GROUP BY Name
                                   ORDER BY {}""".format(PROP_ATTRS, sort_attr))
        elif sort_attr == SEARCH_BY[2]:
            self.populate_table("""SELECT {}
                                   FROM Property LEFT OUTER JOIN Visit
                                   ON ID=PropertyID
                                   WHERE ApprovedBy IS NULL
                                   GROUP BY Name
                                   ORDER BY FIELD(PropertyType, \"FARM\", \"GARDEN\", \"ORCHARD\")""".format(PROP_ATTRS))
        elif sort_attr == SEARCH_BY[3]:
            self.populate_table("""SELECT {}
                                   FROM Property LEFT OUTER JOIN Visit
                                   ON ID=PropertyID
                                   WHERE ApprovedBy IS  NULL
                                   GROUP BY Name
                                   ORDER BY ApprovedBy""".format(PROP_ATTRS))
        else:
            self.populate_table("""SELECT {}
                                   FROM Property LEFT OUTER JOIN Visit
                                   ON ID=PropertyID
                                   WHERE ApprovedBy IS NULL
                                   GROUP BY Name
                                   ORDER BY AvgRating""".format(PROP_ATTRS))


    def search_button_click_handler(self):
        search_attr = self.search_by_var.get()
        search_val = self.search_text.get().strip()
        if search_attr == SEARCH_BY[0]:
            self.populate_table("""SELECT {}
                                   FROM Property
                                   WHERE ApprovedBy IS NULL AND {}=\"{}\"
                                   GROUP BY Name""".format(PROP_ATTRS, search_attr, search_val))
        elif search_attr == SEARCH_BY[1]:
            self.populate_table("""SELECT {}
                                   FROM Property
                                   WHERE ApprovedBy IS  NULL AND {}={}
                                   GROUP BY Name""".format(PROP_ATTRS, search_attr, search_val))
        elif search_attr == SEARCH_BY[2]:
            self.populate_table("""SELECT {}
                                   FROM Property
                                   WHERE ApprovedBy IS NULL AND PropertyType=\"{}\"
                                   GROUP BY Name""".format(PROP_ATTRS, self.search_by_type_var.get()))
        elif search_attr == SEARCH_BY[3]:
            self.populate_table("""SELECT {}
                                   FROM Property
                                   WHERE ApprovedBy IS NULL AND Owner=\"{}\"
                                   GROUP BY Name""".format(PROP_ATTRS, search_val))



    def manage_prop_button_clicked_handler(self):
        table_item = self.table.focus()
        property_id = self.table.item(table_item)["values"][8]


    def back_button_clicked_handler(self):
        self.master.master.show_window("AdminHomeWindow")


    def populate_table(self, query):
        self.table.delete(*self.table.get_children())
        self.db_cursor.execute(query)
        data = self.db_cursor.fetchall()
        for i in range(len(data)):
            row = (data[i][1], data[i][5], data[i][6], data[i][7], data[i][2], data[i][8], "Yes" if data[i][4] == 1 else "No", "Yes" if data[i][3] == 1 else "No", data[i][0], data[i][10], data[i][11])
            self.table.insert("", i, values=row)


    def init_populate_table(self):
        self.populate_table("""SELECT {}
                               FROM Property
                               WHERE ApprovedBy IS NULL
                               GROUP BY Name""".format(PROP_ATTRS))


root = Tk()
my_gui = unconfirmedpropertieswindow(root)
root.mainloop()
