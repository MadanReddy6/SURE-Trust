# 2 friend are going out to eat, in total they have x money, they enter a restaurent and get a menu in the form of a list (just the prices) called menu
# we have to output the combination of 2 items that make the friends use up all the money

budget = 180
menu = [10, 20, 40, 80, 100, 140, 200]

done = False

for i in range(len(menu)):
    for j in range(i+1, len(menu)):

        total = menu[i] + menu[j]

        if total == budget:
            print(i, j)
            done = True
            break

    if done:
        break



