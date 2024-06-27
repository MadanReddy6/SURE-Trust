age = input("Enter your age : ") 
print(type(age))

age = int(age)
print(type(age))
# child / teen / adult

if age <= 4:
    print("Infant")
if (age > 4) and (age <=12):
    print("Kid")
if (age > 12) and (age <= 17):
    print("Teen")
if (age > 17) and (age <= 55):
    print("Adult")
if (age > 55):
    print("Old")


if age <= 4:
    print("Infant")
elif age <= 12:
    print("Kid")
elif age <= 17:
    print("Teen")
elif age <= 55:
    print("Adult")
else:
    print("Old")
