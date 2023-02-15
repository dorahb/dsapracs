def create_user():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    password2 = input("Enter the password again: ")
    if password == password2:
        print("Your account has been created!")
    else:
        print("Your passwords do not match!")
        create_user()


