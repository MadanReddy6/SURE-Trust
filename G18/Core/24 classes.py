from animal_module import Animal

# a1 = Animal("omni", True, "hot","Human")
# a2 = Animal("omni", True, "hot", "Human")

class Human(Animal):
    def __init__(self,name,country):
        super().__init__("omni",True,"hot","Human")
        self.name = name
        self.country = country

    def __str__(self):
        return self.name

h1 = Human("ashwani", "India")
# print(h1)

class Reptile(Animal):
    def __init__(self,species):
        super().__init__('carni',True,"cold",species)


x = Reptile("Lizard")

print(x.feeding)