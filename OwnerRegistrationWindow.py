from tkinter import *


# The amount of padding between each label.
LABEL_PADDING = 2.4

# The options for the property type drop down.
PROP_TYPES = ["Farm", "Orchard", "Garden"]

# The values for "Public?" or "Commercial?".
PUB_COMM_VALUES = ["Yes", "No"]


class OwnerRegistrationWindow:
    def __init__(self, master):
        self.master = master
        master.title("Owner Registration")

        self.welcome_label = Label(master,
                           text="New Owner Registration",
                           font="Times 48")
        self.welcome_label.pack(pady=(0, 20))

        self.text_entry_container = Frame(master)
        self.text_entry_container.pack(pady=(0, 10))

        self.label_container = Frame(self.text_entry_container)
        self.label_container.pack(side=LEFT)

        self.entry_container = Frame(self.text_entry_container)
        self.entry_container.pack(side=RIGHT)

        self.email_label = Label(self.label_container,
                                 text="Email*:",
                                 font="Times 16")
        self.email_label.pack(side=TOP, pady=LABEL_PADDING)
        self.email_text = Entry(self.entry_container,
                                font="Times 16",
                                width=30)
        self.email_text.pack(side=TOP)

        self.username_label = Label(self.label_container,
                                    text="Username*:",
                                    font="Times 16")
        self.username_label.pack(side=TOP, pady=LABEL_PADDING)
        self.username_text = Entry(self.entry_container,
                                   font="Times 16",
                                   width=30)
        self.username_text.pack(side=TOP)

        self.password_label = Label(self.label_container,
                                    text="Password*:",
                                    font="Times 16")
        self.password_label.pack(side=TOP, pady=LABEL_PADDING)
        self.password_text = Entry(self.entry_container,
                                   font="Times 16",
                                   width=30)
        self.password_text.pack(side=TOP)

        self.confirm_password_label = Label(self.label_container,
                                            text="Confirm Password*:",
                                            font="Times 16")
        self.confirm_password_label.pack(side=TOP, pady=LABEL_PADDING)
        self.confirm_password_text = Entry(self.entry_container,
                                           font="Times 16",
                                           width=30)
        self.confirm_password_text.pack(side=TOP)

        self.property_name_label = Label(self.label_container,
                                         text="Property Name*:",
                                         font="Times 16")
        self.property_name_label.pack(side=TOP, pady=LABEL_PADDING)
        self.property_name_text = Entry(self.entry_container,
                                        font="Times 16",
                                        width=30)
        self.property_name_text.pack(side=TOP)

        self.street_address_label = Label(self.label_container,
                                          text="Street Address*:",
                                          font="Times 16")
        self.street_address_label.pack(side=TOP, pady=LABEL_PADDING)
        self.street_address_text = Entry(self.entry_container,
                                         font="Times 16",
                                         width=30)
        self.street_address_text.pack(side=TOP)

        self.city_zip_container = Frame(master)
        self.city_zip_container.pack(pady=(0, 10))

        self.city_label = Label(self.city_zip_container,
                                text="City*:",
                                font="Times 16")
        self.city_label.pack(side=LEFT)
        self.city_text = Entry(self.city_zip_container,
                               font="Times 16",
                               width=10)
        self.city_text.pack(side=LEFT)

        self.zip_label = Label(self.city_zip_container,
                               text="Zip*:",
                               font="Times 16")
        self.zip_label.pack(side=LEFT)
        self.zip_text = Entry(self.city_zip_container,
                              font="Times 16",
                              width=10)
        self.zip_text.pack(side=LEFT)

        self.acres_label = Label(self.city_zip_container,
                                 text="Acres*:",
                                 font="Times 16")
        self.acres_label.pack(side=LEFT)
        self.acres_text = Entry(self.city_zip_container,
                                font="Times 16",
                                width=10)
        self.acres_text.pack(side=LEFT)

        self.drop_down_container = Frame(master)
        self.drop_down_container.pack(pady=(0, 10))

        self.prop_animal_crop_container = Frame(self.drop_down_container)
        self.prop_animal_crop_container.pack(pady=(0, 10))

        self.prop_type_label = Label(self.prop_animal_crop_container,
                                     text="Property Type*:",
                                     font="Times 16")
        self.prop_type_label.pack(side=LEFT)
        
        self.prop_type_var = StringVar(master)
        self.prop_type_var.set(PROP_TYPES[0])
        self.prop_type_drop_down = OptionMenu(self.prop_animal_crop_container,
                                              self.prop_type_var,
                                              *PROP_TYPES)
        self.prop_type_drop_down.pack(side=LEFT)
        self.prop_type_drop_down.bind("<Leave>", self.crop_changed_event_handler)

        self.crop_label = Label(self.prop_animal_crop_container,
                                  text="Crop*:",
                                  font="Times 16")
        self.crop_label.pack(side=LEFT)
        self.crop_var = StringVar(master)
        self.crop_drop_down = OptionMenu(self.prop_animal_crop_container,
                                         self.crop_var,
                                         *PROP_TYPES)
        self.crop_drop_down.pack(side=LEFT)

        self.animal_label = Label(self.prop_animal_crop_container,
                                  text="Animal*:",
                                  font="Times 16")
        self.animal_label.pack(side=LEFT)
        self.animal_var = StringVar(master)
        self.animal_drop_down = OptionMenu(self.prop_animal_crop_container,
                                           self.animal_var,
                                           *PROP_TYPES)
        self.animal_drop_down.pack(side=LEFT)

        self.public_commercial_container = Frame(self.drop_down_container)
        self.public_commercial_container.pack()

        self.public_label = Label(self.public_commercial_container,
                                  text="Public?*:",
                                  font="Times 16")
        self.public_label.pack(side=LEFT)
        self.public_var = StringVar(master)
        self.public_var.set(PUB_COMM_VALUES[0])
        self.public_drop_down = OptionMenu(self.public_commercial_container,
                                           self.public_var,
                                           *PUB_COMM_VALUES)
        self.public_drop_down.pack(side=LEFT)

        self.commercial_label = Label(self.public_commercial_container,
                                      text="Commercial?*:",
                                      font="Times 16")
        self.commercial_label.pack(side=LEFT)
        self.commercial_var = StringVar(master)
        self.commercial_var.set(PUB_COMM_VALUES[1])
        self.commercial_drop_down = OptionMenu(self.public_commercial_container,
                                               self.commercial_var,
                                               *PUB_COMM_VALUES)
        self.commercial_drop_down.pack(side=LEFT)

        self.button_container = Frame(master)
        self.button_container.pack(pady=(0, 30))
        self.reg_button = Button(self.button_container,
                                 text="Register Owner",
                                 padx=10)
        self.reg_button.pack(side=LEFT, padx=(0, 50))
        self.cancel_button = Button(self.button_container,
                                    text="Cancel",
                                    padx=10)
        self.cancel_button.pack(side=RIGHT)


    def crop_changed_event_handler(self, event):
        if (self.prop_type_var.get() != PROP_TYPES[0]):
            self.animal_label.pack_forget()
            self.animal_drop_down.pack_forget()
        else:
            self.animal_label.pack(side=LEFT)
            self.animal_drop_down.pack(side=LEFT)


root = Tk()
my_gui = OwnerRegistrationWindow(root)
root.mainloop()
