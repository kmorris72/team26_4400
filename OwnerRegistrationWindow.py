from tkinter import *
import tkinter.messagebox as messagebox
import hashlib


# The amount of padding between each label.
LABEL_PADDING = 2.4

# The options for the property type drop down.
PROP_TYPES = ["Farm", "Orchard", "Garden"]

# The values for "Public?" or "Commercial?".
PUB_COMM_VALUES = ["Yes", "No"]

# The two types of farm items.
ITEM_TYPES = ["Crop", "Animal"]


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
        self.prop_type_var.trace("w", self.prop_type_changed_event_handler)
        
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
        for i in range(len(crop_list)):
            crop_list[i] = crop_list[i][0].strip("{").strip("}").strip()
        self.crop_var = StringVar(self)
        self.crop_var.set(crop_list[0])
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
        for i in range(len(animal_list)):
            animal_list[i] = animal_list[i][0].strip("{").strip("}").strip()
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

        # Allows the user to select whether they want to have an animal or crop (if their property is a farm).
        self.item_type_label = Label(self.public_commercial_container,
                                     text="Item Type*:",
                                     font="Times 16")
        self.item_type_label.pack(side=LEFT)
        self.item_type_var = StringVar(self)
        self.item_type_var.set(ITEM_TYPES[0])
        self.item_type_drop_down = OptionMenu(self.public_commercial_container,
                                              self.item_type_var,
                                              *ITEM_TYPES)
        self.item_type_drop_down.pack(side=LEFT)

        self.button_container = Frame(self)
        self.button_container.pack(pady=(0, 30))
        self.reg_button = Button(self.button_container,
                                 text="Register Owner",
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

        # Check that the property name is not already being used.
        prop_name = self.property_name_text.get().strip()
        duplicate_prop_name = False
        prop_name_query = "SELECT * FROM Property WHERE Name=\"{}\"".format(prop_name)
        self.db_cursor.execute(prop_name_query)
        if self.db_cursor.fetchall():
            messagebox.showinfo("Alert", "A property with that name already exists.")
            duplicate_prop_name = True

        # Check that property size is a float.
        prop_size = self.acres_text.get()
        bad_size = False
        try:
            prop_size = float(prop_size)
        except:
            messagebox.showinfo("Alert", "Please make sure that the number of acres is expressed as a decimal number.")
            bad_size = True
        
        # Check that property zip is an int.
        prop_zip = self.zip_text.get()
        bad_zip = False
        try:
            prop_zip = int(prop_zip)
        except:
            messagebox.showinfo("Alert", "Please make sure that the zip code is expressed as a non-decimal number.")
            bad_zip = True

        # If none of the above conditions were violated, add the user, their property, and their item and send them back to the login window.
        if no_empty_text and passwords_match and not duplicate_email and not duplicate_username and not duplicate_prop_name and not bad_size and not bad_zip:
            password = hashlib.md5(self.password_text.get().encode("utf-8")).digest()
            user_insert_query = "INSERT INTO User VALUES (\"{}\", \"{}\", \"{}\", \"OWNER\")".format(username, email, password)
            self.db_cursor.execute(user_insert_query)

            highest_prop_id_query = "SELECT MAX(ID) FROM Property"
            self.db_cursor.execute(highest_prop_id_query)
            prop_id = self.db_cursor.fetchall()[0][0] + 1

            is_commercial = 1 if self.commercial_var.get() == PUB_COMM_VALUES[0] else 0
            is_public = 1 if self.public_var.get() == PUB_COMM_VALUES[0] else 0
            prop_street = self.street_address_text.get().strip()
            prop_city = self.city_text.get().strip()
            prop_type = self.prop_type_var.get().upper()
            prop_insert_query = "INSERT INTO Property VALUES ({}, \"{}\", {}, {}, {}, \"{}\", \"{}\", {}, \"{}\", \"{}\", NULL)".format(prop_id, prop_name, prop_size, is_commercial, is_public, prop_street, prop_city, prop_zip, prop_type, username)
            self.db_cursor.execute(prop_insert_query)

            farm_item_name = ""
            if prop_type == PROP_TYPES[0].upper():
                if self.item_type_var.get() == ITEM_TYPES[0]:
                    farm_item_name = self.crop_var.get()
                else:
                    farm_item_name = self.animal_var.get()
            else:
                farm_item_name = self.crop_var.get()
            has_insert_query = "INSERT INTO Has VALUES ({}, \"{}\")".format(prop_id, farm_item_name)
            self.db_cursor.execute(has_insert_query)

            messagebox.showinfo("Alert", "New Owner Registered! You can now login with the specified email and password.")
            self.clear_text_boxes_reset_drop_downs()
            self.master.master.show_window("LoginWindow")

    
    def cancel_button_clicked_handler(self):
        self.master.master.show_window("LoginWindow")
        self.clear_text_boxes_reset_drop_downs()


    def prop_type_changed_event_handler(self, n, m, x):
        if (self.prop_type_var.get() != PROP_TYPES[0]):
            self.animal_label.pack_forget()
            self.animal_drop_down.pack_forget()
            self.item_type_label.pack_forget()
            self.item_type_drop_down.pack_forget()
            
            crop_menu = self.crop_drop_down["menu"]
            crop_menu.delete(0, END)
            get_crop_query = ""
            if self.prop_type_var.get() == PROP_TYPES[1]:
                get_crop_query = """SELECT Name FROM FarmItem
                                    WHERE (Type=\"FRUIT\" OR Type=\"NUT\") AND IsApproved=1"""
            else:
                get_crop_query = """SELECT Name FROM FarmItem
                                    WHERE (Type=\"VEGETABLE\" OR Type=\"FLOWER\") AND IsApproved=1"""
            self.db_cursor.execute(get_crop_query)
            crop_list = list(self.db_cursor.fetchall())
            for crop in crop_list:
                crop_menu.add_command(label=crop[0], command=lambda value=crop[0]: self.crop_var.set(value))
            self.crop_var.set(crop_list[0][0])
        else:
            self.animal_label.pack(side=LEFT)
            self.animal_drop_down.pack(side=LEFT)
            self.item_type_label.pack(side=LEFT)
            self.item_type_drop_down.pack(side=LEFT)

            crop_menu = self.crop_drop_down["menu"]
            crop_menu.delete(0, END)
            get_crop_query = """SELECT Name FROM FarmItem
                                WHERE Type<>\"Animal\" AND IsApproved=1"""
            self.db_cursor.execute(get_crop_query)
            crop_list = list(self.db_cursor.fetchall())
            for crop in crop_list:
                crop_menu.add_command(label=crop[0], command=lambda value=crop[0]: self.crop_var.set(value))
            self.crop_var.set(crop_list[0][0])


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
