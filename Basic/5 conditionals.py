# age = int(input("Enter you age :"))

# # < > == != <= >=

# if age < 0:
#     print("Wrong Input Try Again")
# elif age <= 4:
#     print("You are an infant")
# elif age <= 14:
#     print("You are a Kid")
# elif age <= 18:
#     print("You are a Teenager")
# elif age <= 60:
#     print("You are an Adult")
# else:
#     print("You are old")

# height = float(input("Enter your height in cms:"))
# weight = float(input("Enter your weight in kgs:"))

# BMI = weight / (height/100)**2

BMI = 24.95

print(f"Your BMI is: {BMI}")


if BMI <=18.40:
    print("You are Under weight and have a healthy diet")
elif BMI <=24.9:
    print("You are Healthy and wishing you to continue it")
elif BMI <=29.9:
    print("You are Over weight and do exercise")
else:
    print("You are Obuse and include diet & exercise")