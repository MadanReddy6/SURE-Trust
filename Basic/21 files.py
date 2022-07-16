with open("data.txt","r") as data:
    data_list = data.readlines()

for i in range(len(data_list)):
    el = data_list[i]
    el = el.replace("\n", "")
    el = el.split(",")
    
    data_list[i] = el

print(data_list)


# username = "hi"
# password = "there"

# with open("data.txt","a+") as data:
#     data.write(f"{username},{password}\n")

