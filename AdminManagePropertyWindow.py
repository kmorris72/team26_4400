from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox


# Approved animals (names only).
APPROVED_ANIMALS = []

# Approve crops (names only).
APPROVED_CROPS = []

# Values for IsPublic/IsCommercial.
PUB_COMM_OPTIONS = ["True", "False"]


class AdminManagePropertyWindow(Frame):
    def __init__(self, master, db_cursor):
        Frame.__init__(self, master)

        self.db_cursor = db_cursor

        self.property = None

        self.previous_window = None

        self.name = """select name from propertylist"""
        self.label = Label(self,
                           text="Manage Property",
                           font="Times 32")
        self.label.pack()

        self.basic_info_container=Frame(self)
        self.basic_info_container.pack()

        self.basic_info_container_labels_part_1 = Frame(self.basic_info_container)
        self.basic_info_container_labels_part_1.pack(side=LEFT)

        self.basic_info_container_labels_part_1_left_side=Frame(self.basic_info_container_labels_part_1)
        self.basic_info_container_labels_part_1_left_side.pack(side=LEFT)

        self.name_label = Label(self.basic_info_container_labels_part_1_left_side,
                               text="Name:",
                               font="Times 12")
        self.name_label.pack()

        self.add_label = Label(self.basic_info_container_labels_part_1_left_side,
                           text="Address:",
                           font="Times 12")
        self.add_label.pack()

        self.cit_label = Label(self.basic_info_container_labels_part_1_left_side,
                           text="City:",
                           font="Times 12")
        self.cit_label.pack()

        self.zip_label = Label(self.basic_info_container_labels_part_1_left_side,
                           text="Zip:",
                           font="Times 12")
        self.zip_label.pack()

        self.siz_label = Label(self.basic_info_container_labels_part_1_left_side,
                           text="Size (acres):",
                           font="Times 12")
        self.siz_label.pack()

        self.basic_info_container_labels_part_1_right_side=Frame(self.basic_info_container_labels_part_1)
        self.basic_info_container_labels_part_1_right_side.pack(side=RIGHT)

        self.name_entry = Entry(self.basic_info_container_labels_part_1_right_side,
                                font="Times 12",
                                width=12)
        self.name_entry.pack()

        self.address_entry = Entry(self.basic_info_container_labels_part_1_right_side,
                                font="Times 12",
                                width=12)
        self.address_entry.pack()

        self.city_entry = Entry(self.basic_info_container_labels_part_1_right_side,
                                font="Times 12",
                                width=12)
        self.city_entry.pack()

        self.zip_entry = Entry(self.basic_info_container_labels_part_1_right_side,
                                font="Times 12",
                                width=12)
        self.zip_entry.pack()

        self.size_entry = Entry(self.basic_info_container_labels_part_1_right_side,
                                font="Times 12",
                                width=12)
        self.size_entry.pack()

        self.basic_info_container_labels_part_2=Frame(self.basic_info_container)
        self.basic_info_container_labels_part_2.pack()

        self.basic_info_container_labels_part_2_left_side=Frame(self.basic_info_container_labels_part_2)
        self.basic_info_container_labels_part_2_left_side.pack(side=LEFT)

        self.typ_label = Label(self.basic_info_container_labels_part_2_left_side,
                           text="Type:",
                           font="Times 12")
        self.typ_label.pack()

        self.pub_label = Label(self.basic_info_container_labels_part_2_left_side,
                           text="Public:",
                           font="Times 12")
        self.pub_label.pack()

        self.com_label = Label(self.basic_info_container_labels_part_2_left_side,
                           text="Commercial:",
                           font="Times 12")
        self.com_label.pack()

        self.id_label = Label(self.basic_info_container_labels_part_2_left_side,
                           text="ID:",
                           font="Times 12")
        self.id_label.pack()

        self.basic_info_container_labels_part_2_right_side=Frame(self.basic_info_container_labels_part_2)
        self.basic_info_container_labels_part_2_right_side.pack(side=RIGHT)

        self.a_type_label = Label(self.basic_info_container_labels_part_2_right_side,
                           text="Farm",
                           font="Times 12")
        self.a_type_label.pack()

        self.public_var = StringVar(self.basic_info_container_labels_part_2_right_side)
        self.public_var.set(PUB_COMM_OPTIONS[1])

        self.public_drop_down = OptionMenu(self.basic_info_container_labels_part_2_right_side, self.public_var, *PUB_COMM_OPTIONS)
        self.public_drop_down.pack()

        self.comm_var = StringVar(self.basic_info_container_labels_part_2_right_side)
        self.comm_var.set(PUB_COMM_OPTIONS[1])

        self.comm_drop_down = OptionMenu(self.basic_info_container_labels_part_2_right_side, self.comm_var, *PUB_COMM_OPTIONS)
        self.comm_drop_down.pack()

        self.id_num_label = Label(self.basic_info_container_labels_part_2_right_side,
                           text="ID:",
                           font="Times 12")
        self.id_num_label.pack()

        self.animals_and_crops_container = Frame(self)
        self.animals_and_crops_container.pack()

        self.animals_and_crops_container_part_animals = Frame(self.animals_and_crops_container)
        self.animals_and_crops_container_part_animals.pack(side=LEFT)

        self.animals_and_crops_container_part_animals_labels_side = Frame(self.animals_and_crops_container_part_animals)
        self.animals_and_crops_container_part_animals_labels_side.pack(side=LEFT)

        self.a_label=Label(self.animals_and_crops_container_part_animals_labels_side,
                        text="Animals:",
                        font="Times 12")
                        
        self.animals_and_crops_container_part_animals_list_side = Frame(self.animals_and_crops_container_part_animals)
        self.animals_and_crops_container_part_animals_list_side.pack(side=RIGHT)

        self.animals_and_crops_container_crops_side = Frame(self.animals_and_crops_container)
        self.animals_and_crops_container_crops_side.pack(side=RIGHT)

        self.animals_and_crops_container_crops_side_label_side = Frame(self.animals_and_crops_container_crops_side)
        self.animals_and_crops_container_crops_side_label_side.pack(side=LEFT)

        self.a_label = Label(self.animals_and_crops_container_crops_side_label_side,
                        text="Crops:",
                        font="Times 12")

        self.animals_and_crops_container_crops_side_lists_side = Frame(self.animals_and_crops_container_crops_side)
        self.animals_and_crops_container_crops_side_lists_side.pack(side=RIGHT)

        self.add_animals_or_crops_container = Frame(self)
        self.add_animals_or_crops_container.pack()

        self.add_animals_or_crops_container_add_animal = Frame(self.add_animals_or_crops_container)
        self.add_animals_or_crops_container_add_animal.pack(side=LEFT)

        self.anim_label = Label(self.add_animals_or_crops_container_add_animal,
                           text="Add new Animal:",
                           font="Times 12")
        self.anim_label.pack(side=LEFT, pady=(50,0))

        self.add_animals_or_crops_container_add_animal_select_side = Frame(self.add_animals_or_crops_container_add_animal)
        self.add_animals_or_crops_container_add_animal_select_side.pack(side=RIGHT)

        self.animal_var = StringVar(self.add_animals_or_crops_container_add_animal_select_side)

        self.animal_drop_down = OptionMenu(self.add_animals_or_crops_container_add_animal_select_side, self.animal_var, "")
        self.animal_drop_down.pack()

        self.add_an_button = Button(self.add_animals_or_crops_container_add_animal_select_side,
                                   text="Add Animal to \nProperty",
                                   padx=10,
                                   height=2,width=12,
                                   command=self.add_animal_button_clicked_handler)
        self.add_an_button.pack(side=LEFT, pady=(5,10),padx=5)

        self.add_animals_or_crops_container_add_crops=Frame(self.add_animals_or_crops_container)
        self.add_animals_or_crops_container_add_crops.pack(side=RIGHT)

        self.anim_label = Label(self.add_animals_or_crops_container_add_crops,
                           text="Add new Crop:",
                           font="Times 12")
        self.anim_label.pack(side=LEFT, pady=(50,0))

        self.add_animals_or_crops_container_add_crops_select_side=Frame(self.add_animals_or_crops_container_add_crops)
        self.add_animals_or_crops_container_add_crops_select_side.pack(side=RIGHT)

        self.crop_var = StringVar(self.add_animals_or_crops_container_add_crops_select_side)

        self.crop_drop_down = OptionMenu(self.add_animals_or_crops_container_add_crops_select_side, self.crop_var, "")
        self.crop_drop_down.pack()

        self.add_cr_button = Button(self.add_animals_or_crops_container_add_crops_select_side,
                                   text="Add Crop to \nProperty",
                                   padx=10,
                                   height=2,width=12,
                                   command=self.add_crop_button_clicked_handler)
        self.add_cr_button.pack(side=LEFT, pady=(5,10),padx=5)

        self.delete_save_back_buttons_container = Frame(self)
        self.delete_save_back_buttons_container.pack()

        self.delete_property_button = Button(self.delete_save_back_buttons_container,
                                   text="Delete Property",
                                   padx=10,
                                   width = 12)
        self.delete_property_button.pack(side=LEFT, pady=(75,0))

        self.delete_save_back_buttons_container_middle_section = Frame(self.delete_save_back_buttons_container)
        self.delete_save_back_buttons_container_middle_section.pack(side=RIGHT)

        self.save_button = Button(self.delete_save_back_buttons_container_middle_section,
                                   text="Save Changes\n(confirm property)",
                                   padx=10,
                                   height=3,width=15,
                                   command=self.save_button_clicked_handler)
        self.save_button.pack()

        self.back_button = Button(self.delete_save_back_buttons_container_middle_section,
                                   text="Back\n(Don't Save or Confirm)",
                                   padx=10,
                                   height=3,width=15,
                                   command=self.back_button_clicked_handler)
        self.back_button.pack()


    def add_animal_button_clicked_handler(self):
        if messagebox.askyesno("Alert", "Are You Sure You Want to Add the Selected Animal to this Property?"):
            add_animal_query = """INSERT INTO Has
                            VALUES ({}, "{}")""".format(self.property[0], self.animal_var.get())
            self.db_cursor.execute(add_animal_query)
            messagebox.showinfo("Alert", "Animal added.")
        else:
            messagebox.showinfo("Alert", "Animal not added.")


    def add_crop_button_clicked_handler(self):
        if messagebox.askyesno("Alert", "Are You Sure You Want to Add the Selected Crop to this Property?"):
            add_crop_query = """INSERT INTO Has
                                VALUES ({}, "{}")""".format(self.property[0], self.crop_var.get())
            self.db_cursor.execute(add_crop_query)
            messagebox.showinfo("Alert", "Crop added.")
        else:
            messagebox.showinfo("Alert", "Crop not added.")

        
    def delete_property_button_clicked_handler(self):
        if messagebox.askyesno("Alert", "Are You Sure You Want to Delete this Property?"):
            delete_property_query = """DELETE FROM Property
                                       WHERE ID={}""".format(self.property[0])
            self.db_cursor.execute(delete_property_query)
            messagebox.showinfo("Alert", "Property deleted.")
            self.master.master.show_window(self.previous_window)
        else:
            messagebox.showinfo("Alert", "Property not deleted.")


    def save_button_clicked_handler(self):
        if messagebox.askyesno("Alert", "Are You Sure You Want to Save the Changes to this Property?"):
            try:
                make_prop_changes_query = """UPDATE Property
                                            SET Name="{}", Street="{}", City="{}". Zip={}, Size={}, IsPublic={}, IsApproved={}
                                            WHERE ID={}""".format(self.name_entry.get(), self.address_entry.get(), self.city_entry.get(), int(self.zip_entry.get()), float(self.size_entry.get()), 1 if self.public_var.get() == "True" else 0, 1 if self.comm_var.get() == "True" else 0, self.property[0])
                self.db_cursor.execute(make_prop_changes_query)
                messagebox.showinfo("Alert", "Changes saved.")
            except:
                messagebox.showinfo("Alert", "No changes saved. Please make sure that you have entered numbers for Zip and Size.")
        else:
            messagebox.showinfo("Alert", "Changes not saved.")

    
    def back_button_clicked_handler(self):
        self.master.master.show_window(self.previous_window)

    
    def set_previous_window(self, window):
        self.previous_window = window

        
    def fill_in_data_from_prop(self, prop):
        self.property = list(prop)

        self.name_entry.delete(0, END)
        self.name_entry.insert(0, prop[1])

        self.address_entry.delete(0, END)
        self.address_entry.insert(0, prop[5])

        self.city_entry.delete(0, END)
        self.city_entry.insert(0, prop[6])

        self.zip_entry.delete(0, END)
        self.zip_entry.insert(0, prop[7])

        self.size_entry.delete(0, END)
        self.size_entry.insert(0, prop[2])

        self.a_label.config(text=prop[8])

        if prop[4] == 1:
            self.public_var.set(PUB_COMM_OPTIONS[0])
        else:
            self.public_var.set(PUB_COMM_OPTIONS[1])

        if prop[3] == 1:
            self.comm_var.set(PUB_COMM_OPTIONS[0])
        else:
            self.comm_var.set(PUB_COMM_OPTIONS[1])

        self.id_num_label.config(text=prop[0])


    def get_approved_animals_and_crops_from_db(self):
        animal_query = """SELECT Name
                          FROM FarmItem
                          WHERE Type="ANIMAL" AND IsApproved=1"""
        self.db_cursor.execute(animal_query)
        animals_result = self.db_cursor.fetchall()

        crop_query = """SELECT Name
                        FROM FarmItem
                        WHERE Type<>"ANIMAL" AND IsApproved=1"""
        self.db_cursor.execute(crop_query)
        crops_result = self.db_cursor.fetchall()

        for i in range(len(animals_result)):
            APPROVED_ANIMALS.append(animals_result[i][0])
        
        for i in range(len(crops_result)):
            APPROVED_CROPS.append(crops_result[i][0])
        
        animal_menu = self.animal_drop_down["menu"]
        animal_menu.delete(0, END)
        for animal in APPROVED_ANIMALS:
            animal_menu.add_command(label=animal, command=lambda value=animal: self.animal_var.set(value))
        self.animal_var.set(APPROVED_ANIMALS[0])

        crop_menu = self.crop_drop_down["menu"]
        crop_menu.delete(0, END)
        for crop in APPROVED_CROPS:
            crop_menu.add_command(label=crop, command=lambda value=crop: self.crop_var.set(value))
        self.crop_var.set(APPROVED_CROPS[0])
