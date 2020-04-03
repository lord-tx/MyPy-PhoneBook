import tkinter as tk
import MYPYPhoneBook as PhoneBook
from tkinter import messagebox

# This first set of commented-out code is a simplistic GUI 
# It just implements the LookUp function in a minimalistic
# manner

"""
win = tk.Tk()
win.title("Lookup Number")

search_entry_number = tk.IntVar()
search_entry = tk.Entry(win, width=20, textvariable=search_entry_number)
search_entry.grid(column=0, row=0, padx=10, pady=10)

def LookupContact(phone_number):
    print(phone_number)
    phonebook = PhoneBook.PhoneBook()
    details = phonebook.Lookup_Number(phone_number)
    name = details["name"]
    print (name)

search_button = tk.Button(win, text="Search", command=lambda: LookupContact(search_entry_number.get()))
search_button.grid(column=0, row=1, padx=10, pady=10)

result_sheet = tk.Label(win, width=10, height=5)
result_sheet.grid(column=0, row=3, padx=10, pady=10)
result_sheet.grid_forget()

win.mainloop()
"""

# This second set of commented out code is a BUILD-DESTROY kind
# of GUI where one window calls out another window but it becomes
# cluttered quickly

# It also fails to implement the LookUp function (I'm still trying
# to figure out why?)
"""
class GUILookUp(object):
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("LookUp Number")
        self.text = tk.StringVar()

        self.Look_up_frame = tk.Frame(self.win)
        self.Look_up_frame.grid()

        self.search_entry_number = tk.IntVar()
        self.search_entry = tk.Entry(self.Look_up_frame, width=20, textvariable=self.search_entry_number)
        self.search_entry.grid(column=0, row=0, padx=10, pady=10)
        self.search_entry.focus()

        self.search_button = tk.Button(self.Look_up_frame, text="Search", command= self.LookupContact)
        self.search_button.grid(column=0, row=1, padx=10, pady=10)

        self.result_sheet = tk.Label(self.Look_up_frame, textvariable=self.text)
        self.result_sheet.grid(column=0, row=3, padx=10, pady=10)
        self.result_sheet.grid_remove()

    def LookupContact(self):
        phone_number = self.search_entry_number.get()
        print(phone_number)
        phonebook = PhoneBook.PhoneBook()
        details = phonebook.Lookup_Number(phone_number)
        name = str(details["name"])
        # self.result_sheet.grid()
        # self.text.set("Name: " + name + "\n Phone Number: " + (str(details["number"])))

# lookup = GUILookUp()
# lookup.win.mainloop()

class GUIMENU(object):
    def __init__(self):
        self.gui_win = tk.Tk()
        self.gui_win.title("GUI MyPy PhoneBook")

        welcome = "\n\n--   MYPY PHONE BOOK   --\n\n"

        self.Welcome_Label = tk.Label(self.gui_win, text=welcome)
        self.Welcome_Label.grid()

        self.Add_Button = tk.Button(self.gui_win, text="Add New Entry")
        self.Add_Button.grid()

        self.Delete_Button = tk.Button(self.gui_win, text="Delete Entry")
        self.Delete_Button.grid()

        self.Update_Button = tk.Button(self.gui_win, text="Update Entry")
        self.Update_Button.grid()

        self.Lookup_Button = tk.Button(self.gui_win, text="Lookup Number", command=self.Lookup_Button)
        self.Lookup_Button.grid()

        self.Exit_Button = tk.Button(self.gui_win, text="Exit", command=quit)
        self.Exit_Button.grid()

    def Lookup_Button(self):
        lookup = GUILookUp()
        lookup.win.mainloop()

guimenu = GUIMENU()
guimenu.gui_win.mainloop()

"""

# This third implementation directly accesses the Tkinter class by inheriting
# directly from it and implementing other classes as frames

# It works perfectly. Except for the unimplemented parts.

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("MYPY Phone Book")
        self.resizable(0, 0)

        # self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MenuPage, GUILookUp, GUIAddEntry, GUIDeleteEntry, GUIUpdateEntry):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MenuPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        welcome = "\n\n--   MYPY PHONE BOOK   --\n\n"

        # These parts are kinda explanatory - We just create a bunch of labels
        # and buttons
        i = 0
        while i < 5:
            label = tk.Label(self, text="         ")
            label.grid(column=0, row = i)
            i += 1

        self.Welcome_Label = tk.Label(self, text=welcome)
        self.Welcome_Label.grid(column=2, row=0, columnspan=3, padx=10, pady=10)

        self.Add_Button = tk.Button(self, text="Add New Entry", command=lambda: controller.show_frame("GUIAddEntry"))
        self.Add_Button.grid(column=2, row=1, columnspan=3, padx=10, pady=10)

        self.Delete_Button = tk.Button(self, text="Delete Entry", command=lambda: controller.show_frame("GUIDeleteEntry"))
        self.Delete_Button.grid(column=2, row=2, columnspan=3, padx=10, pady=10)

        self.Update_Button = tk.Button(self, text="Update Entry", command=lambda: controller.show_frame("GUIUpdateEntry"))
        self.Update_Button.grid(column=2, row=3, columnspan=3, padx=10, pady=10)

        self.Lookup_Button = tk.Button(self, text="Lookup Number", command=lambda: controller.show_frame("GUILookUp"))
        self.Lookup_Button.grid(column=2, row=4, columnspan=3, padx=10, pady=10)

        self.Exit_Button = tk.Button(self, text="Exit", command=quit)
        self.Exit_Button.grid(column=2, row=5, columnspan=3, padx=10, pady=10)

    
    def Back(self):
        self.result_sheet.grid_remove()
        self.controller.show_frame("MenuPage")


