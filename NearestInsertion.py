"""
NearestInsertion.py
Author: Howard Wang

Takes a file from standard in containing coordinates of points to be
added to a tour using the nearest insertion heuristic. Prints the number
of points in the tour and the total length.
"""
from Tour.py import Tour
from Point import Point
fileName = input("Name of file: ")
tour = Tour()

with open(fileName, 'r') as f:
    for line in f:
        line = line.strip()
        coords = line.split(" ")

