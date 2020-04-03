import os
import json

# TODO: Initialize the JSON file with Default entry

class Individual(object):
    def __init__(self):
        self.individual_array = {}

    # One of the most important functions. It gives a window 
    # for objects to request directly for the individual array
    def get_array(self):
        return self.individual_array

    # This function might be useless
    def get_phone_number(self):
        return self.PhoneNumber

    # This function eliminates the need for a complicated 
    # constructor
    def set_details(self, name, some_number):
        self.FullName = name
        self.PhoneNumber = some_number

    # Returns true no matter what happens - Which is supposed to be changed
    def save(self):
        self.individual_array.update ({"name" : self.FullName, "number" : self.PhoneNumber})
        return True


class PhoneBook(object):

    def __init__(self):
        # This array would hold the initial array to be
        # manipulated during creation of phone data and for 
        # other array manipulations
        self.Phone_Record = []

        self.number_of_entries = 0

        # I'm trying to initialize an array to
        # take the individual object's array
        self.ind_array = {}

        # This Total Array would hold the 
        # specific contents of the JSON file 
        self.TotalArray = []

        # get current directory
        currentDirectory = os.getcwd()
        # store file name in a variable
        file_name = r'/phonebook.json'
        # full path of json file
        total_path = currentDirectory + file_name
        # check if json file exists
        if os.path.isfile(total_path) and os.access(total_path, os.R_OK):
            # read json file
            with open('phonebook.json', 'r') as json_file:
                self.TotalArray = json.load(json_file)

    # This function eliminates the need for a complicated constructor
    # It takes a single parameter and sets the in_array var to its array
    def set_person(self, person):
        self.ind_array = person.get_array()
    
    # Allows the function to reset the link to the JSON file after 
    # every operation in the main function
    def startJSON_link(self):
        # get current directory
        currentDirectory = os.getcwd()
        # store file name in a variable
        file_name = r'/phonebook.json'
        # full path of json file
        total_path = currentDirectory + file_name
        # check if json file exists
        if os.path.isfile(total_path) and os.access(total_path, os.R_OK):
            # read json file
            with open('phonebook.json', 'r') as json_file:
                self.TotalArray = json.load(json_file)
    
    def Add_Phone_Entry(self, ind_array):
        # print (json_file)     -- Debugging purposes only
        # print(self.TotalArray) 

        # Array to hold individual array incase the variable exists
        reset_array = ind_array

        # Call the JSON file here and scan for
        # existing details in it
        if ind_array["number"] in ([sub["number"] for sub in self.TotalArray]):
            print ("Duplicate Detail exists")
            # Create an array variable that holds the dict to retrieve the name
            array = self.Lookup_Number(ind_array["number"])
            print ("Number exists with Name: {}".format(array["name"]))

            # This is for the API capabilities
            error = "Duplicate Detail exists"
            error_details = "Number exists with Name: {}".format(array["name"])

            # Return a dictionary containing the error and error details
            return ({"error" : error, "details" : error_details})

        elif ind_array["number"] not in ([sub["number"] for sub in self.TotalArray]):
            self.Save_Phone_Entry(ind_array)
            return "Successful"

    # A simple function that opens the JSON and dumps the new JSON 
    def Save_Phone_Entry(self, ind_array):
        self.Phone_Record = ind_array # Line might not be needed 
        self.TotalArray.append(self.Phone_Record)
        # Call the JSON file here and pop
        # details into it
        with open('phonebook.json', 'w') as phonebook:
            json.dump(self.TotalArray, phonebook, indent=4)
    
    # Function to allow for last minute change of heart
    def confirm_change(self, type_of="delete"):
        # Takes two parameters that allows the user of the function 
        # to select between the type of action to perform - Default is 'delete'
        if type_of == "delete":
            print ("Do you really want to delete this? (Y)/N (Press AnyKey to Select Default)")
            response = str(input())
            if response != "N" or "n":
                return True
            else:
                return False

        # For the alter part, it sets two new variables that are visible 
        # throughout the class and are utilized in the Update_Entry function
        if type_of == "alter":
            print ("Enter New Name: ")
            self.new_name = str(input()).lower()
            print ("Enter New Number: ")
            self.new_number = int(input())
            print ("\nDo you really want to alter this? (Y)/N (Press AnyKey to Select Default)")
            response = str(input())
            if response != "N" or "n":
                return True
            else:
                return False

    def Delete_Entry(self, name, number):
        # print (self.TotalArray) -- Debugging purposes only
        # Boolean to indicate if a value is found in the list or not
        available = False
        # Function sets record to run through the Total Array
        for record in range(len(self.TotalArray)):
            # if a matching record is found...
            if ((self.TotalArray[record]["name"] == name) & (self.TotalArray[record]["number"] == number)):
                # Verify if they want to delete it
                
                # For the API functionality, it implements it's 
                # own confirm_change function.
                del self.TotalArray[record]
                with open('phonebook.json', 'w') as phonebook:
                        json.dump(self.TotalArray, phonebook, indent=4)
                    # print (self.TotalArray) -- Debugging purposes only
                available = True

                # For the standard CMD call
                """
                if (self.confirm_change("delete") == True):
                    # Nuke em!
                    del self.TotalArray[record]
                    print("Entry Deleted Successfully! \n")

                    # For the API call
                    return "Entry Deleted Successfully! \n"

                    # Save the deleted list back to the JSON
                    with open('phonebook.json', 'w') as phonebook:
                        json.dump(self.TotalArray, phonebook, indent=4)
                    # print (self.TotalArray) -- Debugging purposes only
                    available = True
                else:
                    pass
                    # Adding anything here ruins this code
                """
                break
                    # This stops the app from doing any more iterations
                    # VERY IMPORTANT as it also reduces the app overhead
                    

            else:
                pass
                # Adding anything here ruins this code

        if available == True:
            return "Entry Deleted Successfully! \n"
        else:
            # print("\n\t Check the name or number! \n")
            # For the API call
            return ("\n\t ERROR DELETING! \n Check the name or number! \n")
        # Call the JSON file here and pop
        # details out of it

    def Update_Entry(self, name, number, new_name = "", new_number=0):
        # print (self.TotalArray) -- Debugging purposes only
        # Boolean to indicate if a value is found in the list or not
        available = False
        for record in self.TotalArray:
            # Traverse the array linearly (This should be binary in future)
            if ((record["name"] == name) & (record["number"] == number)):
                # Check if the new_number already exists in there
                if new_number in ([sub["number"] for sub in self.TotalArray]):
                    return "Duplicate Details Exist! - Number already exists!"
                else:
                    # Save the updated list back to the JSON
                    record["name"] = new_name
                    record["number"] = new_number
                    with open('phonebook.json', 'w') as phonebook:
                        json.dump(self.TotalArray, phonebook, indent=4)
                    # Set boolean to True to enable other manipulation
                    available = True
                """    
                # Call the confirm_change function incase of any last 
                # minute change of heart
                if (self.confirm_change("alter") == True):
                    record["name"] = self.new_name
                    record["number"] = self.new_number
                    # print (self.TotalArray) -- Debugging purpose only

                    # Save the updated list back to the JSON
                    with open('phonebook.json', 'w') as phonebook:
                        json.dump(self.TotalArray, phonebook, indent=4)
                    # Set boolean to True to enable other manipulation
                    available = True
                else:
                    pass
                    # Adding anything here ruins this code
                """
                break
                    # This stops the app from doing any more iterations

        if available == True:
            # print ("Successful!") -- Non-API, CLI and Debugging purposes
            return "Successful!"
        else:
            # print("\nNumber or name not found!\n") -- Non-API, CLI and Debugging purposes
            return "\nNumber or name not found!"


    def Lookup_Number(self, number):
        # Initialize available variable
        available = False
        # Traverse the array linearly (This should be binary in future)
        for record in self.TotalArray:
            if (record["number"] == number):
                # Return an dict that's subscript-able
                # Nice Eh? 
                return ({"name" : record["name"], "number" : record["number"]})

                # Set boolean to True to enable other manipulation
                available = True

            else:
                pass
                # Adding anything here ruins this code
                
        if available == True:
            pass
        else:
            print("\nNumber doesn't exist!")


        

