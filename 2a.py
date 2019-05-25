class point():
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __add__(self, p):
        return point(self.x + p.x, self.y + p.y)

    def __str__(self):
        return str("(" + str(self.x) + "," + str(self.y) + ")")

    def read(self):
        self.x, self.y = map(int, input("Enter x,y : ").split())

a = point()
b = point()
a.read()
b.read()
c = a + b
print(c)
