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
    
    def draw(self):
        plt.plot(self.x, self.y)
    
    def drawTo(self, other):
        plt.plot([self.x, other.x], [self.y, other.y])
