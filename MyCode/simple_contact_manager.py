# simple_contact_manager.py
class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def view_contacts(self):
        return self.contacts

if __name__ == "__main__":
    manager = ContactManager()
    while True:
        action = input("Choose action: add, remove, view, or quit: ").strip().lower()
        if action == 'add':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            manager.add_contact(name, phone)
        elif action == 'remove':
            name = input("Enter contact name to remove: ")
            manager.remove_contact(name)
        elif action == 'view':
            contacts = manager.view_contacts()
            print("Contacts:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        elif action == 'quit':
            break
