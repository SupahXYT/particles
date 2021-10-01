
class test:
    def __init__(self):
        self.x = 0

    def set_x(self, test, x):
        test.x = x

t = test()
a = test()

t.set_x(t, 4)

print(t.x)
