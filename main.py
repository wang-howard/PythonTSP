"""
main.py
Author: Howard Wang

Testing module to test Tour.py methods with a static set of coded
points. The value of the tour length is then compared to a Java
implementation of TSP that is confirmed to be correctly implemented.
"""

from Tour import Tour
from Tour import Point

a = Point(621.0, 400.0)
b = Point(420.0, 512.0)
c = Point(411.0, 621.0)
d = Point(600.0, 621.0)
e = Point(400.0, 400.0)
f = Point(500.0, 500.0)

test = Tour()

# before insertion
print("Before Insertion:")
print("Number of points = " + str(test.size()))
print("Tour length = " + str(test.length()))
print("Tour:")
print(test)

test.insertNearest(a)
test.insertNearest(b)
test.insertNearest(c)
test.insertNearest(d)
test.insertNearest(e)
test.insertNearest(f)

print("After Insertion:")
print("Number of points = " + str(test.size()))
print("Tour length = " + str(test.length()))
print("Tour:")
print(test)