
age = input("Age : ")


if age == "0":
    print(f"You aren't born")
elif age:
    print(f"You are {age} years old")
else:
    print("You didn't mention the age")


if not age:
    print("You didn't mention the age")
elif age == "0":
    print(f"You aren't born")
else:
    print(f"You are {age} years old")


if (age != "") and (age != "0"):
    print(f"You are {age} years old")
elif not age:
    print("You didn't mention the age")
else:
    print(f"You aren't born")