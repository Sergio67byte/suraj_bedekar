import json
    
class ContactBook:
    def __init__(self, filename):
             self.filename = filename
             self.contacts = self.load_contacts()
    
    def load_contacts(self):
        try:
             with open(self.filename, 'r') as f: 
                 contacts = json.load(f)
        except FileNotFoundError:
            contacts = {}
            return contacts
    
        def save_contacts(self):
            with open(self.filename, 'w') as f:
                json.dump(self.contacts, f, indent=4)
    
    def add_contact(self, name, phone_number, email):
        if name not in self.contacts:
            self.contacts[name] = {'phone': phone_number, 'email': email}
            self.save_contacts()
            print("Contact '{name}' added successfully.")
        else:
            print(f"Contact '{name}' already exists.")
    
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts [name]
            self.save_contacts()
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")
    
    def search_contact(self, name): 
        if name in self.contacts:
            print("Name: {name}")
            print(f"Phone: {self.contacts [name] ['phone']}")
            print(f"Email: {self.contacts [name]['email']}")
        else:
            print(f"Contact '{name}' not found.")
    
    def display_contacts(self):
        if self.contacts:
            print("Contacts:")
            for name in self.contacts:
                print(f" {name}: {self.contacts [name] ['phone']}, {self.contacts [name]['email']}")
        else:
            print("No contacts found.")
    
    def main():
        contact_book = ContactBook('contacts.json')
    
    while True:
        print("\nContact Book Menu:")
        print("1. Add a new contact")
        print("2. Search for a contact")
        print("3. Delete a contact")
        print("4. Display all contacts")
        print("5. Exit")
    
        choice = input("Enter your choice (1-5): ")
    
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact_book.add_contact(name, phone, email)
        
        elif choice == '2':
            name = input("Enter name to search: ")
            contact_book.search_contact(name)
    
        elif choice == '3':
             name = input("Enter name to delete: ")
             contact_book.delete_contact(name)
    
        elif choice == '4':
            contact_book.display_contacts()
    
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
    
        else:
             print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
