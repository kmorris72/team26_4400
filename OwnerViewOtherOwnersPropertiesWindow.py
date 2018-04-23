from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox


# Property types for searching.
PROP_TYPES = ["Yes","No"]

# Column names for the data table.
COLUMN_NAMES = ["Name", "Address", "City", "Zip", "Size", "Type", "Public", "Commercial",
                "ID", "Visits", "Avg. Rating"]

# The names of the columns that can be used as search terms.
SEARCH_BY = ["Name", "City", "IsPublic", "Visits", "Avg. Rating"]

# The attributes of a property as a string (used for queries).
PROP_ATTRS = "Name, Street, City, Zip, Size, PropertyType, IsPublic, IsCommercial, ID"


class OwnerViewOtherOwnersPropertiesWindow(Frame):
    def __init__(self, master, db_cursor):
        Frame.__init__(self, master)

        self.db_cursor = db_cursor

        self.curr_owner = ""

        self.welcome_label = Label(self,
                           text="All Other Valid Properties",
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

        self.num_visits_search_container = Frame(self.search_container_inner)

        self.num_visits_low_label = Label(self.num_visits_search_container,
                                        text="Lower End of Range:",
                                        font="Times 16")
        self.num_visits_low_label.pack()

        self.num_visits_range_low_text = Entry(self.num_visits_search_container,
                                             font="Times 16",
                                             width=10)
        self.num_visits_range_low_text.pack(pady=(0, 10))

        self.num_visits_high_label = Label(self.num_visits_search_container,
                                        text="Higher End of Range:",
                                        font="Times 16")
        self.num_visits_high_label.pack()

        self.num_visits_range_high_text = Entry(self.num_visits_search_container,
                                             font="Times 16",
                                             width=10)
        self.num_visits_range_high_text.pack(pady=(0, 10))


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

        self.view_back_button_container=Frame(self.button_container)
        self.view_back_button_container.pack(side=LEFT)

        self.manage_prop_button = Button(self.view_back_button_container,
                                         text="View Property Details",
                                         padx=10,
                                         command=self.manage_prop_button_clicked_handler)
        self.manage_prop_button.pack(side=TOP, padx=(0, 50))

        self.back_button = Button(self.view_back_button_container,
                                  text="Back",
                                  padx=10,
                                  command=self.back_button_clicked_handler)
        self.back_button.pack(padx=(0, 50))


    def search_by_var_changed_handler(self, x, y, z):
        search_by_var = self.search_by_var.get()
        if search_by_var == SEARCH_BY[2]:
            self.search_text.pack_forget()
            self.avg_rat_container.pack_forget()
            self.num_visits_search_container.pack_forget()
            self.search_by_type_drop_down.pack()
        elif search_by_var == SEARCH_BY[4]:
            self.search_text.pack_forget()
            self.search_by_type_drop_down.pack_forget()
            self.num_visits_search_container.pack_forget()
            self.avg_rat_container.pack()
        elif search_by_var==SEARCH_BY[3]:
            self.search_text.pack_forget()
            self.search_by_type_drop_down.pack_forget()
            self.num_visits_search_container.pack()
        else:
            self.search_by_type_drop_down.pack_forget()
            self.avg_rat_container.pack_forget()
            self.num_visits_search_container.pack_forget()
            self.search_text.pack()


    def sort_button_click_handler(self):
        sort_attr = self.sort_by_var.get()
        if sort_attr == SEARCH_BY[0] or sort_attr == SEARCH_BY[1]:
            self.populate_table("""SELECT {}, COUNT(*), ROUND(AVG(Rating), 1)
                                   FROM Property LEFT OUTER JOIN Visit
                                   ON Owner!=\"{}\" AND ID=PropertyID
                                   WHERE ApprovedBy IS NOT NULL
                                   GROUP BY Name
                                   ORDER BY {}""".format(PROP_ATTRS, self.curr_owner, sort_attr))
        elif sort_attr == SEARCH_BY[2]:
            self.populate_table("""SELECT {}, COUNT(*), ROUND(AVG(Rating), 1)
                                   FROM Property LEFT OUTER JOIN Visit
                                   ON ID=PropertyID
                                   WHERE Owner!=\"{}\" AND ApprovedBy IS NOT NULL
                                   GROUP BY Name
                                   ORDER BY {}""".format(PROP_ATTRS, self.curr_owner, sort_attr))
        elif sort_attr == SEARCH_BY[3]:
            self.populate_table("""SELECT {}, COUNT(*) as TotalVisits, ROUND(AVG(Rating), 1)
                                   FROM Property LEFT OUTER JOIN Visit
                                   ON ID=PropertyID
                                   WHERE Owner!=\"{}\" AND ApprovedBy IS NOT NULL
                                   GROUP BY Name
                                   ORDER BY TotalVisits""".format(PROP_ATTRS, self.curr_owner))
        else:
            self.populate_table("""SELECT {}, COUNT(*), ROUND(AVG(Rating), 1) AS AvgRating
                                   FROM Property LEFT OUTER JOIN Visit
                                   ON ID=PropertyID
                                   WHERE ApprovedBy IS NOT NULL
                                   GROUP BY Name
                                   ORDER BY AvgRating""".format(PROP_ATTRS))


    def search_button_click_handler(self):
        search_attr = self.search_by_var.get()
        search_val = self.search_text.get().strip()
        if search_attr == SEARCH_BY[0]:
            self.populate_table("""SELECT {}, COUNT(*), ROUND(AVG(Rating), 1)
                                   FROM Property LEFT OUTER JOIN Visit
                                   ON ID=PropertyID
                                   WHERE Owner!=\"{}\" AND ApprovedBy IS NOT NULL AND {}=\"{}\"
                                   GROUP BY Name""".format(PROP_ATTRS, self.curr_owner, search_attr, search_val))
        elif search_attr == SEARCH_BY[1]:
            self.populate_table("""SELECT {}, COUNT(*), ROUND(AVG(Rating), 1)
                                   FROM Property LEFT OUTER JOIN Visit
                                   ON ID=PropertyID
                                   WHERE Owner!=\"{}\" AND ApprovedBy IS NOT NULL
                                   GROUP BY Name""".format(PROP_ATTRS, self.curr_owner, search_val))
        elif search_attr == SEARCH_BY[2]:
            self.populate_table("""SELECT {}, COUNT(*), ROUND(AVG(Rating), 1)
                                   FROM Property LEFT OUTER JOIN Visit
                                   ON ID=PropertyID
                                   WHERE Owner!=\"{}\" AND ApprovedBy IS NOT NULL AND IsPublic={}
                                   GROUP BY Name""".format(PROP_ATTRS, self.curr_owner, self.search_by_type_var.get().upper()))
        elif search_attr == SEARCH_BY[3]:
            try:
                lower_bound = int(self.num_visits_range_low_text.get())
                upper_bound = int(self.num_visits_range_high_text.get())
                self.populate_table("""SELECT U.Username, Email, COUNT(Rating) as VisitCount
                                       FROM Property LEFT OUTER JOIN Visit
                                       ON ID=PropertyID
                                       WHERE Owner!=\"{}\" AND ApprovedBy IS NOT NULL
                                       HAVING VisitCount>={} AND VisitCount<={}""".format(PROP_ATTRS,self.curr_owner, lower_bound, upper_bound))
            except:
                messagebox.showinfo("Alert", "Please Enter Numbers for the Bounds for Logged Visits.")



        else:
            try:
                lower_bound = float(self.avg_rat_low_end_text.get())
                upper_bound = float(self.avg_rat_high_end_text.get())
                self.populate_table("""SELECT {}, ROUND(AVG(Rating), 1) AS AvgRating
                                       FROM Property LEFT OUTER JOIN Visit
                                       ON ID=PropertyID
                                       WHERE Owner!=\"{}\" AND ApprovedBy IS NOT NULL
                                       GROUP BY Name
                                       HAVING AvgRating>={} AND AvgRating<={}""".format(PROP_ATTRS, self.curr_owner, lower_bound, upper_bound))
            except:
                messagebox.showinfo("Alert", "Please Enter Numbers for the Bounds for the Average Rating.")


    def manage_prop_button_clicked_handler(self):
        table_item = self.table.focus()
        prop_name = self.table.item(table_item)['values'][0]
        self.master.master.windows["PropertyDetailsWindow"].current_property = prop_name
        self.master.master.windows["PropertyDetailsWindow"].populate()
        property_id = self.table.item(table_item)["values"][8]
        self.master.master.show_window("PropertyDetailsWindow")


    def back_button_clicked_handler(self):
        self.master.master.show_window("OwnerWelcomeWindow")


    def populate_table(self, query):
        self.table.delete(*self.table.get_children())
        self.db_cursor.execute(query)
        data = self.db_cursor.fetchall()
        for i in range(len(data)):
            row = (data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], "Yes" if data[i][6] == 1 else "No", "Yes" if data[i][7] == 1 else "No", data[i][8], data[i][9], data[i][10])
            self.table.insert("", i, values=row)


    def init_populate_table(self):
        self.populate_table("""SELECT {}, COUNT(*), ROUND(AVG(Rating), 1)
                               FROM Property LEFT OUTER JOIN Visit
                               ON ID=PropertyID
                               WHERE OWNER!= \"{}\" AND ApprovedBy IS NOT NULL
                               GROUP BY Name""".format(PROP_ATTRS, self.curr_owner))
