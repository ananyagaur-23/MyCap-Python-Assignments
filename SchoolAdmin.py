import csv

def write_csv(data):
    with open('students.csv', 'a', newline='') as csvfile:
        fieldnames = ['Name', 'Age', 'Class', 'Gender']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow(data)

def read_csv():
    with open('students.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            print(row)

def main():
    print("Welcome to the School Administration Program!")
    print("1. Add student\n2. View all students")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        age = input("Enter age: ")
        grade = input("Enter class: ")
        gender = input("Enter gender: ")

        student_data = {'Name': name, 'Age': age, 'Grade': grade, 'Gender': gender}
        write_csv(student_data)

    elif choice == "2":
        read_csv()

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
