from ContactArray import ContactList
from Contact import Contact

MENUS = {
    "main": {
        1: "Store to ASEAN Phonebook",
        2: "Edit entry in ASEAN Phonebook",
        3: "Delete entry from ASEAN Phonebook",
        4: "View/Search ASEAN Phonebook",
        5: "Exit"
    },
    "views": {
        1: "Search by country",
        2: "Search by surname",
        3: "View all",
        4: "Go back to main menu"
    },
    "edit": {
        1: "Student Number",
        2: "Surname",
        3: "Gender",
        4: "Occupation",
        5: "Country Code",
        6: "Area Code",
        7: "Phone Number",
        8: "None - Go back to main menu"
    },
    "cc": {
        1: "Burma", # 856
        2: "Cambodia", # 855
        3: "Thailand", # 66
        4: "Vietnam", # 84
        5: "Malaysia", # 60
        6: "Philippines", # 63
        7: "Indonesia", # 62
        8: "Timor Leste", # 670
        9: "Laos", # 95
        10: "Brunei", # 673
        11: "Singapore", #65
        12: "All",
        0: "No More"
    }
}

def showMenu(target: str, inline :int = None):
    """Shows the target menu in the ASEAN Phonebook program.
    
    Args:
        target (str): Target menu to show. Refer to MENUS dictionary.
        inline (int): If not none, then will create an inline menu with n items each.
    """
    print("\n<-----Menu----->")
    i = 1 if inline != None else None
    for menu in MENUS[target]:
        out = "[{}]".format(menu)
        if inline != None and i == inline:
            out = "\n[{}]".format(menu)
        print("{} {}".format(out, MENUS[target][menu]), end= "\t" if inline != None else "\n")
        if i != None:
            i = 1 if i == inline else i + 1
        
def receiveContactInfo() -> Contact:
    """Cast several prompts for user to input about the
    contact's data.

    Returns:
       Contact: Contact object created based from data.
    """
    stdn = prompt("Enter student number: ")    
    lname = prompt("Enter surname: ")
    fname = prompt("Enter first name: ")
    occupation = prompt("Enter occupation: ")
    gender = prompt("Enter gender (M for male, F for female): ")
    cc = int(prompt("Enter country code: "))
    area = int(prompt("Enter area code: "))
    number = int(prompt("Enter number: "))
    return Contact(stdn,fname,lname,occupation,gender,cc,area,number)

def prompt(phrase: str) -> str:
    """Prompts an input to the user

    Args:
        phrase (str): Input phrase.

    Returns:
        str : Returns a string type of inputted value.
    """
    return input(phrase)

def convertChoices(choices: list) -> list:
    """Converts choices from the phonebook menu
    into proper country code value for accuracy purposes.

    Args:
        choices (list): Choices selected by user during prompt.

    Returns:
        list: Converted values of choices.
    """
    for i in range(0, len(choices)):
        match choices[i]:
            case 1:
                choices[i] = 856
            case 2:
                choices[i] = 855
            case 3:
                choices[i] = 66
            case 4: 
                choices[i] = 84
            case 5:
                choices[i] = 60
            case 6:
                choices[i] = 63
            case 7:
                choices[i] = 62
            case 8:
                choices[i] = 670
            case 9:
                choices[i] = 95
            case 10:
                choices[i] = 673
            case 11:
                choices[i] = 65
    return choices
                

