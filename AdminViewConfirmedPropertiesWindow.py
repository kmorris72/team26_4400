from tkinter import *
from tkinter import ttk


# Column names for the data table.
COLUMN_NAMES = ["Name", "Address", "City", "Zip", "Size", "Type", "Public", "Commercial",
                "ID", "Verified by", "Avg. Rating"]

# The names of the columns that can be used as search terms.
SEARCH_BY = ["Name", "Zip", "Type", "Verified by", "Avg. Rating"]


class AdminViewConfirmedPropertiesWindow(Frame):
    def __init__(self, master, db_cursor):
        Frame.__init__(self, master)

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

        self.search_container = Frame(self.button_container)
        self.search_container.pack(side=LEFT, padx=(50, 50))

        self.search_by_var = StringVar(self)
        self.search_by_var.set(SEARCH_BY[0])

        self.search_by_drop_down = OptionMenu(self.search_container,
                                              self.search_by_var,
                                              *SEARCH_BY)
        self.search_by_drop_down.pack(side=TOP, pady=(0, 10))

        self.search_text = Entry(self.search_container,
                                 font="Times 16",
                                 width=10)
        self.search_text.pack(side=TOP, pady=(0, 10))

        self.search_button = Button(self.search_container,
                                    text="Search Properties",
                                    padx=10)
        self.search_button.pack(side=TOP)

        self.manage_prop_button = Button(self.button_container,
                                         text="Manage Selected Property",
                                         padx=10)
        self.manage_prop_button.pack(side=LEFT, padx=(0, 50))

        self.back_button = Button(self.button_container,
                                  text="Back",
                                  padx=10)
        self.back_button.pack(side=RIGHT, padx=(0, 50))
