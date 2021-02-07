from task_c1_10_1 import Rectangle, Circle, Square

rect = Rectangle(5, 10, 50, 100)
circ = Circle(10,15,25)
sq = Square(34,65,23)

print("Rectangle " + str( rect.get_data()))
print("Rectangle", rect.get_data())

print(circ.get_data())

print(sq.get_data())