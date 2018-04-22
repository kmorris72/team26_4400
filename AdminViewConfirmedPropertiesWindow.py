from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox


# Property types for searching.
PROP_TYPES = ["FARM", "GARDEN", "ORCHARD"]

# Column names for the data table.
COLUMN_NAMES = ["Name", "Address", "City", "Zip", "Size", "Type", "Public", "Commercial",
                "ID", "Verified by", "Avg. Rating"]

# The names of the columns that can be used as search terms.
SEARCH_BY = ["Name", "Zip", "Type", "Verified by", "Avg. Rating"]

# The attributes of a property as a string (used for queries).
PROP_ATTRS = "Name, Street, City, Zip, Size, PropertyType, IsPublic, IsCommercial, ID, ApprovedBy"


class AdminViewConfirmedPropertiesWindow(Frame):
    def __init__(self, master, db_cursor):
        Frame.__init__(self, master)

        self.db_cursor = db_cursor

        self.welcome_label = Label(self,
                           text="Confirmed Properties:",
                           font="Times 36")
        self.welcome_label.pack(pady=(0, 5))

        self.table = ttk.Treeview(self, columns=tuple(COLUMN_NAMES))
        self.table.pack(pady=(0, 50))
        self.table.displaycolumns = COLUMN_NAMES

        # This line makes the annoying empty first column go away.
        self.table["show"] = "headings"

        for col in COLUMN_NAMES:
            self.table.column(col, width=75)
            self.table.heading(col, text=col)

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

        self.search_by_type_var = StringVar(self)
        self.search_by_type_var.set(PROP_TYPES[0])

        self.search_by_type_drop_down = OptionMenu(self.search_container_inner,
                                                   self.search_by_type_var,
                                                   *PROP_TYPES)

        self.avg_rat_container = Frame(self.search_container_inner)

        self.avg_rat_low_end_label = Label(self.avg_rat_container,
                                           text="Lower End of Range:",
                                           font="Times 16")
        self.avg_rat_low_end_label.pack(pady=(0, 10))

        self.avg_rat_low_end_text = Entry(self.avg_rat_container,
                                          font="Times 16",
                                          width=10)
        self.avg_rat_low_end_text.pack(pady=(0, 10))

        self.avg_rat_high_end_label = Label(self.avg_rat_container,
                                           text="Higher End of Range:",
                                           font="Times 16")
        self.avg_rat_high_end_label.pack(pady=(0, 10))

        self.avg_rat_high_end_text = Entry(self.avg_rat_container,
                                          font="Times 16",
                                          width=10)
        self.avg_rat_high_end_text.pack(pady=(0, 10))

        self.search_button = Button(self.search_container,
                                    text="Search Properties",
                                    padx=10,
                                    command=self.search_button_click_handler)
        self.search_button.pack(side=TOP, pady=(10, 10))

        self.manage_prop_button = Button(self.button_container,
                                         text="Manage Selected Property",
                                         padx=10,
                                         command=self.manage_prop_button_clicked_handler)
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
            self.avg_rat_container.pack_forget()
            self.search_by_type_drop_down.pack()
        elif search_by_var == SEARCH_BY[4]:
            self.search_text.pack_forget()
            self.search_by_type_drop_down.pack_forget()
            self.avg_rat_container.pack()
        else:
            self.search_by_type_drop_down.pack_forget()
            self.avg_rat_container.pack_forget()
            self.search_text.pack()


    def sort_button_click_handler(self):
        sort_attr = self.sort_by_var.get()
        if sort_attr == SEARCH_BY[0] or sort_attr == SEARCH_BY[1]:
            self.populate_table("""SELECT {}, ROUND(AVG(Rating), 1) 
                                   FROM Property LEFT OUTER JOIN Visit
                                   ON ID=PropertyID
                                   WHERE IsPublic=1 AND ApprovedBy IS NOT NULL
                                   GROUP BY Name
                                   ORDER BY {}""".format(PROP_ATTRS, sort_attr))
        elif sort_attr == SEARCH_BY[2]:
            self.populate_table("""SELECT {}, ROUND(AVG(Rating), 1)
                                   FROM Property LEFT OUTER JOIN Visit
                                   ON ID=PropertyID
                                   WHERE IsPublic=1 AND ApprovedBy IS NOT NULL
                                   GROUP BY Name
                                   ORDER BY FIELD(PropertyType, \"FARM\", \"GARDEN\", \"ORCHARD\")""".format(PROP_ATTRS))
        elif sort_attr == SEARCH_BY[3]:
            self.populate_table("""SELECT {}, ROUND(AVG(Rating), 1)
                                   FROM Property LEFT OUTER JOIN Visit
                                   ON ID=PropertyID
                                   WHERE IsPublic=1 AND ApprovedBy IS NOT NULL
                                   GROUP BY Name
                                   ORDER BY ApprovedBy""".format(PROP_ATTRS))
        else:
            self.populate_table("""SELECT {}, ROUND(AVG(Rating), 1) AS AvgRating
                                   FROM Property LEFT OUTER JOIN Visit
                                   ON ID=PropertyID 
                                   WHERE IsPublic=1 AND ApprovedBy IS NOT NULL
                                   GROUP BY Name
                                   ORDER BY AvgRating""".format(PROP_ATTRS))


    def search_button_click_handler(self):
        search_attr = self.search_by_var.get()
        search_val = self.search_text.get().strip()
        if search_attr == SEARCH_BY[0]:
            self.populate_table("""SELECT {}, ROUND(AVG(Rating), 1) 
                                   FROM Property LEFT OUTER JOIN Visit
                                   ON ID=PropertyID
                                   WHERE IsPublic=1 AND ApprovedBy IS NOT NULL AND {}=\"{}\"
                                   GROUP BY Name""".format(PROP_ATTRS, search_attr, search_val))
        elif search_attr == SEARCH_BY[1]:
            self.populate_table("""SELECT {}, ROUND(AVG(Rating), 1)
                                   FROM Property LEFT OUTER JOIN Visit
                                   ON ID=PropertyID
                                   WHERE IsPublic=1 AND ApprovedBy IS NOT NULL AND {}={}
                                   GROUP BY Name""".format(PROP_ATTRS, search_attr, search_val))
        elif search_attr == SEARCH_BY[2]:
            self.populate_table("""SELECT {}, ROUND(AVG(Rating), 1)
                                   FROM Property LEFT OUTER JOIN Visit
                                   ON ID=PropertyID
                                   WHERE IsPublic=1 AND ApprovedBy IS NOT NULL AND PropertyType=\"{}\"
                                   GROUP BY Name""".format(PROP_ATTRS, self.search_by_type_var.get()))
        elif search_attr == SEARCH_BY[3]:
            self.populate_table("""SELECT {}, ROUND(AVG(Rating), 1) AS AvgRating
                                   FROM Property LEFT OUTER JOIN Visit
                                   ON ID=PropertyID
                                   WHERE IsPublic=1 AND ApprovedBy IS NOT NULL AND ApprovedBy=\"{}\"
                                   GROUP BY Name""".format(PROP_ATTRS, search_val))
        else:
            try:
                lower_bound = float(self.avg_rat_low_end_text.get())
                upper_bound = float(self.avg_rat_high_end_text.get())
                self.populate_table("""SELECT {}, ROUND(AVG(Rating), 1) AS AvgRating
                                       FROM Property LEFT OUTER JOIN Visit
                                       ON ID=PropertyID 
                                       WHERE IsPublic=1 AND ApprovedBy IS NOT NULL
                                       GROUP BY Name
                                       HAVING AvgRating>={} AND AvgRating<={}""".format(PROP_ATTRS, lower_bound, upper_bound))
            except:
                messagebox.showinfo("Alert", "Please Enter Numbers for the Bounds for the Average Rating.")

    
    def manage_prop_button_clicked_handler(self):
        try:
            table_item = self.table.focus()
            property_id = self.table.item(table_item)["values"][8]
            get_prop_query = """SELECT * FROM Property
                                WHERE ID={}""".format(property_id)
            self.db_cursor.execute(get_prop_query)
            prop = self.db_cursor.fetchall()[0]
            self.master.master.windows["AdminManagePropertyWindow"].fill_in_data_from_prop(prop)
            self.master.master.windows["AdminManagePropertyWindow"].get_approved_animals_and_crops_from_db()
            self.master.master.windows["AdminManagePropertyWindow"].set_previous_window("AdminViewConfirmedPropertiesWindow")
            self.master.master.show_window("AdminManagePropertyWindow")
        except:
            messagebox.showinfo("Alert", "Please Select a Property to Manage From the Table.")

    
    def back_button_clicked_handler(self):
        self.master.master.show_window("AdminHomeWindow")
        

    def populate_table(self, query):
        self.table.delete(*self.table.get_children())
        self.db_cursor.execute(query)
        data = self.db_cursor.fetchall()
        for i in range(len(data)):
            row = (data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], "Yes" if data[i][6] == 1 else "No", "Yes" if data[i][7] == 1 else "No", data[i][8], data[i][9], data[i][10])
            self.table.insert("", i, values=row)
    

    def init_populate_table(self):
        self.populate_table("""SELECT {}, ROUND(AVG(Rating), 1)
                               FROM Property LEFT OUTER JOIN Visit
                               ON ID=PropertyID
                               WHERE IsPublic=1 AND ApprovedBy IS NOT NULL
                               GROUP BY Name""".format(PROP_ATTRS))
