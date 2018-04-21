from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox


# Column names for the data table. Also serve as possible "search by" terms.
COLUMN_NAMES = ["Username", "Email", "Logged Visits"]


class AdminVisitorOverviewWindow(Frame):
    def __init__(self, master, db_cursor):
        Frame.__init__(self, master)

        self.db_cursor = db_cursor

        self.welcome_label = Label(self,
                           text="All Visitors in System",
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

        self.delete_visitor_button = Button(self.delete_back_button_container,
                                         text="Delete Visitor Account",
                                         padx=10,
                                         command=self.delete_visitor_button_clicked_handler)
        self.delete_visitor_button.pack(pady=(0, 20))

        self.delete_log_button = Button(self.delete_back_button_container,
                                         text="Delete Log History",
                                         padx=10,
                                         command=self.delete_log_button_clicked_handler)
        self.delete_log_button.pack(pady=(0, 20))

        self.back_button = Button(self.delete_back_button_container,
                                  text="Back",
                                  padx=10,
                                  command=self.back_button_clicked_handler)
        self.back_button.pack()

        self.search_container = Frame(self.button_container)
        self.search_container.pack(side=LEFT)

        self.search_container_inner = Frame(self.search_container)
        self.search_container_inner.pack()

        self.search_by_label = Label(self.search_container_inner,
                                     text="Search By:",
                                     font="Times 16")
        self.search_by_label.pack(side=TOP, pady=(0, 2))

        self.search_by_var = StringVar(self)
        self.search_by_var.set(COLUMN_NAMES[0])
        self.search_by_var.trace("w", self.search_by_var_changed_handler)

        self.search_by_drop_down = OptionMenu(self.search_container_inner,
                                              self.search_by_var,
                                              *COLUMN_NAMES)
        self.search_by_drop_down.pack(side=TOP, pady=(0, 10))

        self.search_text = Entry(self.search_container_inner,
                                 font="Times 16",
                                 width=10)
        self.search_text.pack(side=TOP, pady=(0, 10))

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

        self.search_button = Button(self.search_container,
                                    text="Search Visitors",
                                    padx=10,
                                    command=self.search_button_clicked_handler)
        self.search_button.pack(side=TOP)


    def delete_visitor_button_clicked_handler(self):
        should_delete = messagebox.askyesno("Alert", "Do You Really Want to Delete the Selected Visitor?")
        if should_delete:
            table_item = self.table.focus()
            visitor_username = self.table.item(table_item)["values"][0]
            delete_query = """DELETE FROM User
                              WHERE Username=\"{}\"""".format(visitor_username)
            self.db_cursor.execute(delete_query)
            self.table.delete(table_item)
            messagebox.showinfo("Alert", "Deleted Selected Visitor.")
        else:
            messagebox.showinfo("Alert", "Visitor Not Deleted.")


    def delete_log_button_clicked_handler(self):
        should_delete = messagebox.askyesno("Alert", "Do You Really Want to Delete the Selected Visitor's Visit Log?")
        if should_delete:
            table_item = self.table.focus()
            visitor_username = self.table.item(table_item)["values"][0]
            delete_query = """DELETE FROM Visit
                              WHERE Username=\"{}\"""".format(visitor_username)
            self.db_cursor.execute(delete_query)
            messagebox.showinfo("Alert", "Deleted Selected Visitor's Visit Log.")
        else:
            messagebox.showinfo("Alert", "Visit Log Not Deleted.")


    def search_by_var_changed_handler(self, x, y, z):
        if self.search_by_var.get() == COLUMN_NAMES[0] or self.search_by_var.get() == COLUMN_NAMES[1]:
            self.num_visits_search_container.pack_forget()
            self.search_text.pack()
        else:
            self.search_text.pack_forget()
            self.num_visits_search_container.pack()

    
    def search_button_clicked_handler(self):
        search_attr = self.search_by_var.get()
        if search_attr == COLUMN_NAMES[0] or search_attr == COLUMN_NAMES[1]:
            search_val = self.search_text.get()
            self.populate_table("""SELECT U.Username, Email, COUNT(*) 
                                   FROM User AS U LEFT OUTER JOIN Visit as V
                                   ON U.Username=V.Username
                                   WHERE U.UserType="VISITOR" AND U.{}=\"{}\"
                                   GROUP BY U.Username""".format(search_attr, search_val))
        else:
            try:
                lower_bound = int(self.num_visits_range_low_text.get())
                upper_bound = int(self.num_visits_range_high_text.get())
                self.populate_table("""SELECT U.Username, Email, COUNT(*) as VisitCount
                                       FROM User AS U LEFT OUTER JOIN Visit as V
                                       ON U.Username=V.Username
                                       WHERE U.UserType="VISITOR"
                                       GROUP BY U.Username
                                       HAVING VisitCount>={} AND VisitCount<={}""".format(lower_bound, upper_bound))
            except:
                messagebox.showinfo("Alert", "Please Enter Numbers for the Bounds for Logged Visits.")


    def back_button_clicked_handler(self):
        self.master.master.show_window("AdminHomeWindow")


    def populate_table(self, query):
        self.table.delete(*self.table.get_children())
        self.db_cursor.execute(query)
        data = self.db_cursor.fetchall()
        for i in range(len(data)):
            row = (data[i][0], data[i][1], data[i][2])
            self.table.insert("", i, values=row)
            

    def init_populate_table(self):
        self.populate_table("""SELECT U.Username, Email, COUNT(*)
                               FROM User AS U LEFT OUTER JOIN Visit AS V
                               ON U.Username=V.Username
                               WHERE U.UserType="VISITOR"
                               GROUP BY U.Username""")
