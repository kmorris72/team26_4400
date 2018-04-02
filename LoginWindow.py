from tkinter import *

class LoginWindow:
    def __init__(self, master):
        self.master = master
        master.title("Login Window")

        self.label = Label(master,
                           text="ATL Gardens, Farms, and Orchards",
                           font="Times 48")
        self.label.pack()

        self.email_container = Frame(master)
        self.email_container.pack()
        self.email_label = Label(self.email_container,
                                 text="Email:",
                                 font="Times 16")
        self.email_label.pack(side=LEFT)
        self.email_text = Entry(self.email_container,
                                font="Times 16",
                                width=30)
        self.email_text.pack(side=LEFT)

        self.password_container = Frame(master)
        self.password_container.pack()
        self.password_label = Label(self.password_container,
                                    text="Password:",
                                    font="Times 16")
        self.password_label.pack(side=LEFT)
        self.password_text = Entry(self.password_container,
                                   font="Times 16",
                                   width=30)
        self.password_text.pack(side=LEFT)

        self.login_button = Button(master,
                                   text="Login",
                                   padx=10)
        self.login_button.pack()

        self.reg_button_container = Frame(master)
        self.reg_button_container.pack()
        self.owner_reg_button = Button(self.reg_button_container,
                                       text="New Owner Registration",
                                       padx=10)
        self.owner_reg_button.pack(side=LEFT)
        self.visitor_reg_button = Button(self.reg_button_container,
                                         text="New Visitor Registration",
                                         padx=10)
        self.visitor_reg_button.pack(side=RIGHT)

root = Tk()
my_gui = LoginWindow(root)
root.mainloop()