# Display function takes no parameters and returns
# response based on user_selection - For Simplification
def Display():
    print("###########################")
    print("###   MYPY PHONE BOOK   ###")
    print("###########################")
    print("1: Add New Entry")
    print("2: Delete Entry")
    print("3: Update Entry")
    print("4: Lookup Number")
    print("5: QUIT")
    try:
        response = int(input(">: "))
        return response
    except (ValueError):
        print ("\n\tEnter one of the numbers!\n")
    
# Simple function that grabs user input and makes it a string
def GetName():
    print("FullName: ")
    name = str(input()).lower()
    return name

# Simple function that grabs user input and makes it an integer
def GetNumber():
    print("Number: ")
    try:
        number = int(input())
    except ValueError:
        print("Enter Only Numbers!")
        return GetNumber()

    return number

# Main Driver Function
def MyPyFunction():
    # Initialization of objects of both classes 
    # with the default (empty) constructors
    individual = Individual()
    phone_book = PhoneBook()

    exit_signal = False
    while (exit_signal == False):
        display_response = Display()
        # This startJSON_link function resets the Program's 
        # own array that holds the content of the JSON file -> self.TotalArray[]
        phone_book.startJSON_link()

        if display_response == 1:
            name = GetName()
            number = GetNumber()
            # The set_detail function is only used during 
            # the add_entry selection
            individual.set_details(name, number)
            # Variable to hold the boolean value of the individual method 
            # save()
            try_save = individual.save()
            if (try_save == True):
                # When the operation is complete - the get_array 
                # method has been populated by the save function

                # Set the phone book to point to an individual object
                phone_book.set_person(individual)
                phone_book.Add_Phone_Entry(individual.get_array())
            else:
                print("\nCouldn't Save!\n")

        # Other responses utilize the GetName() and GetNumber() 
        # functions to simplify integer checking and avoid too many 
        # try-catch statements

        elif display_response == 2:
            name = GetName()
            number = GetNumber()
            phone_book.Delete_Entry(name, number)

        elif display_response == 3:
            name = GetName()
            number = GetNumber()
            phone_book.Update_Entry(name, number)

        elif display_response == 4:
            number = GetNumber()
            # Create array to retrieve dict from lookup
            array = phone_book.Lookup_Number(number)
            # Check if array is empty
            if (array != None):
                name = array["name"]
                number = array["number"]
                print("\n\n#################################")
                print("|Name|: \t{}".format(name))
                print("|Phone Number|: {}".format(number))
                print("#################################\n")

        elif display_response == 5:
            exit_signal = True

# Comment out this part of the code to let this work like a package
# MyPyFunction()