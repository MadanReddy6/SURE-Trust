# CRUD
# creating
# retrieving
# updating
# deleting


# file = open("attendence.txt","w")
# attendence = {
#     "A" : 6,
#     "S"  : 4,
#     "P" : 5
# }

# data = []
# for key in attendence:
#     data.append(f"{key},{attendence[key]}")

# file.write("\n".join(data))
# file.close()

# with open("attendence.txt","r") as file:
#     data = file.read()
#     data = data.split("\n")
#     print(data)

name = "J"
days = 3

with open("attendence.txt", "a") as file:
    file.write(f"\n{name},{days}")

new_data = []

with open("attendence.txt", "r") as file:
    old_data = file.read().split("\n")

    for line in old_data:
        line = line.split(",")
        line[1] = str ( int(line[1]) + 1 )
        
        new_data.append(",".join(line))

with  open("attendence.txt", "w") as file:
    new_data = "\n".join(new_data)
    file.write(new_data)


# create a function which takes a name and a number as arguments and add them to the top of the file, if name is not already present

def add_user(name: str, atten:int , filename) -> None:
    pass

# delete user funciton
def pop_user(name: str , filename) -> ("name",0):
    pass
