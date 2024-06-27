

class Towel:
    size_options = ["Face Towel", "Body Towel", "Cleaning Towel", "Custom Towel"]

    def __init__(self, color, size, cloth = None, thickness=None, owner = None):
        if type(color) != str:
            raise Exception("Color must be a string")  
        if not color :
            raise Exception("Color must not be empty")
        self.color = color

        if size not in Towel.size_options:
            raise Exception(f"Size must be one of {Towel.size_options}")

        self.size = size
        self.cloth_type = cloth
        self.owner = owner

    def overview(self):
        if self.cloth_type:
            print(f"{self.cloth_type} {self.size} - {self.color}")
        else:
            print(f"{self.size} - {self.color}")



# mytowel1.overview()



class Human:
    gender_options = ["M","F","NA"]
    
    def __init__(this,name, age, gender):
        this.name = name
        this.age = age
        this.gender = gender

    def __str__(this):
        return f"Name - [{this.name}]"

    
h1 = Human("A" ,30, "M")

mytowel1 = Towel("Lime", "Face Towel", thickness=5, owner=h1)


print(mytowel1.owner.age)
