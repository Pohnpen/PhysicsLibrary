# SI Unit for Physics class

class SIBaseUnit():
    quantity = None
    symbol = None
    value = None
    # prefix (standart 10**0)

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value} {self.symbol}"

    def __truediv__(self, other):
        return self.value / other.value

    def __mul__(self, other):
        return self.value * other.value

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Can not add different tpyes of units!")
        return self.value + other.value

class Meter(SIBaseUnit):
    quantity = "length"
    symbol = "m"

class Kilogram(SIBaseUnit):
    quantity = "mass"
    symbol = "kg"

class Second(SIBaseUnit):
    quantity = "time"
    symbol = "s"

class Kevin(SIBaseUnit):
    quantity = "temperature"
    symbol = "K"

class Ampere(SIBaseUnit):
    quantity = "current"
    symbol = "A"

class Mole(SIBaseUnit):
    quantity = "amount of substance"
    symbol = "mol"




if __name__ == "__main__":
    kg = Kilogram(53.2)
    sec = Second(10)
    print(kg * sec)
    print(kg / sec)  # kg.__truediv__(sec)
    #print(kg + sec)
    print(kg + kg)
