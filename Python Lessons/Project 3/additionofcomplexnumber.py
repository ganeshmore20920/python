class complex:
    def __init__(self, real , imag ):
        self.real = real
        self.imag = imag

    def add(self, number):
        real = self.real + number.real
        imag = self.imag + number.imag
        result = complex(real,number)
        return result

n1 = complex(2,6)
n2 = complex(5,1)
result = n1.add(n2)
print(result.real)
print(*result.imag)