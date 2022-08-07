ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'Ad31n15Tr@t012'
Username = input("Username: ")
Password = input("Password: ")
if Username == ADMIN_USERNAME and Password == ADMIN_PASSWORD:
    print("Welcome, admin.")
else:
    print("You are not admin.")