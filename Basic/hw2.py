print("Rate these things")

hobbies = ["swiming","gaming","cricket"]
ratings = dict()


for hobby in hobbies:
    # make sure it is integer
    while True:
        try:
            rating = int(input("Rating for {} :".format(hobby)))
            ratings[rating] = hobby
            break
        except:
            print("Wrong Input")


while True:
# the key i is present in dict ratings
    try:
        i = int(input("Position u want to see based on rating :"))
        print(ratings[i])
        break
    except Exception as e:
        print("Wrong Input :",e)