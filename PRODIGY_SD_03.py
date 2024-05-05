import os

class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactManager:
    def __init__(self):
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists('contacts.txt'):
            with open('contacts.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    name, phone_number, email = line.strip().split(',')
                    contact = Contact(name, phone_number, email)
                    self.contacts.append(contact)

    def save_contacts(self):
        with open('contacts.txt', 'w') as file:
            for contact in self.contacts:
                file.write(f"{contact.name},{contact.phone_number},{contact.email}\n")

    def add_contact(self, name, phone_number, email):
        contact = Contact(name, phone_number, email)
        self.contacts.append(contact)
        self.save_contacts()
        print(f"Contact '{name}' added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")

    def edit_contact(self, index, name, phone_number, email):
        if 1 <= index <= len(self.contacts):
            contact = self.contacts[index - 1]
            contact.name = name
            contact.phone_number = phone_number
            contact.email = email
            self.save_contacts()
            print("Contact updated successfully!")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 1 <= index <= len(self.contacts):
            deleted_contact = self.contacts.pop(index - 1)
            self.save_contacts()
            print(f"Contact '{deleted_contact.name}' deleted successfully!")
        else:
            print("Invalid contact index.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("------------------------")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact_manager.add_contact(name, phone_number, email)

        elif choice == '2':
            contact_manager.view_contacts()

        elif choice == '3':
            index = int(input("Enter the index of the contact to edit: "))
            name = input("Enter updated name: ")
            phone_number = input("Enter updated phone number: ")
            email = input("Enter updated email address: ")
            contact_manager.edit_contact(index, name, phone_number, email)

        elif choice == '4':
            index = int(input("Enter the index of the contact to delete: "))
            contact_manager.delete_contact(index)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
