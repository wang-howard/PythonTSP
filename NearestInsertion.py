"""
NearestInsertion.py
Author: Howard Wang

Takes a file from standard in containing coordinates of points to be
added to a tour using the nearest insertion heuristic. Prints the number
of points in the tour and the total length.
"""

from Tour import Tour
from Tour import Point

tour = Tour()

fileName = input("Name of file: ")
with open(fileName, 'r') as f:
    for line in f:
        line = line.strip()
        coords = line.split(" ")
        p = Point(float(coords[0]), float(coords[1]))
        tour.insertNearest(p)

print("Number of Points: " + str(tour.size()))
print("Tour Length: " + str(tour.length()))
print(tour)
