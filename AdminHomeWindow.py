from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox


class AdminHomeWindow(Frame):
    def __init__(self, master, db_cursor):
        Frame.__init__(self, master)

        self.db_cursor = db_cursor

        self.label = Label(self,
                           text="Welcome",
                           font="Times 32")
        self.label.pack(pady=(0, 20))

        self.visitors_list_button = Button(self,
                                           text="View Visitors List",
                                           font="Times 16",
                                           padx=10,
                                           pady=5,
                                           command=self.visitors_list_button_clicked_handler)
        self.visitors_list_button.pack(pady=(0, 10))

        self.owners_list_button = Button(self,
                                         text="View Owners List",
                                         font="Times 16",
                                         padx=10,
                                         pady=5,
                                         command=self.owners_list_button_clicked_handler)
        self.owners_list_button.pack(pady=(0, 10))

        self.confirmed_properties_button = Button(self,
                                                  text="View Confirmed Properties",
                                                  font="Times 16",
                                                  padx=10,
                                                  pady=5,
                                                  command=self.confirmed_properties_button_clicked_handler)
        self.confirmed_properties_button.pack(pady=(0, 10))

        self.unconfirmed_properties_button = Button(self,
                                                    text="View Unconfirmed Properties",
                                                    font="Times 16",
                                                    padx=10,
                                                    pady=5,
                                                    command=self.unconfirmed_properties_button_clicked_handler)
        self.unconfirmed_properties_button.pack(pady=(0, 10))

        self.approved_items_button = Button(self,
                                            text="View Approved Animals and Crops",
                                            font="Times 16",
                                            padx=10,
                                            pady=5,
                                            command=self.approved_items_button_clicked_handler)
        self.approved_items_button.pack(padx=(50, 50), pady=(0, 10))

        self.pending_items_button = Button(self,
                                           text="View Pending Animals and Crops",
                                           font="Times 16",
                                           padx=10,
                                           pady=5,
                                           command=self.pending_items_button_clicked_handler)
        self.pending_items_button.pack(pady=(0, 20))

        self.log_out_button = Button(self,
                                     text="Log Out",
                                     font="Times 16",
                                     padx=10,
                                     pady=5,
                                     command=self.log_out_button_clicked_handler)
        self.log_out_button.pack(pady=(0, 10))


    def set_label_text(self):
        self.label.config(text="Welcome {}".format(self.master.master.logged_in_user))


    def visitors_list_button_clicked_handler(self):
        self.master.master.windows["AdminVisitorOverviewWindow"].init_populate_table()
        self.master.master.show_window("AdminVisitorOverviewWindow")


    def owners_list_button_clicked_handler(self):
        self.master.master.windows["AdminOwnerOverviewWindow"].init_populate_table()
        self.master.master.show_window("AdminOwnerOverviewWindow")


    def confirmed_properties_button_clicked_handler(self):
        self.master.master.windows["AdminViewConfirmedPropertiesWindow"].init_populate_table()
        self.master.master.show_window("AdminViewConfirmedPropertiesWindow")


    def unconfirmed_properties_button_clicked_handler(self):
        self.master.master.windows["AdminViewUnconfirmedPropertiesWindow"].init_populate_table()
        self.master.master.show_window("AdminViewUnconfirmedPropertiesWindow")


    def approved_items_button_clicked_handler(self):
        self.master.master.windows["AdminViewApprovedItemsWindow"].init_populate_table()
        self.master.master.show_window("AdminViewApprovedItemsWindow")


    def pending_items_button_clicked_handler(self):
        self.master.master.windows["AdminViewPendingItemsWindow"].populate_table()
        self.master.master.show_window("AdminViewPendingItemsWindow")


    def log_out_button_clicked_handler(self):
        if messagebox.askyesno("Alert", "Are You Sure You Want to Log Out?"):
            self.master.master.show_window("LoginWindow")
