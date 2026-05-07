import os
import csv

file_name = "STUDENT.csv"

def create_file():
    if not os.path.exists(file_name):
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["name", "age", "marks", "subject"])

def add_student():
    name = input("Enter your name -> ")
    age = input("Enter your age -> ")
    marks = input("Enter your marks -> ")
    subject = input("Enter your subject -> ")

    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, age, marks, subject])

    print("Record inserted successfully")


def view_student():
    with open(file_name, 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)
def student_search():
    name = input("Enter the name to search -> ")
    found = False

    with open(file_name, 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0].lower() == name.lower():
                print("Found:", row)
                found = True

    if not found:
        print("Student not found")
# Update Student
def update_student():
    name = input("Enter name to change -> ")
    update_data = []
    found = False

    with open(file_name, 'r') as file:
        reader = csv.reader(file)

        for row in reader:

            if row[0].lower() == name.lower():

                print("Enter new details")

                age = input("Enter new age -> ")
                marks = input("Enter new marks -> ")
                subject = input("Enter new subject -> ")

                update_data.append([name, age, marks, subject])

                found = True

            else:
                update_data.append(row)

    if found:
        with open(file_name, 'w', newline='') as file:
             writer = csv.writer(file)
             writer.writerow(["name", "age", "marks", "subject"])
             writer.writerows(update_data)
        print("Record updated successfully")

    else:
        print("Student not found")


def delete_student():

    name = input("Enter name to delete -> ")

    new_data = []
    found = False

    with open(file_name, 'r') as file:

        reader = csv.reader(file)

        for row in reader:

            if row[0].lower() != name.lower():
                new_data.append(row)

            else:
                found = True

    if found:

        with open(file_name, 'w', newline='') as file:

            writer = csv.writer(file)
            writer.writerow(["name", "age", "marks", "subject"])
            writer.writerows(new_data)
        print("Record deleted successfully")

    else:
        print("Student not found")
def main():
    create_file()

    while True:
        print("\nWelcome to Student Management System")
        print("1. Add Student")
        print("2. View Student")
        print("3. Search Student")
        print("4. update Student")
        print("5. delete Student")
        print("6. Exit")

        choice = input("Enter your choice -> ").strip()

        if choice == '1':
            add_student()

        elif choice == '2':
            view_student()

        elif choice == '3':
            student_search()
        
        elif choice == '4':
            update_student()

        elif choice == '5':
             delete_student()

        elif choice == '6':
            print("Program Closed")
            break

        else:
            print("Invalid Choice")
if __name__ == "__main__":
  main()
