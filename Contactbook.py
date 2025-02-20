class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name}, {self.phone}, {self.email}, {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if self.contacts:
            for contact in self.contacts:
                print(contact)
        else:
            print("No contacts found.")

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ")
        found = False
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                print(contact)
                found = True
        if not found:
            print("Contact not found.")

    def update_contact(self):
        name_to_update = input("Enter the name of the contact to update: ")
        found = False
        for contact in self.contacts:
            if contact.name.lower() == name_to_update.lower():
                found = True
                print(f"Found contact: {contact}")
                contact.name = input("Enter new name: ")
                contact.phone = input("Enter new phone number: ")
                contact.email = input("Enter new email: ")
                contact.address = input("Enter new address: ")
                print("Contact updated successfully.")
                break
        if not found:
            print("Contact not found.")

    def delete_contact(self):
        name_to_delete = input("Enter the name of the contact to delete: ")
        found = False
        for contact in self.contacts:
            if contact.name.lower() == name_to_delete.lower():
                found = True
                self.contacts.remove(contact)
                print(f"Contact {contact.name} deleted successfully.")
                break
        if not found:
            print("Contact not found.")

    def display_menu(self):
        while True:
            print("\nContact Book Menu:")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.display_menu()
