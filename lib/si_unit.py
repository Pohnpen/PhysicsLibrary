# SI Unit for Physics class

from constants import PREFIX

class SIBaseUnit():
    SI_STANDARD_PREFIX = "normal" #(normal 10**0)
    quantity = None
    symbol = None

    def __init__(self, value, prefix="normal"):
        self.prefix = self.SI_STANDARD_PREFIX
        self.value = self.normalize(value, prefix)

    def normalize(self, value, to_prefix, from_prefix=None):
        if not from_prefix:
            from_prefix = self.prefix
        conversion = PREFIX[to_prefix]["factor"] / PREFIX[from_prefix]["factor"]
        return float(value * conversion)

    def cast(self, prefix):
        r = self.__class__(self.value)
        old_prefix = r.prefix
        r.prefix = prefix
        r.value = r.normalize(r.value, old_prefix, prefix)
        return r
        #return f'{self.normalize(self.value, prefix)} {PREFIX[prefix]["symbol"]}{self.symbol}'

    def __str__(self):
        return f'{self.value} {PREFIX[self.prefix]["symbol"]}{self.symbol}'

    def __truediv__(self, other):
        return self.__class__(self.value / other.value)

    def __mul__(self, other):
        return self.__class__(self.value * other.value)

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Can not add different tpyes of units!")
        return self.__class__(self.value + other.value)

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
        return f"{super().__str__()}  ({self.si_unit_expression})"
        #return f"{self.value} {self.symbol} ({self.si_unit_expression})"

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
    a = MeterPerSecond(2.5, "nano")
    print(a)
    print(a.cast("mega"))

    #b = Ampere(55.0, prefix="milli")
    #r = a / b
    #print(r)
    #print(r.cast("kilo"))
