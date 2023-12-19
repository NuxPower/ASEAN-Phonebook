# Main Python File to run from
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
        opt = int(input("Select Operation: "))
        if opt == 1:
            # Store to ASEAN Phonebook
            contact = receiveContactInfo()
            pb.insert(contact)
        elif opt == 2:
            # Edit entry in ASEAN Phonebook
            # Implement this part based on your requirements
            if pb.size == 0:
                print("Phonebook is empty. Add a contact first.")
            else:
                showMenu("edit")
                edit_opt = int(input("Select Edit Operation: "))
                stdn = input("Enter student number to edit: ")
                
                # Find the contact
                contact = pb.getContact(stdn)

                # If contact is not found, print a message and continue to the next iteration
                if contact is None:
                    print("Contact not found.")
                    continue

                if edit_opt == 1:
                    # Edit student number
                    new_stdn = input("Enter new student number: ")
                    contact.setStudentNumber(new_stdn)
                elif edit_opt == 2:
                    # Edit surname
                    new_lname = input("Enter new surname: ")
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
                elif edit_opt == 8:
                    print("Going back to the main menu.")
                    # No need to edit anything, just break out of the edit loop
                    break
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
                cc_opt = int(input("Select Country Code: "))
                if cc_opt == 12:
                    # View all
                    print(pb)
                else:
                    # View by country
                    cc_opt = convertChoices([cc_opt])[0]
                    filtered_contacts = [contact for contact in pb.phonebook if contact and contact.getNumericCountryCode() == cc_opt]
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
                print(pb)
            elif view_opt == 4:
                # Go back to main menu
                pass
            else:
                print("Invalid option.")
        elif opt == 5:
            # Exit
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option.")
