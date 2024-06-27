x = {
    "fname":"Humpty",
    "lname":"Dumpty",
    "age" : 32,
    True : False,
    8.23 : [1,2,3,4,5],
    3 : None,
    None : {"hey", "there"},
    "age" : 23
}

# print(x[-1])
# print(x.get(-1, x[x.get(-1)] ))

# print(list(x.keys()))
# print(list(x.values()))
# print(list(x.items()))

# x["gender"] = "male"
y = {
    "rust":x,
    "list":x[8.23]
}

x["fname"] = "Ashwani"
x["lname"] = x["fname"]

# print(y["rust"]["fname"])


# print(x["fname"] + x["lname"])

# deep / shallow copy

del(x["fname"])

print(x)


#  list, tuple , dictionary , set