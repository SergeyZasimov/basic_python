class Complex:
    def __init__(self, number):
        self.rnumber, self.mnumber = Complex.separator(number)

    @staticmethod
    def separator(number):
        number = number.split('+')
        return int(number[0]), int(number[1][0])

    def __add__(self, other):
        return f'{self.rnumber + other.rnumber}+{self.mnumber + other.mnumber}i'

    def __mul__(self, other):
        rnum = self.rnumber * other.rnumber - self.mnumber * other.mnumber
        mnum = self.mnumber * other.rnumber + self.rnumber * other.mnumber
        return f'{rnum}+{mnum}i'

if __name__ == "__main__":
    num1 = Complex('5+6i')
    num2 = Complex('4+5i')
    print(num1 + num2)
    print(num1 * num2)