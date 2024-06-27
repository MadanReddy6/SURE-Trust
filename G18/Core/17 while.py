users = {
    "abc" : "1234",
    "fff" : "8912",
    "got" : "2205"
}

username = input("Username :")

while not users.get(username):
    print("Wrong Username\n")

    username = input("Username :")


correct_pin = users.get(username)

i = 0
while i < 5:
    pin_in = input("Password :")

    if correct_pin == pin_in:
        print("Logged in")
        i += 5
    else:
        print(f"Wrong PIN {4-i} tries remaining")
        i+=1
        if i>=5:
            print("Try again next time")