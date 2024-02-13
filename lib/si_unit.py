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

class Kelvin(SIBaseUnit):
    quantity = "temperature"
    symbol = "K"

class Ampere(SIBaseUnit):
    quantity = "current"
    symbol = "A"

class Mole(SIBaseUnit):
    quantity = "amount of substance"
    symbol = "mol"


class SIDerivedUnit(SIBaseUnit):
    si_unit_expression = None

    def __str__(self):
        return f"{self.value} {self.symbol} ({self.si_unit_expression})"

class Joule(SIDerivedUnit):
    quantity = "energy, work, heat"
    symbol = "J"
    si_unit_expression = "kg*(m**2/s**2)"

class Inch(SIDerivedUnit):
    quantity = "length"
    symbol = "in"
    si_unit_expression = "m/39.3700787"

class MeterPerSecond(SIDerivedUnit):
    quantity = "velocity"
    symbol = "m/s"
    si_unit_expression = "m/s" # Meter / Second

class JoulesPerKelvin(SIDerivedUnit):
    quantity = "heat"
    symbol = "J/K"
    si_unit_expression = "J/K"


if __name__ == "__main__":
    joule = Joule(1.0)
    print(joule) # 1.0 J (kg*(m**2/s**2))
    inch = Inch(1.0)
    print(inch) # 1.0 J (kg*(m**2/s**2))