if __name__ == "__main__":
    pb = ContactList()

    while True:
        showMenu("main")
        try:
            opt = int(input("Select Operation: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if opt == 1:
            while True:
                try:
                    stdn = int(input("Enter student number: "))
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
                    continue

                lname = input("Enter surname: ")
                lname_invalid = False
                for char in lname:
                    if not ('a' <= char <= 'z' or 'A' <= char <= 'Z' or char == ' ' or char == '\t'):
                        lname_invalid = True
                        break
                if lname_invalid:
                    print("Invalid input. Last name should not contain numbers.")
                    continue

                fname = input("Enter first name: ")
                fname_invalid = False
                for char in fname:
                    if not ('a' <= char <= 'z' or 'A' <= char <= 'Z' or char == ' ' or char == '\t'):
                        fname_invalid = True
                        break
                if fname_invalid:
                    print("Invalid input. First name should not contain numbers.")
                    continue

                occupation = input("Enter occupation: ")
                occupation_invalid = False
                for char in occupation:
                    if not ('a' <= char <= 'z' or 'A' <= char <= 'Z' or char == ' ' or char == '\t'):
                        occupation_invalid = True
                        break
                if occupation_invalid:
                    print("Invalid input. Occupation should not contain numbers.")
                    continue

                gender = input("Enter gender (M for male, F for female): ")
                if gender.upper() not in {'M', 'F'}:
                    print("Invalid input. Please enter 'M' for male or 'F' for female.")
                    continue


                while True:
                    try:
                        cc = int(input("Enter country code: "))
                        if cc in [856, 855, 66, 84, 60, 63, 62, 670, 95, 673, 65]:
                            break
                        else:
                            print("Invalid country code. Please enter a valid ASEAN country code.")
                    except ValueError:
                        print("Invalid input. Please enter a numeric value for the country code.")
                try:
                    area = int(input("Enter area code: "))
                    number = int(input("Enter number: "))
                except ValueError:
                    print("Invalid input. Please enter numeric values for area code and number.")

                contact = Contact(stdn, fname, lname, occupation, gender, cc, area, number)
                pb.insert(contact)
                
                add_new_entry = input("Contact added successfully! Do you want to add a new entry? (yes/no): ").lower()
                while add_new_entry not in ['yes', 'no']:
                    print("Invalid input. Please enter 'yes' or 'no'.")
                    add_new_entry = input("Do you want to add a new entry? (yes/no): ").lower()

                if add_new_entry == "yes":
                    print("Add a new Entry")
                    # Continue with the loop, prompting for a new entry
                elif add_new_entry == "no":
                    # Break out of the loop and go back to the main menu
                    break

        elif opt == 2:
            # Edit entry in ASEAN Phonebook
            if pb.size == 0:
                print("Phonebook is empty. Add a contact first.")
            else:
                while True:
                    showMenu("edit")
                    try:
                        edit_opt = int(input("Select Edit Operation: "))
                    except ValueError:
                        print("Invalid input. Please enter a valid integer.")
                        continue

                    if edit_opt == 8:
                        print("Going back to the main menu.")
                        break  # Break out of the loop and go back to the main menu


                    stdn = input("Enter student number to edit: ")

                    # If contact is not found, print a message and continue to the next iteration
                    if contact is None:
                        print("Contact not found.")
                        continue

                    if edit_opt == 1:
                        # Edit student number
                        new_stdn = input("Enter new student number: ")
                        contact.setStudentNumber(new_stdn)
                    elif edit_opt == 2:
                        new_lname = input("Enter new last name: ")
                        contact.setLName(new_lname)
                    elif edit_opt == 3:
                        # Edit occupation
                        new_occupation = input("Enter new occupation: ")
                        contact.setOccupation(new_occupation)
                    elif edit_opt == 4:
                        # Edit gender
                        new_gender = input("Enter new gender: ")
                        contact.setGender(new_gender)
                    elif edit_opt == 5:
                        # Edit country code
                        new_cc = int(input("Enter new country code: "))
                        contact.setCountryCode(new_cc)
                    elif edit_opt == 6:
                        # Edit area code
                        new_area = int(input("Enter new area code: "))
                        contact.setAreaCode(new_area)
                    elif edit_opt == 7:
                        # Edit number
                        new_number = int(input("Enter new number: "))
                        contact.setContactNumber(new_number)
                    else:
                        print("Invalid option.")

                    print("Edited contact:", contact)

        elif opt == 3:
            # Delete entry from ASEAN Phonebook
            stdn = input("Enter student number to delete: ")
            deleted_contact = pb.deleteContact(stdn)
            if deleted_contact:
                print("Deleted contact:", deleted_contact)
            else:
                print("Contact not found.")

        elif opt == 4:
            # View/Search ASEAN Phonebook
            showMenu("views")
            view_opt = int(input("Select View Operation: "))

            if view_opt == 1:
                # Search by country
                showMenu("cc")
                start_cc_opt = int(input("Select Start Country Code: "))
                end_cc_opt = int(input("Select End Country Code: "))
                start_cc_opt, end_cc_opt = convertChoices([start_cc_opt, end_cc_opt])

                if start_cc_opt == 12:
                    # View all
                    if pb.size == 0:
                        print("Phonebook is empty.")
                    else:
                        print(pb)
                else:
                    filtered_contacts = [contact for contact in pb.phonebook if contact and start_cc_opt <= contact.getNumericCountryCode() <= end_cc_opt]

                    if len(filtered_contacts) == 0:
                        print("No contacts found for the selected countries.")
                    else:
                        print("Here are the students from the selected countries: ")
                        for contact in filtered_contacts:
                            print(contact)
            elif view_opt == 2:
                # Search by surname
                surname = input("Enter surname to search: ")
                contact = pb.getContactBySurname(surname)
                if contact:
                    print(contact)
                else:
                    print("Contact not found.")
            elif view_opt == 3:
                # View all
                if pb.size == 0:
                    print("Phonebook is empty.")
                else:
                    print(pb)
            elif view_opt == 4:
                # Go back to the main menu
                pass
            else:
                print("Invalid option.")

        elif opt == 5:
            # Exit
            break
        else:
            print("Invalid option.")
