


x, y = 3,10


# i = 1
# while True:
#     if ((i % x) == 0) and ((i % y) == 0):
#         break=
#     i+=1
# print(i)


i = 1

while ((i % x) != 0) or ((i % y) != 0):
    i+=1

print(i)



PIN = 3323
MAX_TRIES = 3
tries = 0


while True:
    if tries >= MAX_TRIES:
        print(f"Attempts exceeded max tries")
        break

    password = int(input("Enter your PIN:"))
    
    tries += 1


    if password == PIN:
        print ("Logged in...")
        break
    else:
        print(f"\nWRONG PIN, {MAX_TRIES - tries} tries left...")