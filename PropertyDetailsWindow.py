#NOTES:
#Stuff to do:
#1. Add the pass in of the property name

from tkinter import *
import tkinter.messagebox as messagebox
import MySQLdb as sql

#db = sql.connect(host="academic-mysql.cc.gatech.edu",
#                user="cs4400_team_26", passwd="YFxUWSqD",
#                db="cs4400_team_26")

#root = Tk()

class PropertyDetailsWindow(Frame):
    def __init__(self, parent, db_cursor):
        Frame.__init__(self, parent)
        self.db_cursor = db_cursor
        #self.master = master
        #master.title(self.current_property + " Property Details")

        self.current_property = ""

    def populate(self):
        prop_detail_query = "SELECT * FROM Property WHERE Name=\"{}\"".format(self.current_property)
        self.db_cursor.execute(prop_detail_query)
        prop_details = self.db_cursor.fetchall()
        prop_id = prop_details[0][0]
        prop_size = prop_details[0][2]
        prop_commercial = prop_details[0][3]
        prop_public = prop_details[0][4]
        prop_address = prop_details[0][5]
        prop_city = prop_details[0][6]
        prop_zip = prop_details[0][7]
        prop_type = prop_details[0][8]
        prop_owner = prop_details[0][9]
        if prop_commercial == 1:
            prop_commercial = "Yes"
        else: 
            prop_commercial = "No"
        if prop_public == 1:
            prop_public = "Yes"
        else:
            prop_public = "No"
        prop_type = (prop_type[0].upper() + prop_type[1:].lower())
        prop_id = str(prop_id).zfill(5)
        email_query = "SELECT Email FROM User WHERE Username=\"{}\"".format(prop_owner)
        self.db_cursor.execute(email_query)
        prop_owner_email = self.db_cursor.fetchall()[0][0]

        visits_query = "SELECT COUNT(PropertyID) FROM Visit WHERE PropertyID =\"{}\"".format(prop_id)
        self.db_cursor.execute(visits_query)
        prop_visits = self.db_cursor.fetchall()[0][0]

        avg_rating_query = "SELECT AVG(Rating) FROM Visit WHERE PropertyID =\"{}\"".format(prop_id)
        self.db_cursor.execute(visits_query)
        prop_avg_rtg = self.db_cursor.fetchall()[0][0]
        if prop_visits == 0:
            prop_avg_rtg = "No Visits Yet"

        crops_query = "SELECT ItemName FROM Has LEFT OUTER JOIN FarmItem ON Has.ItemName=FarmItem.Name WHERE PropertyID =\"{}\" and Type !=\"ANIMAL\"".format(prop_id)
        self.db_cursor.execute(crops_query)
        prop_crops = self.db_cursor.fetchall()
        prop_crop_list = ""
        for item in prop_crops:
            prop_crop_list = prop_crop_list + item[0] + ", "
        prop_crop_list = prop_crop_list[0:len(prop_crop_list)-2]

        animal_query = "SELECT ItemName FROM Has LEFT OUTER JOIN FarmItem ON Has.ItemName=FarmItem.Name WHERE PropertyID =\"{}\" and Type =\"ANIMAL\"".format(prop_id)
        self.db_cursor.execute(animal_query)
        prop_animals = self.db_cursor.fetchall()
        prop_animal_list = ""
        for item in prop_animals:
            prop_animal_list = prop_animal_list + item[0] + ", "
        prop_animal_list = prop_animal_list[0:len(prop_animal_list)-2]


        Label(self, text=self.current_property + " Property Details", font="Times 24"). grid(row=0, columnspan=6)

        Label(self, text="Name:", font="Times 12").grid(row=1,column=0, sticky=E, padx=0)
        self.name_text = Label(self, text=self.current_property, font="Times 12")
        self.name_text.grid(row=1,column=1, sticky=W, padx=0)

        Label(self, text="Owner:", font="Times 12").grid(row=2,column=0, sticky=E, padx=0)
        self.owner_text = Label(self, text=prop_owner, font="Times 12")
        self.owner_text.grid(row=2,column=1, sticky=W, padx=0)
        
        Label(self, text="Owner Email:", font="Times 12").grid(row=3,column=0, sticky=E, padx=0)
        self.email_text = Label(self, text=prop_owner_email, font="Times 12")
        self.email_text.grid(row=3,column=1, sticky=W, padx=0)

        Label(self, text="Visits:", font="Times 12").grid(row=4,column=0, sticky=E, padx=0)
        self.visits_text = Label(self, text=prop_visits, font="Times 12")
        self.visits_text.grid(row=4,column=1, sticky=W, padx=0)

        Label(self, text="Address:", font="Times 12").grid(row=5,column=0, sticky=E, padx=0)
        self.address_text = Label(self, text=prop_address, font="Times 12")
        self.address_text.grid(row=5,column=1, sticky=W, padx=0)

        Label(self, text="City:", font="Times 12").grid(row=6,column=0, sticky=E, padx=0)
        self.city_text = Label(self, text=prop_city, font="Times 12")
        self.city_text.grid(row=6,column=1, sticky=W, padx=0)

        Label(self, text="Zip:", font="Times 12").grid(row=7,column=0, sticky=E, padx=0)
        self.zip_text = Label(self, text=prop_zip, font="Times 12")
        self.zip_text.grid(row=7,column=1, sticky=W, padx=0)

        Label(self, text="Size (Acres):", font="Times 12").grid(row=8,column=0, sticky=E, padx=0)
        self.size_text = Label(self, text=prop_size, font="Times 12")
        self.size_text.grid(row=8,column=1, sticky=W, padx=0)

        Label(self, text="Avg Rating:", font="Times 12").grid(row=9,column=0, sticky=E, padx=0)
        self.rating_text = Label(self, text=prop_avg_rtg, font="Times 12")
        self.rating_text.grid(row=9,column=1, sticky=W, padx=0)

        Label(self, text="Type:", font="Times 12").grid(row=10,column=0, sticky=E, padx=0)
        self.type_text = Label(self, text=prop_type, font="Times 12")
        self.type_text.grid(row=10,column=1, sticky=W, padx=0)

        Label(self, text="Public:", font="Times 12").grid(row=11,column=0, sticky=E, padx=0)
        self.public_text = Label(self, text=prop_public, font="Times 12")
        self.public_text.grid(row=11,column=1, sticky=W, padx=0)

        Label(self, text="Commercial:", font="Times 12").grid(row=12,column=0, sticky=E, padx=0)
        self.commercial_text = Label(self, text=prop_commercial, font="Times 12")
        self.commercial_text.grid(row=12,column=1, sticky=W, padx=0)

        Label(self, text="ID:", font="Times 12").grid(row=13,column=0, sticky=E, padx=0)
        self.id_text = Label(self, text=prop_id, font="Times 12")
        self.id_text.grid(row=13,column=1, sticky=W, padx=0)

        Label(self, text="Crops:", font="Times 12").grid(row=14,column=0, sticky=E, padx=0)
        self.crops_text = Label(self, text=prop_crop_list, font="Times 12")
        self.crops_text.grid(row=14,column=1, sticky=W, padx=0)

        Label(self, text="Animals:", font="Times 12").grid(row=15,column=0, sticky=E, padx=0)
        self.animals_text = Label(self, text=prop_animal_list, font="Times 12")
        self.animals_text.grid(row=15,column=1, sticky=W, padx=0)

        self.backButton = Button(self, text="Back",
                                command=self.back_event_handler)
        self.backButton.grid(row=16,column=0, sticky=W+E,columnspan=2)
        self.text_list = [self.animals_text, self.crops_text, self.id_text, self.commercial_text, self.public_text, self.type_text, self.rating_text, self.size_text, self.zip_text, self.city_text, self.address_text, self.visits_text, self.email_text, self.owner_text, self.name_text]

    def back_event_handler(self):
        self.master.master.show_window("OwnerViewOtherOwnersPropertiesWindow")
        for text in self.text_list:
            text.grid_remove()
        