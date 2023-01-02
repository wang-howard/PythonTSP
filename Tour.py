import matplotlib.pyplot as plt
import numpy as np

from Point import Point

class Node:
    def __init__(self, pt):
        self.point = pt
        self.next = None
    def _repr__(self):
        return self.point

class Tour:
    def __init(self):
        # initialize empty tour
        Tour.first = None
    
    def size(self):
        # return 0 for empty tour
        if (self.first == None):
            return 0
        
        # traverse linked list
        current = self.first
        count = 0
        while (current != None):
            count += 1
            current = current.next
        return count

    def draw(self):
        if (self.first == None):
            return
        current = self.first
        while (current != None):
            current.point.draw()
            current.point.drawTo(current.next.point)
            current = current.next
        
    



