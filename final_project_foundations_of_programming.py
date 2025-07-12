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
    query = input("Choose Your Query Options (1,2,3 or add, calc or search) or type 'exit' to quit): \n"
    "[1] Adding students (add) \n[2] Calculating grades (calc)\n[3]Searching by ID or namen (search)\n")
    if query.lower() == "exit":
        print("Exiting the program. Goodbye!")
        break
    elif query not in ["1", "2", "3", "add", "calc", "search"]:
        print("Invalid option. Please choose a valid query option or type 'exit' to quit.")
        continue
    else:
        # Simulate processing the query
        print(f"Processing your query: {query}")
        
        if query == "1" or query.lower() == "add":
            add_student()
        elif query == "2" or query.lower() == "calc":
            calculate_grades()
        elif query == "3" or query.lower() == "search":
            search_student()