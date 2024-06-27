



class Animal:
    feeding_types = ("omni","herbi","carni")
    blood_types = ("cold","hot")
    animal_types = ("mammal", "bird", "fish", "insect")

    def __init__(self,feeding,vertibrate,blood,species):
        if type(feeding)!=str:
            raise TypeError("feeding attribute must be a string")
        if feeding not in Animal.feeding_types:
            raise ValueError("Value of feeding must be one of" , Animal.feeding_types)

        try:
            vertibrate = bool(vertibrate)
        except:
            raise TypeError("vertibrate attribute must be convertible to boolean")

        if type(blood)!=str:
            raise TypeError("blood attribute must be a string")
        if blood not in Animal.blood_types:
            raise ValueError("Value of feeding must be one of" , Animal.blood_types)

        # if type(taxanomy)!=str:
        #     raise TypeError("taxanomy attribute must be a string")
        # if taxanomy not in Animal.animal_types:
        #     raise ValueError("Value of taxanomy must be one of" , Animal.animal_types)


        self.feeding = feeding
        self.is_vertibrate = vertibrate
        self.blood = blood
        self.species = species
        # self.taxanomy = taxanomy

    def __str__(self):
        return str(self.species)

# x = Animal("omni", "vertibrate", "hot")
# y = Animal("herbi", "vertibrate", "cold")
# z = Animal("carni", "vertibrate", "hot")

# z.blood = "neutral"

# Animal.feeding_types = ("heeeyy", "hiii")

