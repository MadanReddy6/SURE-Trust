
x = [2, 4, 5, 2, 6, 7, 3, 6, 1, 3, 8, 7, 7]

while True:
    try:
        roll = input("Enter Roll NO.")
        roll = int(roll)
        marks = x[roll-1]
        break
    except KeyboardInterrupt:
        print("Bad input, we will output default marks for roll no. 1")
        roll = 1
        marks = x[roll]
        break
    except IndexError:
        print(f"The last Roll No. is {len(x)}")
    except ValueError:
        print(f"Please enter a valid number")
    except Exception as e:
        print(f"Unknown Error : {e}")
    
    print("Hello")


print(f"Marks for Roll No. {roll} are {marks}")