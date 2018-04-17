from tkinter import *
import tkinter.messagebox as messagebox


# The amount of padding between each label.
LABEL_PADDING = 2.4

# The options for the property type drop down.
PROP_TYPES = ["Farm", "Orchard", "Garden"]

# The values for "Public?" or "Commercial?".
PUB_COMM_VALUES = ["Yes", "No"]


class OwnerRegistrationWindow(Frame):
    def __init__(self, parent, db_cursor):
        Frame.__init__(self, parent)

        self.db_cursor = db_cursor

        self.welcome_label = Label(self,
                           text="New Owner Registration",
                           font="Times 48")
        self.welcome_label.pack(pady=(0, 20))

        self.text_entry_container = Frame(self)
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

        self.city_zip_container = Frame(self)
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

        self.drop_down_container = Frame(self)
        self.drop_down_container.pack(pady=(0, 10))

        self.prop_animal_crop_container = Frame(self.drop_down_container)
        self.prop_animal_crop_container.pack(pady=(0, 10))

        self.prop_type_label = Label(self.prop_animal_crop_container,
                                     text="Property Type*:",
                                     font="Times 16")
        self.prop_type_label.pack(side=LEFT)
        
        self.prop_type_var = StringVar(self)
        self.prop_type_var.set(PROP_TYPES[0])
        self.prop_type_var.trace("w", self.crop_changed_event_handler)
        self.prop_type_drop_down = OptionMenu(self.prop_animal_crop_container,
                                              self.prop_type_var,
                                              *PROP_TYPES)
        self.prop_type_drop_down.pack(side=LEFT)

        self.crop_label = Label(self.prop_animal_crop_container,
                                  text="Crop*:",
                                  font="Times 16")
        self.crop_label.pack(side=LEFT)
        crop_query = "SELECT Name FROM FarmItem WHERE Type<>\"Animal\""
        self.db_cursor.execute(crop_query)
        crop_list = list(self.db_cursor.fetchall())
        self.crop_var = StringVar(self)
        self.crop_var.set(crop_list[0])
        for i in range(len(crop_list)):
            crop_list[i] = crop_list[i][0].strip("{").strip("}").strip()
        self.crop_drop_down = OptionMenu(self.prop_animal_crop_container,
                                         self.crop_var,
                                         *crop_list)
        self.crop_drop_down.pack(side=LEFT)

        self.animal_label = Label(self.prop_animal_crop_container,
                                  text="Animal*:",
                                  font="Times 16")
        self.animal_label.pack(side=LEFT)
        animal_query = "SELECT Name FROM FarmItem WHERE Type=\"Animal\""
        self.db_cursor.execute(animal_query)
        animal_list = list(self.db_cursor.fetchall())
        self.animal_var = StringVar(self)
        self.animal_var.set(animal_list[0])
        self.animal_drop_down = OptionMenu(self.prop_animal_crop_container,
                                           self.animal_var,
                                           *animal_list)
        self.animal_drop_down.pack(side=LEFT)

        self.public_commercial_container = Frame(self.drop_down_container)
        self.public_commercial_container.pack()

        self.public_label = Label(self.public_commercial_container,
                                  text="Public?*:",
                                  font="Times 16")
        self.public_label.pack(side=LEFT)
        self.public_var = StringVar(self)
        self.public_var.set(PUB_COMM_VALUES[0])
        self.public_drop_down = OptionMenu(self.public_commercial_container,
                                           self.public_var,
                                           *PUB_COMM_VALUES)
        self.public_drop_down.pack(side=LEFT)

        self.commercial_label = Label(self.public_commercial_container,
                                      text="Commercial?*:",
                                      font="Times 16")
        self.commercial_label.pack(side=LEFT)
        self.commercial_var = StringVar(self)
        self.commercial_var.set(PUB_COMM_VALUES[1])
        self.commercial_drop_down = OptionMenu(self.public_commercial_container,
                                               self.commercial_var,
                                               *PUB_COMM_VALUES)
        self.commercial_drop_down.pack(side=LEFT)

        self.button_container = Frame(self)
        self.button_container.pack(pady=(0, 30))
        self.reg_button = Button(self.button_container,
                                 text="Register Owner",
                                 padx=10)
        self.reg_button.pack(side=LEFT, padx=(0, 50))
        self.cancel_button = Button(self.button_container,
                                    text="Cancel",
                                    padx=10,
                                    command=self.cancel_button_clicked_handler)
        self.cancel_button.pack(side=RIGHT)


    def reg_button_clicked_handler(self):
        # Check for empty text boxes.
        no_empty_text = True
        for text_box in (self.email_text, self.username_text, self.password_text, self.confirm_password_text, self.property_name_text, self.street_address_text, self.city_text, self.zip_text, self.acres_text):
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

        # NOT DONE

    
    def cancel_button_clicked_handler(self):
        self.master.master.show_window("LoginWindow")
        self.clear_text_boxes_reset_drop_downs()


    def crop_changed_event_handler(self, n, m, x):
        if (self.prop_type_var.get() != PROP_TYPES[0]):
            self.animal_label.pack_forget()
            self.animal_drop_down.pack_forget()
        else:
            self.animal_label.pack(side=LEFT)
            self.animal_drop_down.pack(side=LEFT)


    def clear_text_boxes_reset_drop_downs(self):
        self.email_text.delete(0, END)
        self.username_text.delete(0, END)
        self.password_text.delete(0, END)
        self.confirm_password_text.delete(0, END)
        self.property_name_text.delete(0, END)
        self.street_address_text.delete(0, END)
        self.city_text.delete(0, END)
        self.zip_text.delete(0, END)
        self.acres_text.delete(0, END)
        self.prop_type_var.set(PROP_TYPES[0])
        self.crop_var.set(self.crop_drop_down["menu"].entrycget(0, "label"))
        self.animal_var.set(self.animal_drop_down["menu"].entrycget(0, "label"))
        self.public_var.set(PUB_COMM_VALUES[0])
        self.commercial_var.set(PUB_COMM_VALUES[1])
