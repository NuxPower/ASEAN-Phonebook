# Array List implementation of Contacts
from Contact import Contact

class ContactList:
    """Contact List class that creates an array list of the phonebook.
    """

    def __init__(self, size: int = 50):
        """
            Create an array list of contacts with default storage size of 50.
        """
        self.phonebook = [None] * size
        self.size = 0

    def getSize(self):
        """
            Get the size of this contact list.
        """
        return self.size
    
    def first(self) -> Contact:
        """
            Get the first contact in this contact list.
            Returns none if the list is empty.
        """
        # Complete this Method
        if self.size == 0:
            return None
        
        return self.phonebook[0]

    
    def getLast(self) -> Contact:
        """
            Get the last contact in this contact list.
            Returns none if the list is empty.
        """
        # Complete this Method
        if self.size == 0:
            return None

        return self.phonebook[self.size - 1]


    def getContactAtIndex(self, index: int) -> Contact:
        """Gets the contact at given index in the contact linked list.
        Returns None if index is not found in the list.

        Args:
            index (int): Index to get in the contact linked list.

        Returns:
            Contact: Contact at index.
        """
        # Complete this Method
        if 0 <= index < self.getSize():
            return self.phonebook[index]
        else:
            return None



    
    def getContact(self, student_num: str) -> Contact:
        """Gets the contact based on given student number. Will return None
        if contact is not found.

        Args:
            student_num (str): Student number to base search from.

        Returns:
            Contact: Contact information.
        """
        # Complete this Method
        for contact in self.phonebook:
            if contact and contact.getStudentNumber() == student_num:
                return contact
        return None
    
    def getContactsBySurname(self, surname):
        """Returns a list of contacts with the given surname."""
        matching_contacts = [contact for contact in self.phonebook if contact and contact.getLName() == surname]
        return matching_contacts
    
    def isEmpty(self) -> bool:
        """
            Checks if contact list has no contacts.
        """
        return self.getSize() == 0
    
    def incrSize(self) -> None:
        """
            Increase the size of this contact list.
        """
        # Complete this Method
        # complte namani ah
        self.size += 1

    def decrSize(self) -> None:
        """
            Decrease the size of this contact list
        """
        self.size -= 1

    def __increasePhonebookSize(self) -> None:
        """
            Increases the size of this phonebook by two times.
        """
        # Complete this Method
        new_size = self.size * 2
        if new_size > 100:
            new_size = 100  # assuming the default maximum size is 100

        new_phonebook = [None] * new_size

        i = 0
        while i < self.size:
            new_phonebook[i] = self.phonebook[i]
            i += 1

        self.phonebook = new_phonebook

    def insert(self, c : Contact):
        """Inserts new contact at index point.

        Args:
            c (Contact): Contact to be inserted.
        """
        # Complete this Method
        if self.size == len(self.phonebook):
            self.__increasePhonebookSize()

        index = self.__findIndexInsertion(c)

        # Check if the contact already exists
        if index < self.size and Contact.compareNames(self.phonebook[index], c) == 0:
            print("Contact already exists!")

        else:
            # If the contact doesn't exist, insert it
            self.__adjustPhonebook(index, self.size, dir="f")  # Adjust the phonebook from index to size
            self.phonebook[index] = c
            self.incrSize()  # Increment the size


    def __findIndexInsertion(self, c: Contact) -> int:
        """Finds the index to insert from based on contact's
        last name, and first name if both have the same first names.

        Args:
            c (Contact): Contact to compare and to be inserted.

        Returns:
            int: Node insertion point for new contact.
        """
        # Complete this Method
        index = 0
        while index < self.size:
            contact = self.phonebook[index]
            if contact is not None:
                comparison_result = Contact.compareNames(contact, c)
                if comparison_result == 1:
                    return index
                elif comparison_result == 0:
                    comparison_result_fname = Contact.compareNames(contact, c, comparison_type=1)
                    if comparison_result_fname == -1:
                        return index
                    elif comparison_result_fname == 1:
                        return index + 1
            index += 1
        return self.size


    def __adjustPhonebook(self, start: int, end = int, dir: str = "f") -> None:
        """
        Adjusts the arrangement of this phonebook from start to end.

        Args:
            index (int): Index for adjustment.
            dir (str): Direction of adjustment:
                "f" -> Forward indexing adjustment. For example, element at index 0 takes the value of the element at index 1.
                "b" -> Backward indexing adjustment. For example, elemet at index 1 takes the value of the element at index 0.
        """
        # Complete this Method
        if dir == "f":
            i = end
            while i > start:
                self.phonebook[i] = self.phonebook[i - 1]
                i -= 1
        elif dir == "b":
            i = start
            while i < end:
                self.phonebook[i] = self.phonebook[i + 1]
                i += 1
        else:
            print("Invalid direction for adjustment! Use 'f' for forward or 'b' for backward.")
            return



        # step = 1 if dir == "f" else -1
        # current_index = start
        # while 0 <= current_index < end:
        #     self.phonebook[current_index + step], self.phonebook[current_index] = self.phonebook[current_index], self.phonebook[current_index + step]
        #     current_index += step



    def deleteContact(self, stdn: str) -> Contact:
        """Finds the contact based on their student number.
        Returns the deleted contact. Otherwise, returns -1 if not found.

        Args:
            stdn (str): Student number of contact to be deleted.

        Returns:
            Contact: Deleted contact, if found.
        """
        # Complete this Method
        i = 0
        while i < self.size:
            contact = self.phonebook[i]
            if contact and contact.getStudentNumber() == stdn:
                deleted_contact = self.phonebook[i]
                self.__adjustPhonebook(i, self.size - 1, dir="b")  # Change 'f' to 'b' for backward adjustment
                self.decrSize()
                self.phonebook[self.getSize()] = None
                return deleted_contact
            i += 1

        # Contact not found
        return None


            
    def __str__(self, f = None) -> str:
        """Prints every contact in this contact list.

        Args:
            f (list, optional): A list that filters which contact should
                be outputted. Defaults to None.

        Returns:
            str: Every contact in this contact list.
        """
        # Complete this method
        s = "<----Phonebook---->"
        if not self.isEmpty():
            for contact in self.phonebook:
                if contact and (f is None or contact.getNumericCountryCode() in f):
                    s += "\n" + str(contact)
        else:
            s += "\nThis phonebook is currently empty..."
        s += "\n<----End---->"
        return s
