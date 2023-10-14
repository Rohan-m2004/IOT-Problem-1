# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 06:36:58 2023

@author: jeman
"""

import Read_Hospital_Excel_Sheet
import Write_Hospital_Excel_Sheet


def AppointmentIndexInDoctorsDataBase(patient_ID):
    for i in Doctors_DataBase:
        for j in Doctors_DataBase[i]:
            if str(patient_ID) == str(j[0]):
                Appointment_index = Doctors_DataBase[i].index(j)
                return Appointment_index, i


print("****************************************************************************")
print("*                                                                          *")
print("*                   Welcome to Vitality Medical Centre Management System          *")
print("*                                                                          *")
print("****************************************************************************")

tries = 0
tries_flag = ""
while tries_flag != "Close the program":

    Pateints_DataBase = Read_Hospital_Excel_Sheet.Read_Patients_DataBase()
    Doctors_DataBase = Read_Hospital_Excel_Sheet.Read_Doctors_DataBase()

    print("-----------------------------------------")
    print("|Enter 1 for Admin mode			|\n|Enter 2 for user mode|")
    print("-----------------------------------------")
    Admin_user_mode = input("Enter your mode : ")

    if Admin_user_mode == "1":  # Admin mode
        print(
            "*****\n|         Welcome to admin mode         |\n*****")
        Password = input("Please enter your password : ")
        while True:

            if Password == "1234":
                print("-----------------------------------------")
                print("|To manage patients Enter 1|\n|"
                    "To manage docotrs Enter 2|\n|"
                    "To manage appointments Enter 3|\n|"
                    "To be back Enter E			|")
                print("-----------------------------------------")
                AdminOptions = input("Enter your choice : ")
                AdminOptions = AdminOptions.upper()

                if AdminOptions == "1":  # Admin mode --> Pateints Management
                    print("-----------------------------------------")
                    print("|To add new patient Enter 1	  	|")
                    print("|To display patient Enter 2	  	|")
                    print("|To delete patient data Enter 3		|")
                    print("|To edit patient data Enter 4    	|")
                    print("|To Back enter B      			|")
                    print("-----------------------------------------")
                    Admin_choice = input("Enter your choice : ")
                    Admin_choice = Admin_choice.upper()

                    if Admin_choice == "1":  # Admin mode --> Pateints Management --> Enter new patient data
                        try:  
                            patient_ID = int(input("Enter patient ID : "))
                            while patient_ID in Pateints_DataBase:  # if Admin entered used ID
                                patient_ID = int(input("This ID is unavailable, please try another ID : "))
                            Department = input("Enter patient department                : ")
                            DoctorName = input("Enter name of doctor following the case : ")
                            Name = input("Enter patient name                      : ")
                            Age = input("Enter patient age                       : ")
                            Gender = input("Enter patient gender                    : ")
                            Address = input("Enter patient address                   : ")
                            RoomNumber = input("Enter patient room number               : ")
                            Pateints_DataBase[patient_ID] = [Department, DoctorName, Name, Age, Gender, Address,
                                                             RoomNumber]
                            print("----------------------Patient added successfully----------------------")
                        except:
                            print("Patient ID should be an integer number")

                    elif Admin_choice == "2":  # Admin mode --> Pateints Management --> Display patient data
                        try:  
                            patient_ID = int(input("Enter patient ID : "))
                            while patient_ID not in Pateints_DataBase:
                                patient_ID = int(input("Incorrect ID, Please Enter patient ID : "))
                            print("\npatient name        : ", Pateints_DataBase[patient_ID][2])
                            print("patient age         : ", Pateints_DataBase[patient_ID][3])
                            print("patient gender      : ", Pateints_DataBase[patient_ID][4])
                            print("patient address     : ", Pateints_DataBase[patient_ID][5])
                            print("patient room number : ", Pateints_DataBase[patient_ID][6])
                            print("patient is in " + Pateints_DataBase[patient_ID][0] + " department")
                            print("patient is followed by doctor : " + Pateints_DataBase[patient_ID][1])
                        except:
                            print("Patient ID should be an integer number")

                    elif Admin_choice == "3":  # Admin mode --> Pateints Management --> Delete patient data
                        try:  
                            patient_ID = int(input("Enter patient ID : "))
                            while patient_ID not in Pateints_DataBase:
                                patient_ID = int(input("Incorrect ID, Please Enter patient ID : "))
                            Pateints_DataBase.pop(patient_ID)
                            print("----------------------Patient data deleted successfully----------------------")
                        except:
                            print("Patient ID should be an integer number")

                    elif Admin_choice == "4":  # Admin mode --> Pateints Management --> Edit patient data
                        try:  
                            patient_ID = int(input("Enter patient ID : "))
                            while patient_ID not in Pateints_DataBase:
                                patient_ID = int(input("Incorrect ID, Please Enter patient ID : "))
                            while True:
                                print("------------------------------------------")
                                print("|To Edit pateint Department Enter 1 :    |")
                                print("|To Edit Doctor following case Enter 2 : |")
                                print("|To Edit pateint Name Enter 3 :          |")
                                print("|To Edit pateint Age Enter 4 :           |")
                                print("|To Edit pateint Gender Enter 5 :        |")
                                print("|To Edit pateint Address Enter 6 :       |")
                                print("|To Edit pateint RoomNumber Enter 7 :    |")
                                print("|To be Back Enter B                      |")
                                print("-----------------------------------------")
                                Admin_choice = input("Enter your choice : ")
                                Admin_choice = Admin_choice.upper()
                                if Admin_choice == "1":
                                    Pateints_DataBase[patient_ID][0] = input("\nEnter patient department : ")
                                    print(
                                        "----------------------Patient Department edited successfully----------------------")

                                elif Admin_choice == "2":
                                    Pateints_DataBase[patient_ID][1] = input("\nEnter Doctor follouing case : ")
                                    print(
                                        "----------------------Doctor follouing case edited successfully----------------------")

                                elif Admin_choice == "3":
                                    Pateints_DataBase[patient_ID][2] = input("\nEnter patient name : ")
                                    print(
                                        "----------------------Patient name edited successfully----------------------")

                                elif Admin_choice == "4":
                                    Pateints_DataBase[patient_ID][3] = input("\nEnter patient Age : ")
                                    print("----------------------Patient age edited successfully----------------------")

                                elif Admin_choice == "5":
                                    Pateints_DataBase[patient_ID][4] = input("\nEnter patient gender : ")
                                    print(
                                        "----------------------Patient address gender successfully----------------------")

                                elif Admin_choice == "6":
                                    Pateints_DataBase[patient_ID][5] = input("\nEnter patient address : ")
                                    print(
                                        "----------------------Patient address edited successfully----------------------")

                                elif Admin_choice == "7":
                                    Pateints_DataBase[patient_ID][6] = input("\nEnter patient RoomNumber : ")
                                    print(
                                        "----------------------Patient RoomNumber edited successfully----------------------")

                                elif Admin_choice == "B":
                                    break

                                else:
                                    print("Please Enter a correct choice")
                        except:
                            print("Patient ID should be an integer number")

                    elif Admin_choice == "B":  # Admin mode --> Pateints Management --> Back
                        break

                    else:
                        print("Please enter a correct choice\n")

                elif AdminOptions == "2":  # Admin mode --> Doctors Management
                    print("-----------------------------------------")
                    print("|To add new doctor Enter 1              |")
                    print("|To display doctor Enter 2              |")
                    print("|To delete doctor data Enter 3          |")
                    print("|To edit doctor data Enter 4            |")
                    print("|To be back enter B                     |")
                    print("-----------------------------------------")
                    Admin_choice = input("Enter your choice : ")
                    Admin_choice = Admin_choice.upper()

                    if Admin_choice == "1":  # Admin mode --> Doctors Management --> Enter new doctor data
                        try:  
                            Doctor_ID = int(input("Enter doctor ID : "))
                            while Doctor_ID in Doctors_DataBase:  # if Admin entered used ID
                                Doctor_ID = int(input("This ID is unavailable, please try another ID : "))

                            Department = input("Enter Doctor department : ")
                            Name = input("Enter Doctor name       : ")
                            Address = input("Enter Doctor address    : ")
                            Doctors_DataBase[Doctor_ID] = [[Department, Name, Address]]
                            print("----------------------Doctor added successfully----------------------")
                        except:
                            print("Doctor ID should be an integer number")

                    elif Admin_choice == "2":  # Admin mode --> Doctors Management --> Display doctor data
                        try:  
                            Doctor_ID = int(input("Enter doctor ID : "))
                            while Doctor_ID not in Doctors_DataBase:
                                Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
                            print("Doctor name    : ", Doctors_DataBase[Doctor_ID][0][1])
                            print("Doctor address : ", Doctors_DataBase[Doctor_ID][0][2])
                            print("Doctor is in " + Doctors_DataBase[Doctor_ID][0][0] + " department")
                        except:
                            print("Doctor ID should be an integer number")

                    elif Admin_choice == "3":  # Admin mode --> Doctors Management --> Delete doctor data
                        try:  # To avoid non integer input
                            Doctor_ID = int(input("Enter doctor ID : "))
                            while Doctor_ID not in Doctors_DataBase:
                                Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
                            Doctors_DataBase.pop(Doctor_ID)
                            print("/----------------------Doctor data deleted successfully----------------------/")
                        except:
                            print("Doctor ID should be an integer number")

                    elif Admin_choice == "4":  # Admin mode --> Doctors Management --> Edit Doctor data
                        try:  # To avoid non integer input
                            Doctor_ID = input("Enter doctor ID : ")
                            while Doctor_ID not in Doctors_DataBase:
                                Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
                            print("-----------------------------------------")
                            print("|To Edit doctor's department Enter 1    |")
                            print("|To Edit doctor's name Enter 2          |")
                            print("|To Edit doctor's address Enter 3       |")
                            print("To be Back Enter B                      |")
                            print("-----------------------------------------")
                            Admin_choice = input("Enter your choice : ")
                            Admin_choice = Admin_choice.upper()
                            if Admin_choice == "1":
                                Doctors_DataBase[Doctor_ID][0][0] = input("Enter Doctor's Department : ")
                                print(
                                    "/----------------------Doctor's department edited successfully----------------------/")

                            elif Admin_choice == "2":
                                Doctors_DataBase[Doctor_ID][0][1] = input("Enter Doctor's Name : ")
                                print("----------------------Doctor's name edited successfully----------------------")

                            elif Admin_choice == "3":
                                Doctors_DataBase[Doctor_ID][0][2] = input("Enter Doctor's Address : ")
                                print(
                                    "----------------------Doctor's address edited successfully----------------------")

                            elif Admin_choice == "B":
                                break

                            else:
                                print("\nPlease enter a correct choice\n")

                        except:
                            print("Doctor ID should be an integer number")

                    elif Admin_choice == "B":  # Back
                        break

                    else:
                        print("\nPlease enter a correct choice\n")

                elif AdminOptions == "3":  # Admin mode --> Appointment Management
                    print("-----------------------------------------")
                    print("|To book an appointment Enter 1         |")
                    print("|To edit an appointment Enter 2         |")
                    print("|To cancel an appointment Enter 3       |")
                    print("|To be back enter B                     |")
                    print("-----------------------------------------")
                    Admin_choice = input("Enter your choice : ")
                    Admin_choice = Admin_choice.upper()
                    if Admin_choice == "1":  # Admin mode --> Appointment Management --> Book an appointment
                        try:  # To avoid non integer input
                            Doctor_ID = int(input("Enter the ID of doctor : "))
                            while Doctor_ID not in Doctors_DataBase:
                                Doctor_ID = int(input("Doctor ID incorrect, Please enter a correct doctor ID : "))
                            print("---------------------------------------------------------")
                            print("|For book an appointment for an exist patient Enter 1|\n|"
                                  "For book an appointment for a new patient Enter 2|\n|"
                                  "To be Back Enter B|")
                            print("---------------------------------------------------------")
                            Admin_choice = input("Enter your choice : ")
                            Admin_choice = Admin_choice.upper()
                            if Admin_choice == "1":
                                patient_ID = int(input("Enter patient ID : "))
                                while patient_ID not in Pateints_DataBase:  # if Admin entered incorrect ID
                                    patient_ID = int(input("Incorrect ID, please Enter a correct patient ID : "))


                            elif Admin_choice == "2":
                                patient_ID = int(input("Enter patient ID : "))
                                while patient_ID in Pateints_DataBase:  # if Admin entered used ID
                                    patient_ID = int(input("This ID is unavailable, please try another ID : "))
                                Department = Doctors_DataBase[Doctor_ID][0][0]
                                DoctorName = Doctors_DataBase[Doctor_ID][0][1]
                                Name = input("Enter patient name    : ")
                                Age = input("Enter patient age     : ")
                                Gender = input("Enter patient gender  : ")
                                Address = input("Enter patient address : ")
                                RoomNumber = ""
                                Pateints_DataBase[patient_ID] = [Department, DoctorName, Name, Age, Gender, Address,
                                                                 RoomNumber]

                            elif Admin_choice == "B":
                                break

                            Session_Start = input("Session starts at : ")
                            while Session_Start[:2] == "11" or Session_Start[:2] == "12":
                                Session_Start = input("Appointments should be between 01:00PM to 10:00PM,"
                                                      "Please enter a time between working hours : ")

                            for i in Doctors_DataBase[Doctor_ID]:
                                if type(i[0]) != str:
                                    while Session_Start >= i[1] and Session_Start < i[2]:
                                        Session_Start = input("This appointment is already booked,"
                                                              "Please Enter an other time for start of session : ")
                            Session_End = input("Session ends at : ")

                            New_Appointment = list()
                            New_Appointment.append(patient_ID)
                            New_Appointment.append(Session_Start)
                            New_Appointment.append(Session_End)
                            Doctors_DataBase[Doctor_ID].append(New_Appointment)
                            print("/----------------------Appointment booked successfully----------------------/")
                        except:
                            print("Doctor ID should be an integer number")

                    elif Admin_choice == "2":  # Admin mode --> Appointment Management --> Edit an appointment
                        try:  # To avoid non integer input
                            patient_ID = int(input("Enter patient ID : "))
                            while patient_ID not in Pateints_DataBase:
                                patient_ID = int(input("Incorrect Id, Please Enter correct patient ID : "))
                            try:  # To avoid no return function
                                AppointmentIndex, PairKey = AppointmentIndexInDoctorsDataBase(patient_ID)
                                Session_Start = input("Please enter the new start time : ")
                                while Session_Start[:2] == "11" or Session_Start[:2] == "12":
                                    Session_Start = input("Appointments should be between 01:00PM to 10:00PM,"
                                                          "Please enter a time between working hours : ")

                                for i in Doctors_DataBase[Doctor_ID]:
                                    if type(i[0]) != str:
                                        while Session_Start >= i[1] and Session_Start < i[2]:
                                            Session_Start = input("This appointment is already booked, "
                                                                  "Please Enter an other time for start of session : ")
                                Session_End = input("Please enter the new end time : ")
                                Doctors_DataBase[PairKey][AppointmentIndex] = [patient_ID, Session_Start, Session_End]
                                print("/----------------------appointment edited successfully----------------------/")
                            except:
                                print("No Appointment for this patient")
                        except:
                            print("Doctor ID should be an integer number")

                    elif Admin_choice == "3":  # Admin mode --> Appointment Management --> Cancel an appointment
                        try:  # To avoid non integer input
                            patient_ID = int(input("Enter patient ID : "))
                            while patient_ID not in Pateints_DataBase:
                                patient_ID = int(input("Invorrect ID, Enter patient ID : "))
                            try:
                                AppointmentIndex, PairKey = AppointmentIndexInDoctorsDataBase(patient_ID)
                                Doctors_DataBase[PairKey].pop(AppointmentIndex)
                                print("/----------------------appointment canceled successfully----------------------/")
                            except:
                                print("No Appointment for this patient")
                        except:  # To avoid no return function
                            print("Patient ID should be an integer number")

                    elif Admin_choice == "B":  # Back
                        break

                    else:
                        print("please enter a correct choice")

                elif AdminOptions == "B":  # Back
                    break

                else:
                    print("Please enter a correct option")


            elif Password != "1234":
                if tries < 2:
                    Password = input("Password incorrect, please try again : ")
                    tries += 1
                else:
                    print("Incorrect password, no more tries")
                    tries_flag = "Close the program"
                    break

            Write_Hospital_Excel_Sheet.Write_Patients_DataBase(Pateints_DataBase)
            Write_Hospital_Excel_Sheet.Write_Doctors_DataBase(Doctors_DataBase)


    elif Admin_user_mode == "2":  # User mode
        print("*****\n|         Welcome to user mode         |\n*****")
        while True:
            def ambulance_on_the_way():
                print("Ambulance on the way! Estimated time of arrival is {time} minutes.")

            def patient_login():
                registered_members = {'username1': 'password1', 'username2': 'password2'}  # Example registered members

                username = input("Enter your username: ")
                password = input("Enter your password: ")

                if username in registered_members and registered_members[username] == password:
                    print("Login successful! Access granted to app features.")
                else:
                    print("Invalid credentials. Please try again.")

            def register_new_member():
                members_database = {}  # Example members database

                name = input("Enter your name: ")
                phone_number = input("Enter your phone number: ")
                address = input("Enter your address: ")
                gender = input("Enter your gender: ")
                # Add the new member to the database
                members_database[name] = {'phone_number': phone_number, 'address': address, 'gender': gender}

            # First screen for the hospital app
            print("Welcome to the Hospital App!")
            print("Please select the level of criticality:")
            print("1. Critical")
            print("2. Not Critical")
            print("3. View App Features")

            choice = input("Enter your choice: ")

            if choice == "1":
                ambulance_on_the_way()
            elif choice == "2":
                registered = input("Are you a registered member? (yes/no): ").lower()
                if registered == "yes":
                    patient_login()
                else:
                    register_new_member()
            elif choice == "3":
                print("Welcome to the app! You can now access the app features.")
            else:
                print("Invalid choice. Please select a valid option.")
                
                  
                
            from queue import PriorityQueue

            # Example doctors' availability data
            doctors_availability = {
                'Doctor1': {'Monday': ['10:00', '12:00', '15:00'], 'Wednesday': ['11:00', '14:00']},
                'Doctor2': {'Tuesday': ['9:00', '13:00', '16:00'], 'Thursday': ['10:00', '11:00']}
            }

            # Example priority queue of patients
            priority_queue = PriorityQueue()

            def book_appointment():
                date = input("Enter the date for the appointment (e.g., Monday, Tuesday, etc.): ")
                time = input("Enter the time for the appointment (e.g., 10:00, 15:00, etc.): ")
                area_of_concern = input("Enter the area of concern: ")

                print("Available doctors at the specified date and time:")
                for doctor, availability in doctors_availability.items():
                    if date in availability and time in availability[date]:
                        print(doctor)

                selected_doctor = input("Select the desired doctor: ")
                print(f"Appointment booked with {selected_doctor} on {date} at {time} for {area_of_concern}.")

                # Simulate payment page and successful payment
                print("Redirecting to payment page...")
                payment_success = input("Enter 'yes' if payment is successful: ").lower()

                if payment_success == "yes":
                    print("Payment successful!")
                    token_number = len(priority_queue.queue) + 1  # Simulate assigning a token number
                    priority_queue.put((1, f"Token-{token_number}"))  # Assuming priority 1 for simplicity
                    print(f"Appointment confirmed. Your token number is Token-{token_number}.")
                else:
                    print("Payment unsuccessful. Please try again.")

            # Function to access wait time and the priority queue of patients
            def access_appointment_details():
                print("Wait time: 30 minutes")  # Example wait time


            def display_vital_signs():
                vital_signs = {
                    'Heart Rate': '75 bpm',
                    'Blood Oxygen Level': '98%',
                    'Blood Pressure': '120/80 mmHg',
                    'Body Temperature': '98.6°F',
                    'Respiratory Rate': '12 breaths per minute',
                    'Cholesterol Level': '150 mg/dL',
                    'Body Mass Index (BMI)': '24.5 kg/m^2',
                    'Pulse Rate': '72 bpm',
                    # Add more vital signs as needed
                }

                print("Your current vital signs:")
                for sign, value in vital_signs.items():
                    print(f"{sign}: {value}")

            def pharmacy_service(prescribed_medications):
                hospital_inventory = ['MedicineA', 'MedicineB', 'MedicineC', 'MedicineD', 'MedicineE']  # Example hospital inventory
                nearby_pharmacies = ['PharmacyX', 'PharmacyY', 'PharmacyZ']  # Example nearby pharmacies

                print("Your prescribed medications:")
                for medication in prescribed_medications:
                    print(medication)

                for medication in prescribed_medications:
                    if medication in hospital_inventory:
                        print(f"The medicine {medication} is available in the hospital pharmacy.")
                        payment = input("Proceed to payment? (yes/no): ").lower()
                        if payment == "yes":
                            # Simulate payment process and print bill
                            print("Payment successful! Here is your bill:")
                            print(f"Medication: {medication}")
                            # Add more details to the bill as required
                    else:
                        print(f"The medicine {medication} is not available in the hospital pharmacy.")

                print("You may also check nearby pharmacies:")
                for pharmacy in nearby_pharmacies:
                    print(pharmacy)
            print("Welcome to the app! You can now access the app features.")
            print("Feature1 is Book an appointment")
            print("Feature2 Access the appointment details")
            print("Feature3 Monitor the patient vital signs")
            print("Feature4 Access the prescribed medications")
            feature=input("Enter the feature you wanna use:")
                
            if feature=="1":
                book_appointment()
            elif feature=="2":
                access_appointment_details()
            elif feature=="3":
                display_vital_signs()
            elif feature=="4":
                prescribed_meds = ['MedicineA', 'MedicineB', 'MedicineX']  # Example list of prescribed medications
                pharmacy_service(prescribed_meds)
                
            else:
                print("Invalid choice. Please select a valid option.")


    else:
        print("Please choice just 1 or 2")

