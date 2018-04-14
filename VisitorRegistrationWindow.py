from tkinter import *


class VisitorRegistrationWindow(Frame):
    def __init__(self, master, db_cursor):
        Frame.__init__(self, master)

        self.master = master
        # master.title("Visitor Registration")

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
        self.username_label.pack(side=BOTTOM)
        self.username_text = Entry(self.entry_container,
                                   font="Times 16",
                                   width=30)
        self.username_text.pack(side=BOTTOM)

        self.password_label = Label(self.label_container,
                                    text="Password*:",
                                    font="Times 16")
        self.password_label.pack(side=BOTTOM)
        self.password_text = Entry(self.entry_container,
                                   font="Times 16",
                                   width=30)
        self.password_text.pack(side=BOTTOM)

        self.confirm_password_label = Label(self.label_container,
                                    text="Confirm Password*:",
                                    font="Times 16")
        self.confirm_password_label.pack(side=BOTTOM)
        self.confirm_password_text = Entry(self.entry_container,
                                   font="Times 16",
                                   width=30)
        self.confirm_password_text.pack(side=BOTTOM)

        self.button_container = Frame(self)
        self.button_container.pack(pady=(0, 30))
        self.reg_button = Button(self.button_container,
                                       text="Register Visitor",
                                       padx=10)
        self.reg_button.pack(side=LEFT, padx=(0, 50))
        self.cancel_button = Button(self.button_container,
                                         text="Cancel",
                                         padx=10)
        self.cancel_button.pack(side=RIGHT)