class GUIAddEntry(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        button = tk.Button(self, text="Back", command=self.Back)
        button.grid(column=0, row=0, padx=10, pady=10)

        name_label = tk.Label(self, text="Name: ")
        name_label.grid(column=0, row=1, padx=10, pady=10)
        number_label = tk.Label(self, text="Number: ")
        number_label.grid(column=0, row=2, padx=10, pady=10)

        self.search_entry_name = tk.StringVar()
        self.search_entry_na = tk.Entry(self, width=20, textvariable=self.search_entry_name)
        self.search_entry_na.grid(column=1, row=1, padx=10, pady=10)
        self.search_entry_na.focus()

        self.search_entry_number = tk.IntVar()
        self.search_entry_no = tk.Entry(self, width=20, textvariable=self.search_entry_number)
        self.search_entry_no.grid(column=1, row=2, padx=10, pady=10)
        self.search_entry_number.set("")

        self.add_button = tk.Button(self, text="Add Contact", command=self.Add_Contact)
        self.add_button.grid(column=0, row=3, padx=10, pady=10, columnspan=2)

        self.text = tk.StringVar()
        self.result_sheet = tk.Label(self, textvariable=self.text)
        self.result_sheet.grid(column=0, row=4, padx=10, pady=10, columnspan=3)
        self.result_sheet.grid_remove()

    def Add_Contact(self):
        name = self.search_entry_name.get()
        phone_number = self.search_entry_number.get()
        # Save the details in a dictionary, the add contact function
        # takes a dictionary of details
        ind_array = {"name" : name, "number" : phone_number}

        # Create an instance (object) of the phonebook class
        phonebook = PhoneBook.PhoneBook()
        # Start the JSON link as usual
        phonebook.startJSON_link()
        result = phonebook.Add_Phone_Entry(ind_array)
        self.result_sheet.grid()
        if (result == "Successful"):
            self.text.set(result)
            self.search_entry_name.set("")
            self.search_entry_number.set("")
        else:
            total_result = result["error"] + "\n" +result["details"]
            self.text.set(total_result)
            self.search_entry_name.set("")
            self.search_entry_number.set("")

    def Back(self):
        self.result_sheet.grid_remove()
        self.controller.show_frame("MenuPage")


class GUIDeleteEntry(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        button = tk.Button(self, text="Back", command=self.Back)
        button.grid(column=0, row=0, padx=10, pady=10)

        name_label = tk.Label(self, text="Name: ")
        name_label.grid(column=0, row=1, padx=10, pady=10)
        number_label = tk.Label(self, text="Number: ")
        number_label.grid(column=0, row=2, padx=10, pady=10)

        self.search_entry_name = tk.StringVar()
        self.search_entry_na = tk.Entry(self, width=20, textvariable=self.search_entry_name)
        self.search_entry_na.grid(column=1, row=1, padx=10, pady=10)
        self.search_entry_na.focus()

        self.search_entry_number = tk.IntVar()
        self.search_entry_no = tk.Entry(self, width=20, textvariable=self.search_entry_number)
        self.search_entry_no.grid(column=1, row=2, padx=10, pady=10)
        self.search_entry_no.focus()

        self.delete_button = tk.Button(self, text="Delete Contact", command=self.Delete_Contact)
        self.delete_button.grid(column=0, row=3, padx=10, pady=10, columnspan=2)

        self.text = tk.StringVar()
        self.result_sheet = tk.Label(self, textvariable=self.text)
        self.result_sheet.grid(column=0, row=4, padx=10, pady=10, columnspan=3)
        self.result_sheet.grid_remove()
    

    def Delete_Contact(self):
        try:
            name = self.search_entry_name.get()
            phone_number = self.search_entry_number.get()
        except (_tkinter.TclError):
            print("Wrong Inputs")
        # Create an instance (object) of the phonebook class
        phonebook = PhoneBook.PhoneBook()
        # Start the JSON link as usual
        phonebook.startJSON_link()
        answer = self.Confirm_Change()
        self.result_sheet.grid()
        # Get a result from the Delete_Entry Function

        if (answer == True):
            result = phonebook.Delete_Entry(name, phone_number)
            self.text.set(result)
            self.search_entry_name.set("")
            self.search_entry_number.set("")
        else:
            pass

    def Confirm_Change(self):
        message_box = messagebox.askquestion("Proceed", "Do you really want to delete this contact?")
        if message_box == 'yes':
            return True
        else:
            return False

    def Back(self):
        self.result_sheet.grid_remove()
        self.controller.show_frame("MenuPage")


class GUILookUp(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        button = tk.Button(self, text="Back", command=self.Back)
        button.grid(column=0, row=0, padx=10, pady=10)

        self.search_entry_number = tk.IntVar()
        self.search_entry = tk.Entry(self, width=20, textvariable=self.search_entry_number)
        self.search_entry.grid(column=0, row=1, padx=10, pady=10)
        self.search_entry.focus()

        self.search_button = tk.Button(self, text="Search", command= self.LookupContact)
        self.search_button.grid(column=0, row=2, padx=10, pady=10)

        self.text = tk.StringVar()
        self.result_sheet = tk.Label(self, textvariable=self.text)
        self.result_sheet.grid(column=0, row=4, padx=10, pady=10)
        self.result_sheet.grid_remove()

    def LookupContact(self):
        phone_number = self.search_entry_number.get()
        print(phone_number)
        phonebook = PhoneBook.PhoneBook()
        details = phonebook.Lookup_Number(phone_number)
        name = str(details["name"])
        self.result_sheet.grid()
        self.text.set("Name: " + name + "\n Phone Number: " + (str(details["number"])))

    def Back(self):
        self.result_sheet.grid_remove()
        self.controller.show_frame("MenuPage")


class GUIUpdateEntry(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        button = tk.Button(self, text="Back", command=self.Back)
        button.grid(column=0, row=0, padx=10, pady=10)

        name_label = tk.Label(self, text="Name: ")
        name_label.grid(column=0, row=1, padx=10, pady=10)
        number_label = tk.Label(self, text="Number: ")
        number_label.grid(column=0, row=2, padx=10, pady=10)

        self.search_entry_name = tk.StringVar()
        self.search_entry_na = tk.Entry(self, width=20, textvariable=self.search_entry_name)
        self.search_entry_na.grid(column=1, row=1, padx=10, pady=10)
        self.search_entry_na.focus()

        self.search_entry_number = tk.IntVar()
        self.search_entry_no = tk.Entry(self, width=20, textvariable=self.search_entry_number)
        self.search_entry_no.grid(column=1, row=2, padx=10, pady=10)

        demacation_line = tk.Label(self, text="______________________________\n______________________________")
        demacation_line.grid(column=0, row=3, padx=10, pady=10, columnspan=3)

        new_name_label = tk.Label(self, text="New Name: ")
        new_name_label.grid(column=0, row=4, padx=10, pady=10)
        new_number_label = tk.Label(self, text="New Number: ")
        new_number_label.grid(column=0, row=5, padx=10, pady=10)

        self.search_entry_new_name = tk.StringVar()
        self.search_entry_new_na = tk.Entry(self, width=20, textvariable=self.search_entry_new_name)
        self.search_entry_new_na.grid(column=1, row=4, padx=10, pady=10)
        self.search_entry_new_na.focus()

        self.search_entry_new_number = tk.IntVar()
        self.search_entry_new_no = tk.Entry(self, width=20, textvariable=self.search_entry_new_number)
        self.search_entry_new_no.grid(column=1, row=5, padx=10, pady=10)

        self.update_button = tk.Button(self, text="Update Contact", command=self.Update_Contact)
        self.update_button.grid(column=0, row=6, padx=10, pady=10, columnspan=2)

        self.text = tk.StringVar()
        self.result_sheet = tk.Label(self, textvariable=self.text)
        self.result_sheet.grid(column=0, row=7, padx=10, pady=10, columnspan=3)
        self.result_sheet.grid_remove()
    

    def Update_Contact(self):
        try:
            name = self.search_entry_name.get()
            phone_number = self.search_entry_number.get()
            new_name = self.search_entry_new_name.get()
            new_number = self.search_entry_new_number.get()

            # Create an instance (object) of the phonebook class
            phonebook = PhoneBook.PhoneBook()
            # Start the JSON link as usual
            phonebook.startJSON_link()
            answer = self.Confirm_Change()
            self.result_sheet.grid()
            # Get a result from the Delete_Entry Function

            if (answer == True):
                result = phonebook.Update_Entry(name, phone_number, new_name, new_number)
                self.text.set(result)
                self.search_entry_name.set("")
                self.search_entry_number.set("")
            else:
                pass

        except tk.TclError:
            error_msg = messagebox.showerror("Wrong Input!", "Please enter only valid characters or numbers!")
            self.search_entry_number.set("")
            self.search_entry_new_number.set("")
            # print("Please Enter Only Valid Numbers") - Debugging purposes only


    def Confirm_Change(self):
        message_box = messagebox.askquestion("Proceed", "Do you really want to alter this contact?")
        if message_box == 'yes':
            return True
        else:
            return False

    def Back(self):
        self.result_sheet.grid_remove()
        self.controller.show_frame("MenuPage")

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()