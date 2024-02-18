class fraction:
    def __init__(self, numerator, denominator) -> None:
        self._numerator = numerator
        self._denominator = denominator
    
    def get_numerator(self):
        return self._numerator
    def get_denominator(self):
        return self._denominator
    
    def set_numerator(self, value):
        self._numerator = value
    def set_denominator(self, value):
        self._denominator = value

    def input_fraction(self):
        self._numerator = int(input("Enter for numerator: "))
        self._denominator = int(input("Enter for _denominator: "))

    def print_fraction(self):
        print(f"{self._numerator}/{self._denominator}")
    