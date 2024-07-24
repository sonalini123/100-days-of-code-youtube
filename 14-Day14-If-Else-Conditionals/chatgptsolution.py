username = input("Enter username: ")
password = input("Enter password: ")

# Check credentials
if username == "admin":
    if password == "admin123":
        print("Access granted.")
    else:
        print("Invalid password.")
elif username == "user":
    if password == "user123":
        print("Access granted.")
    else:
        print("Invalid password.")
else:
    print("Invalid username.")