from tkinter import *
import tkinter.messagebox as messagebox
import hashlib


class VisitorRegistrationWindow(Frame):
    def __init__(self, master, db_cursor):
        Frame.__init__(self, master)

        self.db_cursor = db_cursor

        self.welcome_label = Label(self,
                           text="New Visitor Registration",
                           font="Times 48")
        self.welcome_label.pack(pady=(0, 30))

        self.text_entry_container = Frame(self)
        self.text_entry_container.pack(pady=(0, 20))

        self.label_container = Frame(self.text_entry_container)
        self.label_container.pack(side=LEFT)

        self.entry_container = Frame(self.text_entry_container)
        self.entry_container.pack(side=RIGHT)

        self.email_label = Label(self.label_container,
                                 text="Email*:",
                                 font="Times 16")
        self.email_label.pack(side=TOP)
        self.email_text = Entry(self.entry_container,
                                font="Times 16",
                                width=30)
        self.email_text.pack(side=TOP)

        self.username_label = Label(self.label_container,
                                    text="Username*:",
                                    font="Times 16")
        self.username_label.pack(side=TOP)
        self.username_text = Entry(self.entry_container,
                                   font="Times 16",
                                   width=30)
        self.username_text.pack(side=TOP)

        self.password_label = Label(self.label_container,
                                    text="Password*:",
                                    font="Times 16")
        self.password_label.pack(side=TOP)
        self.password_text = Entry(self.entry_container,
                                   font="Times 16",
                                   width=30)
        self.password_text.pack(side=TOP)

        self.confirm_password_label = Label(self.label_container,
                                    text="Confirm Password*:",
                                    font="Times 16")
        self.confirm_password_label.pack(side=TOP)
        self.confirm_password_text = Entry(self.entry_container,
                                   font="Times 16",
                                   width=30)
        self.confirm_password_text.pack(side=TOP)

        self.button_container = Frame(self)
        self.button_container.pack(pady=(0, 30))
        self.reg_button = Button(self.button_container,
                                       text="Register Visitor",
                                       padx=10,
                                       command=self.reg_button_clicked_handler)
        self.reg_button.pack(side=LEFT, padx=(0, 50))
        self.cancel_button = Button(self.button_container,
                                         text="Cancel",
                                         padx=10,
                                         command=self.cancel_button_clicked_handler)
        self.cancel_button.pack(side=RIGHT)   


    def reg_button_clicked_handler(self):
        # Check for empty text boxes.
        no_empty_text = True
        for text_box in (self.email_text, self.username_text, self.password_text, self.confirm_password_text):
            if (text_box.get().strip() == ""):
                messagebox.showinfo("Alert", "Please fill out all fields.")
                no_empty_text = False

        # Check that the password and confirm password fields match.
        passwords_match = False
        if (no_empty_text and self.password_text.get() != self.confirm_password_text.get()):
            messagebox.showinfo("Alert", "Please confirm that passwords match.")
        else:
            passwords_match = True

        # Check that the email is not already in the database.
        email = self.email_text.get().strip()
        duplicate_email = False
        email_query = "SELECT * FROM User WHERE Email=\"{}\"".format(email)
        self.db_cursor.execute(email_query)
        if self.db_cursor.fetchall():
            messagebox.showinfo("Alert", "That email is already taken.")
            duplicate_email = True

        # Check that the username is not already in the database.
        username = self.username_text.get().strip()
        duplicate_username = False
        username_query = "SELECT * FROM User WHERE Username=\"{}\"".format(username)
        self.db_cursor.execute(username_query)
        if self.db_cursor.fetchall():
            messagebox.showinfo("Alert", "That username is already taken.")
            duplicate_username = True
        
        # If none of the above conditions were violated, add the user and send them back to the login window.
        if no_empty_text and passwords_match and not duplicate_email and not duplicate_username:
            password = hashlib.md5(self.password_text.get().encode("utf-8")).digest()
            insert_query = "INSERT INTO User VALUES (\"{}\", \"{}\", \"{}\", \"VISITOR\")".format(username, email, password)
            self.db_cursor.execute(insert_query)
            messagebox.showinfo("Alert", "New Visitor Registered! You can now login with the specified email and password.")
            self.clear_text_boxes()
            self.master.master.show_window("LoginWindow")


    def cancel_button_clicked_handler(self):
        self.clear_text_boxes()
        self.master.master.show_window("LoginWindow")


    def clear_text_boxes(self):
        self.email_text.delete(0, END)
        self.username_text.delete(0, END)
        self.password_text.delete(0, END)
        self.confirm_password_text.delete(0, END)
