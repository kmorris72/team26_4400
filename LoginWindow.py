import MySQLdb as sql
from tkinter import *
import tkinter.messagebox as messagebox
import hashlib


# Types of users. Used to determine which screen to go to next.
USER_TYPES = ["ADMIN", "OWNER", "VISITOR"]

# The attributes of a property as a string (used for queries).
PROP_ATTRS = "ID, Name, Size, IsCommercial, IsPublic, Street, City, Zip, PropertyType, Owner, ApprovedBy"


class LoginWindow(Frame):
    def __init__(self, master, db_cursor):
        Frame.__init__(self, master)

        self.db_cursor = db_cursor

        self.welcome_label = Label(self,
                           text="ATL Gardens, Farms, and Orchards",
                           font="Times 48")
        self.welcome_label.pack(pady=(0, 30))

        self.email_password_container = Frame(self)
        self.email_password_container.pack(pady=(0, 20))

        self.label_container = Frame(self.email_password_container)
        self.label_container.pack(side=LEFT)

        self.text_entry_container = Frame(self.email_password_container)
        self.text_entry_container.pack(side=RIGHT)

        self.email_label = Label(self.label_container,
                                 text="Email:",
                                 font="Times 16")
        self.email_label.pack(side=TOP)
        self.email_text = Entry(self.text_entry_container,
                                font="Times 16",
                                width=30)
        self.email_text.pack(side=TOP)

        self.password_label = Label(self.label_container,
                                    text="Password:",
                                    font="Times 16")
        self.password_label.pack(side=BOTTOM)
        self.password_text = Entry(self.text_entry_container,
                                   font="Times 16",
                                   width=30)
        self.password_text.pack(side=BOTTOM)

        self.login_button = Button(self,
                                   text="Login",
                                   padx=10,
                                   command=self.login_button_click_handler)
        self.login_button.pack(pady=(0, 30))

        self.reg_button_container = Frame(self)
        self.reg_button_container.pack(pady=(0, 30))
        self.owner_reg_button = Button(self.reg_button_container,
                                       text="New Owner Registration",
                                       padx=10,
                                       command=self.owner_reg_button_click_handler)
        self.owner_reg_button.pack(side=LEFT, padx=(0, 50))
        self.visitor_reg_button = Button(self.reg_button_container,
                                         text="New Visitor Registration",
                                         padx=10,
                                         command=self.visitor_reg_button_click_handler)
        self.visitor_reg_button.pack(side=RIGHT)


    def login_button_click_handler(self):
        email = self.email_text.get().strip()
        password = hashlib.md5(self.password_text.get().encode("utf-8")).digest()
        query = """SELECT * FROM User
                   WHERE Email=\"{}\" AND Password=\"{}\"""".format(email, password)
        self.db_cursor.execute(query)
        data = self.db_cursor.fetchall()
        if data:
            self.master.master.logged_in_user = data[0][0]
            user_type = data[0][3]
            if user_type == USER_TYPES[0]:
                self.master.master.windows["AdminHomeWindow"].set_label_text()
                self.master.master.show_window("AdminHomeWindow")
            elif user_type == USER_TYPES[1]:
                self.master.master.show_window("OwnerRegistrationWindow")
            else:
                self.master.master.windows["VisitorHomeWindow"].set_uname(self.email_text.get()) 
                self.master.master.windows["VisitorViewPropertyDetails"].set_uname(self.email_text.get()) 
                self.master.master.show_window("VisitorHomeWindow")
            self.clear_text_boxes()
        else:
            messagebox.showinfo("Alert", "Invalid Email/Password Combination")
            

    def owner_reg_button_click_handler(self):
        self.clear_text_boxes()
        self.master.master.show_window("OwnerRegistrationWindow")


    def visitor_reg_button_click_handler(self):
        self.clear_text_boxes()
        self.master.master.show_window("VisitorRegistrationWindow")


    def clear_text_boxes(self):
        self.email_text.delete(0, END)
        self.password_text.delete(0, END)
