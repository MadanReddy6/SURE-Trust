# while True:
#     try:
#         age = int(input("Enter your name :"))
#         print("I am",age,"years old")
#         break
#     except:
#         print("Wrong Input")


week = ("mon", "tues", "wed","thur", "fri", "sat", "sun")

while True:
    break
    try:
        i = int(input("Enter index :"))
        temp = week[i]
        print(temp)

        break
    except ValueError:
        print("Enter a valid number as input")
    except IndexError:
        print("Enter value from 0 to 6")
    except Exception as error:
        print("Error :",error)
    finally:
        print("Input :", i)


# try:
#     raise RuntimeError("Error Occured")
# except RuntimeError as r:
#     print(r)