
class Card:
    suit_types = ("Spade", "Club","Heart","Diamond")
    def __init__(self, number, suit):
        if type(number) != int:
            raise Exception()
        if number>=1 and number<=13:
            pass
        else:
            raise Exception()

        if suit not in Card.suit_types:
            raise Exception()

        self.number = number
        self.suit = suit

        if suit in ("Diamond","Heart"):
            self.color = "Red"
        else:
            self.color = "Black"

        if number >= 11:
            self.is_face = True
        else:
            self.is_face = False

    def __str__(self):
        if self.number == 11:
            out = "Joker"
        elif self.number == 12:
            out = "Queen"
        elif self.number == 13:
            out = "King"
        elif self.number == 1:
            out = "Ace"
        else:
            out = self.number

        return f"{out} of {self.suit}s"

    def __add__(self,other):
        return self.number + other.number

    def __sub__(self,other):
        return self.number - other.number

    def __mul__(self,other):
        return self.number * other.number

    def __truediv__(self,other):
        return self.number/other.number

    def __len__(self):
        return len(self.suit)


    def __eq__(self,other):
        if self.number == other.number:
            if self.suit == "Spade":
                if other.suit == "Spade":
                    return True
                else:
                    return False
            else:
                if other.suit == "Spade":
                    return False
                else:
                    return True
        else:
            return False

    def __gt__(self,other):
        
        if self.number > other.number:
            if other.number == 1:
                return False
            return True
        elif self.number == other.number:
            if self.suit == "Spade":
                if other.suit == "Spade":
                    return False
                else:
                    return True
            else:
                return False
        else:
            if self.number == 1:
                return True
            return False

    def __le__(self,other):
        pass
    
a = Card(1, "Spade")
b = Card(12, "Heart")
c1 = Card(8, "Club")
c2 = Card(8, "Spade")
print(c2<c1)
print(b>a)
print(c2>a)
print(b>c1)