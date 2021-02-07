class Rectangle:
    def __init__(self, x, y, wedth, hight):
        self.x = x
        self.y = y
        self.wedth = wedth
        self.hight = hight

    def get_data(self):
        return (self.x, self.y, self.wedth, self.hight)

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def get_data(self):
        return "Circle " + str((self.x, self.y, self.r))

class Square:
    def __init__(self, x, y, a):
        self.x, self.y, self.a = x, y, a

    def get_data(self):
        return f"Square {self.x, self.y, self.a}"