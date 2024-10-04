class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"


f1 = Fraction(1, 2)  # Дробь 1/2
f2 = Fraction(3, 4)  # Дробь 3/4

print(f"Сложение: {f1} + {f2} = {f1 + f2}")
print(f"Вычитание: {f1} - {f2} = {f1 - f2}")
print(f"Умножение: {f1} * {f2} = {f1 * f2}")
print(f"Деление: {f1} / {f2} = {f1 / f2}")
