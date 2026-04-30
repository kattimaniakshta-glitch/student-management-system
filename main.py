import json

FILE = "students.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f)

def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    students = load_data()
    students.append({"name": name, "age": age})
    save_data(students)
    print("Student added!")

def view_students():
    students = load_data()
    for i, s in enumerate(students, 1):
        print(f"{i}. {s['name']} - {s['age']}")

def delete_student():
    view_students()
    index = int(input("Enter number to delete: ")) - 1
    students = load_data()
    if 0 <= index < len(students):
        students.pop(index)
        save_data(students)
        print("Deleted!")

while True:
    print("\n1. Add  2. View  3. Delete  4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        break