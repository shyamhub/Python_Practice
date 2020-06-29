class arithmetic_operations:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print(self.a + self.b)

    def sub(self):
        print(self.a - self.b)

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

opr1 = arithmetic_operations(4, 2)
opr1.add()
opr2 = arithmetic_operations(3,6)
opr2.sub()
