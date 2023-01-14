"""
Point.py
Author: Howard Wang

Custom 2D point object class defining the only function that is
necessary for the Tour.py implementation to work properly. Takes no
values and returns no values.
"""

import math
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")\n"

    def distanceTo(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx ** 2 + dy ** 2)