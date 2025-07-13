import getpass

# Define global variables
login = True
# Login credentials
cred = {
    "usr": "admin",
    "pwd": "password123"
}

def add_student():
    pass

def calculate_grades():
    pass

def search_student():
    pass

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
            add_student()
        elif query == "2" or query.lower() == "calc":
            calculate_grades()
        elif query == "3" or query.lower() == "search":
            search_student()