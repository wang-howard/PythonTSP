from Point import Point
from Tour import Tour

a = Point(621.0, 400.0)
b = Point(420.0, 512.0)
c = Point(411.0, 621.0)
d = Point(600.0, 621.0)
e = Point(400.0, 400.0)
f = Point(500.0, 500.0)

test = Tour()
test.insertNearest(a)
test.insertSmallest(b)
test.insertSmallest(c)
test.insertSmallest(d)
test.insertSmallest(e)
test.insertSmallest(f)

size = test.size()
print("Number of points = " + str(size))

length = test.length()
print("Tour length = " + str(length))
print("Tour:")
print(test)