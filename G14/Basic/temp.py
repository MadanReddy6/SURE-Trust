class Human:
    def __init__(self, name, age, gender, job):
        self.name = name
        self.age = age
        self.gender = gender
        self.job = job

    
    def introduce(self):
        print(f"I'm {self.name}, and i am a {self.age} year old {self.job}")

    def __str__(self):
        return self.name

class Child(Human):
    def __init__(self, name, gender, standard):
        super().__init__(name, "", gender, "")
        self.standard = standard

    def introduce(self):
        print(f"I'm {self.name}, and i am in {self.standard} class")

    def __str__(self):
        return self.name + " " + self.standard

class Fireman(Human):
    def __init__(self, name, age, post):
        super().__init__(name, age, "", "")
        self.post = post

    def introduce(self):
        print(f"I'm {self.post} {self.name}")


class Nursery:
    def __init__(self, child_list):
        self.childs = child_list

    def __str__(self):
        x = ""

        for child in self.childs:
            x+= "\n"+ str(child)

        return x

x = Human("Ashu", 20, "M", "Instructor")
# x.introduce()
y = Fireman("Singham", 45, "Head Waterman")
# y.introduce()


z1 = Child("Baby", "F", "6th")
z2 = Child("ok", "M", "4th")
z3 = Child("name", "gender", "standard")

nur = Nursery([z1, z2, z3])


# print(z1)
print(nur)