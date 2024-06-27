
# function that takes 2 numbers as input and outputs their divison.

def division(x,y):

    try:
        out = x/y
        return out
    except Exception as error:
        print("Wrong Input for the functon")
        # print(error)
        


while True:
    try:
        x = float(input("No. 1 :"))
        y = float(input("No. 2 :"))
        div = x/y
        print(div)
        break
    except ZeroDivisionError as e:
        print("Denominator can't be zero")
    except ValueError as e:
        print("Please enter Numeric values only")
    except:
        print("Some Error")
    finally:
        print("Again")
    


def is_present(dictionary, key):
    try:
        dictionary[key]
        return True
    except:
        return False

x={
    "hi":1,
    0:"bye"
}







