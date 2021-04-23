class addition:
    a = 0
    b = 0
    ans = 0
    def __init__(self, a , b):
        self.a = a
        self.b = b

    def show(self):
        print(self.a)
        print(self.b)
        return self.a + self.b 

p = addition(100,200)
print(p.show())