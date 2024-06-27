
def get_full_name(first_name = None, middle_name = None, last_name=None):
    
    full_name = ""

    if first_name:
        full_name += first_name
    else:
        return Exception("FIRSTNAME REQUIRED")
    
    if middle_name:
        full_name += middle_name

    if last_name:
        full_name += last_name
    
    return full_name

# print(get_full_name(last_name="Ahlawat", middle_name="Ashwani"))


# recreate mean, count, index function on your own using loops that take lists as input

def total(list):
    x = 0
    
    for  el in list:
        x += el

    return x


x = 5

def change(y):
    global x
    y += 3

# print(x)

change(x)

print(x)