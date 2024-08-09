from colorama import Fore

# Define our Contact Class
class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

# Define our ContactBook Class
class ContactBook:
    def __init__(self):
        self.contacts = [
            Contact("Alice", "1234567890", "alice@email.com"),
            Contact("Bob", "9876543210", "bob@email.com")
        ]


    # Added ADD contact function
    def add_contact(self, name, phone_number, email):
        found_contact = False
        for contact in self.contacts :
            if contact.name.lower() == name.lower(): # check if contact is there 
                print(f"Contact '{name}' already exists")
                found_contact = True    # Since we found the contact lets make the bool set to true
                break
        
        # if found_contact has not been set to True then theres no dupe
        # So we can add it to the contact book
        if not found_contact:
            self.contacts.append(Contact(name, phone_number, email))
            print(f"Contact '{name}' added successfully.")


    # Fixed DISPLAY_ALL contact function
    def display_all_contacts(self):
        if self.contacts:
            print("All Contacts:")
            # Had to find some docs https://docs.python.org/3/howto/sorting.html
            sort_contacts = sorted(self.contacts, key=lambda contact: contact.name)
            for contact in sort_contacts:
                print("-------------------")
                print(f"Name: {contact.name}\nPhone: {contact.phone_number}\nEmail: {contact.email}\n")
        else:
            print("No contacts found.")

    # Added SEARCH contact function
    def search(self, name):
        found = False 
        for contact in self.contacts:
            if contact.name.lower() == name.lower(): # check if contact is there
                print(f"Contact found for {contact.name}\n Phone: {contact.phone_number}\n Email: {contact.email}")
                found = True #  Since we found the contact lets make the bool set to true
                break
        if not found:
            print(f"No contact found for {name}")
    
    # Added UPDATE contact function 
    def update_contact(self, name , phone_number , email ):
        for contact in self.contacts :
            if contact.name.lower() == name.lower(): # check if contact is there
                if phone_number:
                    contact.phone_number = phone_number
                if email:
                    contact.email = email 
                print(f"Updated '{name}' contact information")   
                return
        print("Contact not found")

    # Added DELETE contact functions
    def delete_contact(self, name):
        for contact in self.contacts :
            if contact.name.lower() == name.lower(): # check if contact is there
                self.contacts.remove(contact)
                print(f"Removed '{name}' contact information")   
                return
        print("Contact removed")

    # Added Number Validation function
    def phone_number_validation(self):
        # Keep them in a loop until they input a proper phone number
        while True:
            phone_number = input("Enter phone number: ")
            if phone_number.isdigit(): # check if the input is actually all digits
                return phone_number
            else:
                print("Invalid number please supply numerical value")
            

# Define our console ui
def main():
    contact_book = ContactBook()

    while True:
        # Print our UI options
        print("\n--- Contact Book Menu ---")
        print(f"{Fore.GREEN}1. Add New Contact{Fore.RESET}")
        print(f"{Fore.BLUE}2. Search Contacts{Fore.RESET}")
        print(f"{Fore.YELLOW}3. Update Contact{Fore.RESET}")
        print(f"{Fore.RED}4. Delete Contact{Fore.RESET}")
        print(f"{Fore.MAGENTA}5. Show all Contact{Fore.RESET}")
        print(f"{Fore.LIGHTBLACK_EX}0. Exit{Fore.RESET}")

        # Set the input data to our choice var
        choice = input(f"{Fore.BLUE}Enter your choice: {Fore.RESET}")

        # Check for the appropriate options and handle them accordingly
        if choice == "0":
            print(f"{Fore.RED}Exiting Contact Book. {Fore.RESET}Goodbye!")
            break
        elif choice == "1":
            name = input("Enter name: ")
            phone_number = contact_book.phone_number_validation()
            email = input("Enter email: ")
            contact_book.add_contact(name, phone_number, email)
        elif choice == "2":
            search_query = input("Who would you like to search for:")
            contact_book.search(search_query)
        elif choice == "3":
            print("Enter the new updated details please.")
            name = input("Enter name: ")
            phone_number = contact_book.phone_number_validation
            email = input("Enter email: ")
            contact_book.update_contact(name, phone_number, email)
        elif choice == "4":
            print("Enter the name of the contact to delete")
            name = input("Enter name: ")
            contact_book.delete_contact(name)
        elif choice == "5":
            contact_book.display_all_contacts()
        else:
            # if the choice input is not in the range of 0-5 or contains characters
            # print a error message
            if choice != ["0","1","2","3","4","5"]: 
                print(f"{Fore.RED}You have selected the wrong option!{Fore.RESET}")



# This is direct execution so when we execute the python script it will run our main()
# it will set a special variable name to main
if __name__ == "__main__":
    main() # This will run automatically when executed


