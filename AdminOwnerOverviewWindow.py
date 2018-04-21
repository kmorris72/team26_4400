from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox


# Column names for the data table. Also serve as possible "search by" terms.
COLUMN_NAMES = ["Username", "Email", "Number of Properties"]


class AdminOwnerOverviewWindow(Frame):
    def __init__(self, master, db_cursor):
        Frame.__init__(self, master)

        self.db_cursor = db_cursor

        self.welcome_label = Label(self,
                           text="All Owners in System",
                           font="Times 36")
        self.welcome_label.pack(pady=(0, 5))

        self.table = ttk.Treeview(self, columns=tuple(COLUMN_NAMES))
        self.table.pack(pady=(0, 50))
        self.table.displaycolumns = COLUMN_NAMES

        # This line makes the annoying empty first column go away.
        self.table["show"] = "headings"

        for col in COLUMN_NAMES:
            self.table.column(col, width=120)
            self.table.heading(col, text=col)

        self.button_container = Frame(self)
        self.button_container.pack(padx=(50, 50), pady=(0, 30))

        self.delete_back_button_container = Frame(self.button_container)
        self.delete_back_button_container.pack(side=LEFT, padx=(0, 30))

        self.delete_owner_button = Button(self.delete_back_button_container,
                                         text="Delete Owner Account",
                                         padx=10,
                                         command=self.delete_owner_button_clicked_handler)
        self.delete_owner_button.pack(pady=(0, 20))

        self.back_button = Button(self.delete_back_button_container,
                                  text="Back",
                                  padx=10,
                                  command=self.back_button_clicked_handler)
        self.back_button.pack()

        self.search_container = Frame(self.button_container)
        self.search_container.pack(side=LEFT)

        self.search_by_var = StringVar(self)
        self.search_by_var.set(COLUMN_NAMES[0])

        self.search_by_drop_down = OptionMenu(self.search_container,
                                              self.search_by_var,
                                              *COLUMN_NAMES)
        self.search_by_drop_down.pack(side=TOP, pady=(0, 10))

        self.search_text = Entry(self.search_container,
                                 font="Times 16",
                                 width=10)
        self.search_text.pack(side=TOP, pady=(0, 10))

        self.search_button = Button(self.search_container,
                                    text="Search Properties",
                                    padx=10,
                                    command=self.search_button_clicked_handler)
        self.search_button.pack(side=TOP)


    def delete_owner_button_clicked_handler(self):
        should_delete = messagebox.askyesno("Alert", "Do You Really Want to Delete the Selected Owner?")
        if should_delete:
            table_item = self.table.focus()
            owner_username = self.table.item(table_item)["values"][0]
            delete_query = """DELETE FROM User
                              WHERE Username=\"{}\"""".format(owner_username)
            self.db_cursor.execute(delete_query)
            self.table.delete(table_item)
            messagebox.showinfo("Alert", "Deleted Selected Owner.")
        else:
            messagebox.showinfo("Alert", "Owner Not Deleted.")


    def back_button_clicked_handler(self):
        self.master.master.show_window("AdminHomeWindow")


    def search_button_clicked_handler(self):
        search_attr = self.search_by_var.get()
        search_val = self.search_text.get()
        if search_attr == COLUMN_NAMES[0] or search_attr == COLUMN_NAMES[1]:
            self.populate_table("""SELECT Username, Email, COUNT(ID)
                               FROM User AS U LEFT OUTER JOIN Property AS P
                               ON U.Username=P.Owner
                               WHERE U.UserType="OWNER" AND U.{}=\"{}\"
                               GROUP BY U.Username""".format(search_attr, search_val))
        else:
            self.populate_table("""SELECT Username, Email, COUNT(ID) as PropCount
                               FROM User AS U LEFT OUTER JOIN Property AS P
                               ON U.Username=P.Owner
                               WHERE U.UserType="OWNER"
                               GROUP BY U.Username
                               HAVING PropCount={}""".format(search_val))

    
    def populate_table(self, query):
        self.table.delete(*self.table.get_children())
        self.db_cursor.execute(query)
        data = self.db_cursor.fetchall()
        for i in range(len(data)):
            row = (data[i][0], data[i][1], data[i][2])
            self.table.insert("", i, values=row)


    def init_populate_table(self):
        self.populate_table("""SELECT Username, Email, COUNT(ID)
                               FROM User AS U LEFT OUTER JOIN Property AS P
                               ON U.Username=P.Owner
                               WHERE U.UserType="OWNER"
                               GROUP BY U.Username""")
