from tkinter import *


class LoginWindow:
    def __init__(self, master):
        self.master = master
        master.title("Login Window")

        self.welcome_label = Label(master,
                           text="ATL Gardens, Farms, and Orchards",
                           font="Times 48")
        self.welcome_label.pack(pady=(0, 30))

        self.email_password_container = Frame(master)
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

        self.login_button = Button(master,
                                   text="Login",
                                   padx=10)
        self.login_button.pack(pady=(0, 30))

        self.reg_button_container = Frame(master)
        self.reg_button_container.pack(pady=(0, 30))
        self.owner_reg_button = Button(self.reg_button_container,
                                       text="New Owner Registration",
                                       padx=10)
        self.owner_reg_button.pack(side=LEFT, padx=(0, 50))
        self.visitor_reg_button = Button(self.reg_button_container,
                                         text="New Visitor Registration",
                                         padx=10)
        self.visitor_reg_button.pack(side=RIGHT)

root = Tk()
my_gui = LoginWindow(root)
root.mainloop()
