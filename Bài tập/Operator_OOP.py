class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.Simplify()

    def Simplify(self):
        GCD_Frac = self.GCD(self.numerator, self.denominator)
        self.numerator //= GCD_Frac
        self.denominator //= GCD_Frac

    def __add__(self, other):
        Numerator_New = self.numerator * other.denominator + self.denominator * other.numerator
        Denominator_New = self.denominator * other.denominator
        return Fraction(Numerator_New, Denominator_New)
    
    def __mul__(self, other):
        Numerator_New = self.numerator * other.numerator
        Denominator_New = self.denominator * other.denominator
        return Fraction(Numerator_New, Denominator_New)
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def GCD(self, a, b):
        if a == 0 : return b
        return self.GCD(b % a, a)
    
a = Fraction(1,4)
b = Fraction(2,4)

print(a*b)