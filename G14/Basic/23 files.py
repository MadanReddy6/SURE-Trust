# read
with open("data.txt", "r") as file:
    data = file.read()
    print(data)

# rewrite
with open("data.txt", "w") as file:
    file.write(data + "\nname4 20 sleeping")

# append
with open("data.txt", "a") as file:
    file.write("\nname4 20 sleeping")

# read/append
with open("data.txt", "r+") as file:
    data = file.read()
    print(data)
    file.write("\nname4 20 sleeping")

# name = "name5"
# age = "20"
# hobby = "swimmming"

# print("Dont use _ (underscores) in the inputs")

# name = input("Name :")
# age = input("Age :")
# hobby = input("Hobby :")


# data = [name, age, hobby]


# def add_to_file(path, data):
#     x = "_".join(data)

#     with open(path, "a") as file:
#         file.write("\n"+ x)


# add_to_file("data.txt", data)
