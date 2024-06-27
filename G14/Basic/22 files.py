# name = input("Enter Name :")
# age = int(input("Enter Age :"))

# data = {}

# data["name"] = name
# data["age"] = age

# print(data)
try:
    with open("data.txt","r") as x:
        lines = x.readlines()
    # x = open("data.txt","r")
    # lines = x.readlines()
    # x.close()
except:
    print("File Not found")

new_list = []
for line in lines:
    line = line.replace("\n","")
    line = line.strip()
    line = line.split("_")

    # line[1] = int(line[1])
    new_list.append(line)

print(new_list)

# temp = []
# data = []
# for line in lines:
#     line = line.replace("\n","")

#     if line:
#         temp.append(line)
#     else:
#         data.append(temp)
#         temp = []

# data.append(temp)

# print(data)




name = input("Enter name to serach:")

for el in new_list:
    if el[0] == name:
        print("Age is",el[1])
        break