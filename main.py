"""
This is a game where I make a guest list and see how
many people are coming.
"""

guest_names = []


# create guest 
def add_guest():
    '''add guest name to the list.'''
    name = input("Add your ugly guest please: ").strip().title()
    
    guest_names.append(name)
    print("ugly guest added")


# change the guest
def modify_guest():
    """Update the name for an existing guest."""
    name = input("enter guest name to modify: ").strip().title()

    if name in guest_names:
        index = guest_names.index(name)
        new_name = input("enter new guest: ").strip().title()
        guest_names[index] = new_name
        print("Guest modified.")
    else:
        print("guest not found.")


# kick out guest 
def remove_guest():
    """Remove guest and kick them out."""
    name = input("Enter guest name to remove: ").strip().title()

    if name in guest_names:
        index = guest_names.index(name)
        guest_names.pop(index)
        print("guest removed.")
    else:
        print("guest not found.")


# sort guests by height
def sort_guest():
    sort = input("Enter 'a' guests alphabetically: ").strip().lower()

    if not guest_names:
        print("There are no guests in the list to sort.")
    elif sort == "a":
        print("Here are the guests sorted alphabetically:")
        for name in sorted(guest_names):
            print(name)
    else:
        print("invalid input aka your wrong!")


# show how many guest broke in to the party
def show_number_guests():
    print(f"total number of guests: {len(guest_names)}")


# show the invitations 
def show_invatations():
    if not guest_names:
        print("No guest in list !!!!!!!!!!!!!!!!!!!")
        return

    print("\nGuest Invitation List:")
    for i in range(len(guest_names)):
        print(f"{guest_names[i]}, you are invited to my amazing/ horrible dinner party!")


# check for duplicates
def check_duplicate():
    name = input("Enter name you want to check: ").strip().title()

    if name in guest_names:
        print("this name is already in the list!")
    else:
        print("This name is NOT in the list!!!!!!!!!!")


def main():
    """Main program loop."""
    print("Welcome to guest list creator!")

    while True:
        print("\n1. Add guest")
        print("2. modify guest")
        print("3. remove guest")
        print("4. sort guest")
        print("5. show number of guests")
        print("6. show invitations")
        print("7. check for duplicates")
        print("0. exit")

        choice = input("choose an option: ")

        if choice == "1":
            add_guest()

        elif choice == "2":
            modify_guest()

        elif choice == "3":
            remove_guest()

        elif choice == "4":
            sort_guest()

        elif choice == "5":
            show_number_guests()

        elif choice == "6":
            show_invatations()

        elif choice == "7":
            check_duplicate()

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
