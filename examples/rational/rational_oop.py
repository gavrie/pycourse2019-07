class Rational:

    def __init__(self, numerator, denominator):
        self.numer = numerator
        self.denom = denominator

    def __add__(self, other):
        return Rational(self.numer * other.denom + other.numer * self.denom,
                        self.denom * other.denom)

    def __repr__(self):
        return f"Rational({self.numer}, {self.denom})"

    def __str__(self):
        return "{}/{}".format(self.numer, self.denom)

    def _decimal(self):
        return float(self.numer) / self.denom
