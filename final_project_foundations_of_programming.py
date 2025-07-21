import getpass
from time import sleep

# Define global variables
fp = "students.txt"
login = True
# Login credentials
cred = {
    "usr": "admin",
    "pwd": "password123"
}

## Add student to the record if the student is not in the record
## If successfully added, then print student added
## If already exists, then print student already exists

def add_student(student_id, name, grades, path="students.txt"):
    # Read existing IDs
    existing_ids = set()
    with open(path, "r") as file:
        next(file)  
        for line in file:
            parts = line.strip().split(", ")
            if parts:
                existing_ids.add(parts[0])

    # Add new student if not exists
    if student_id not in existing_ids:
        with open(path, "a") as file:
            file.write(f"{student_id}, {name}, {grades}\n")
        print(f"Student {student_id} added.")
    else:
        print(f"Student {student_id} already exists.")

def calculate_grades(path="students.txt"):
    with open(path, "r") as file:
        next(file)  # Skip header
        for line in file:
            parts = line.strip().split(", ", 2)  # Split into 3 parts: id, name, grade
            student_id = parts[0]
            name = parts[1]
            grades_str = parts[2].strip("[]")  # Remove square brackets
            grades = [int(g) for g in grades_str.split(",")]  # Split by comma, convert to int
            avg_score = sum(grades) / len(grades)
            print(f"{student_id}, {name}, Average Score: {avg_score:}")

##Search student using student_id 
##If found, then print student record with id, name and grade
## If not found, then print student not found
    
def search_student(student_id, path="students.txt"):
    with open(path, "r") as file:
        header = file.readline().strip()
        for line in file:
            parts = line.strip().split(", ")
            if parts[0] == student_id:
                print(header)
                print(line.strip())
                return
    print(f"Student with ID {student_id} not found.")

# Function to classify grades
# Parameter: grade (int)
# Returns: classification (str)
# Description: This function classifies grades into A, B, C, D, or F
def grade_classification(grade:int) -> str:
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"

# Init file and write header if it doesn't exist
try:
    with open(fp, "x") as file:
        file.write("id, name, grade\n")
except FileExistsError:
    with open(fp, "w") as file:
        # Write header
        file.write("id, name, grade\n")
        
        # Write student records
        students = [
            {"id": "S1001", "name": "Alice", "grade": [85, 78, 92]},
            {"id": "S1002", "name": "Bob", "grade": [86, 79, 93]},
            {"id": "S1003", "name": "Cathy", "grade": [80, 81, 82]}
        ]
        
        for student in students:
            line = f"{student['id']}, {student['name']}, {student['grade']}\n"
            file.write(line)

# Login
while login:
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    if username == cred["usr"] and password == cred["pwd"]:
        print("Login successful!")
        login = False
    else:
        print("Invalid username or password. Please try again.")

# Define a query loop
while True:
    qs_int = {
        "1": "Adding students",
        "2": "Calculating grades",
        "3": "Searching by ID or name"
    }
    qs_str = {
        "add": qs_int["1"],
        "calc": qs_int["2"],
        "search": qs_int["3"]
    }
    query = input("Choose Your Query Options (1,2,3 or add, calc or search) or type 'exit' to quit): \n"
    f"[1] {qs_int['1']} (add) \n[2] {qs_int['2']} (calc)\n[3] {qs_int['3']} (search)\n")
    if query.lower() == "exit":
        print("Exiting the program. Goodbye!")
        break
    elif query.lower() not in ["1", "2", "3", "add", "calc", "search"]:
        print("Invalid option. Please choose a valid query option or type 'exit' to quit.")
        continue
    else:
        # Processing the query
        print(f"You selected: {qs_int.get(query, qs_str.get(query.lower()))}")
        
        if query == "1" or query.lower() == "add":
            input_id = input("Enter student ID (S1001, S1002, etc.): ")
            input_name = input("Enter student name: ")
            input_grades = input("Enter student grades (comma-separated): ")
            input_grades = [int(grade.strip()) for grade in input_grades.split(",")]
            add_student(input_id,input_name, input_grades, path=fp)
        elif query == "2" or query.lower() == "calc":
            print("Calculating grades for all students...")
            calculate_grades()
        elif query == "3" or query.lower() == "search":
            input_id = input("Enter student ID to search: ")
            search_student(input_id, path=fp)
    print("-" * 20)
    sleep(1)  

