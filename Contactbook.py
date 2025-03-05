import csv
# File where contacts are stored
CONTACTS_FILE = "contacts.csv"
class ContactBook:
    def __init__(self):
        """Initialize the contact book and load existing contacts from the CSV file."""
        self.load_contacts()

    def load_contacts(self):
        """Load contacts from the CSV file into a list."""
        try:
            with open(CONTACTS_FILE, mode="r", newline="") as file:
                reader = csv.reader(file)
                self.contacts = list(reader)  # Read contacts into a list
        except FileNotFoundError:
            self.contacts = []  # If the file does not exist, initialize an empty list

    def save_contacts(self):
        """Save the updated contacts list back to the CSV file."""
        with open(CONTACTS_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(self.contacts)  # Write all contacts to the file

    def add_contact(self):
        """Prompt user to enter contact details and add a new contact."""
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        # Check if the contact already exists
        for contact in self.contacts:
            if contact[0].lower() == name.lower():
                print("Contact already exists!")
                return

        # Add new contact and save to file
        self.contacts.append([name, phone, email, address])
        self.save_contacts()
        print("Contact added successfully.")

    def view_contacts(self):
        """Display all contacts in the contact book."""
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\nContacts List:")
            for contact in self.contacts:
                print(f"Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}, Address: {contact[3]}")

    def search_contact(self):
        """Search for a contact by name or phone number."""
        search_term = input("Enter name or phone number to search: ").lower()
        found = False
        for contact in self.contacts:
            if search_term in contact[0].lower() or search_term in contact[1]:
                print(f"Found Contact - Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}, Address: {contact[3]}")
                found = True
        if not found:
            print("Contact not found.")

    def update_contact(self):
        """Find a contact by name and update its details."""
        name_to_update = input("Enter the name of the contact to update: ")
        for i, contact in enumerate(self.contacts):
            if contact[0].lower() == name_to_update.lower():
                print(f"Current details: Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}, Address: {contact[3]}")
                # Get new details from the user
                new_phone = input("Enter new phone number: ")
                new_email = input("Enter new email: ")
                new_address = input("Enter new address: ")
                # Update contact and save changes
                self.contacts[i] = [contact[0], new_phone, new_email, new_address]
                self.save_contacts()
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self):
        """Delete a contact from the contact book."""
        name_to_delete = input("Enter the name of the contact to delete: ")
        for i, contact in enumerate(self.contacts):
            if contact[0].lower() == name_to_delete.lower():
                del self.contacts[i]  # Remove contact from list
                self.save_contacts()  # Save updated list to file
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

    def menu(self):
        """Display the menu and handle user input."""
        options = {
            "1": self.add_contact,
            "2": self.view_contacts,
            "3": self.search_contact,
            "4": self.update_contact,
            "5": self.delete_contact,
            "6": self.exit_program
        }
        while True:
            # Display menu options
            print("\nContact Book Menu:")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")

            # Get user's choice
            choice = input("Choose an option: ")

            # Execute corresponding function if choice is valid
            action = options.get(choice)
            if action:
                action()
            else:
                print("Invalid choice, please try again.")

    def exit_program(self):
        """Exit the program."""
        print("Exiting... Goodbye!")
        exit()
# Run the contact book application
if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.menu()
