class Dog:
    def __init__(self, name,s,a,c ):
        self.name = name
        self.species = s
        self.age = a
        self.color = c
        self.hobbies = []
        # x = 10

    def introduce(self):

        print(f"My dog's name is {self.name} he is a {self.age} year old {self.species}")
        if self.hobbies:
            print("and he likes to")
            for hobby in self.hobbies:
                print(hobby)


    def change_name(self,new_name):
        self.name = new_name

    def add_hobby(self,hobby):
        self.hobbies.append(hobby)



dog_1 = Dog("Sandy", "Husky", 6, "white")
dog_2 = Dog("Ruby", "Labrador", 9, "black")


# print(dog_1.name, dog_2.name)

# dog_1.introduce()
# dog_1.change_name("Jimmy")
# dog_1.introduce()

# dog_1.add_hobby("play catch")
# dog_1.add_hobby("take a bath")

# print(dog_1.hobbies)

# dog_1.introduce()

# print(type(dog_1))

# x = list([2,3,2,1])
# print(type(x))

# print(sum([3,5,2]))

# dog_2.introduce()

# dog_1.hello()


# class Book:
#     def __init__(self, title, cover_type, page_nums, cost, author,genre):



# class Pepsi:
#     def define(self, capicity, unit):
#         if unit == "ml":
#             self.capicity = capicity/1000
#         elif unit == "l":
#             self.capicity = capicity

# bottle_1 = Pepsi()
# bottle_1.define(2000, "ml")
# print(bottle_1.capicity)

# define(200, "l")



class int_list:
    def __init__(self,arr):
        for el in arr:
            if type(el) != int:
                return ValueError("This is not a int datatype")

        self.data = arr

    def sum(self):
        return sum(self.data)

x = int_list([3,4,2])

print(x.sum())


