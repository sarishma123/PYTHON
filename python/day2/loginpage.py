# stored (database simulation)
stored_username = "sarishma"
stored_password = "sssss"

# user input
username = input("Enter username: ")
password = input("Enter password: ")

# step 1: check username exists
if username == stored_username:

    # step 2: check password only if username is correct
    if password == stored_password:
        print("Access Granted ✔ Welcome", username)
    else:
        print("Wrong password ❌")

else:
    print("User not found ❌")
    