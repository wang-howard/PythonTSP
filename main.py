from Point import Point
from Tour import Tour

a = Point(621.0, 400.0)
b = Point(420.0, 512.0)
c = Point(411.0, 621.0)
d = Point(600.0, 621.0)

tour = Tour(a, b, c, d)
e = Point(400, 400)
tour.insertNearest(e)
f = Point(500, 500)
tour.insertSmallest(f)

size = tour.size()
print("Number of points = " + str(size))
length = tour.length()
print("Tour length = " + str(length))