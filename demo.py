"""
Simple Gradebook App

Demonstrate list creation, indexing, membership testing,
modification, removal, and basic statistics.
"""


student_names = []
student_grades = []


def create_course():
    """Ask user for course name and return it."""
    return input("enter course name: ")


def add_student():
    """Add a single student with a initial grade."""
    name = input("Enter student name: ")
    grade = int(input("Enter student grade: "))

    student_names.append(name)
    student_grades.append(grade)


def update_grade():
    """Update the grade for an exsisting student."""
    name = input("enter student name to update: ")

    if name in student_names:
        index = student_names.index(name)
        new_grade = int(input("enter new grade: "))
        student_grades[index] = new_grade 
        print("Grade updated.")
    else:
        Print("student not found.")

def remove_student():
    """Remove a student and their grade."""
    name = input("Enter student name to remove: ")

    if name in student_names:
        index = student_names.index(name)
        student_names.pop(index)
        student_grades.pop(index)
        print("student removed.")
    else:
        print("student not found.")


def show_roster():
    """Display all students grades."""
    if not student_names:
        print("no students in the course.")
        
        return

    print("\nClass roster:")
    for i in range(len(student_names)):
        print(student_names[i], "-", student_grades[i])

def show_satistics():
    """Display class statistics."""
    if not student_grades:
        print("no grades availibale.")

        return 

    average = sum(student_grades) / len(student_grades)

    print("\nClass statistics: ")
    print("average:", round (average,2))
    print("Highest:", max (student_grades))
    print("lowest:", min(student_grades))



def main():
    """Main program loop."""
    course = create_course()
    print("n/Welcome to", course)

    while True:
        print("\n1 Add student")
        print("2 - Update grade")
        print("3 - Remove student")
        print("4 - Show Roster")
        print("5 - Show statistics")
        print("6 - Exit")

        choice = input("choose an ugly option: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            update_grade()
        
        elif choice == "3":   
            remove_student()

        elif choice == "4": 
            show_roster()

        elif choice == "5":
            show_satistics()

        elif choice == "0":
            break 

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()