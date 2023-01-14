"""
Tour.py
Author: Howard Wang

Implementation of a Tour object class that includes two heuristics for
solving the Traveling Salesperson Problem. Neither are optimal nor
efficient heuristics but are simply examples of possible approaches to
the TSP. Takes no input and returns no output. 
"""

import math
from Point import Point

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

class Node:
    def __init__(self, pt):
        self.point = pt
        self.next = None
    def _repr__(self):
        return self.point

class Tour:
    def __init__(self):
        # initialize empty tour
        self.first = None
    
    def __repr__(self):
        if (self.first == None):
            return ""
        
        current = self.first
        points = ""
        while (True):
            points += str(current.point)
            current = current.next
            if (current == self.first):
                break
        return points
    
    def size(self):
        # return 0 for empty tour
        if (self.first == None):
            return 0
        
        # traverse linked list
        current = self.first.next
        count = 1
        while (current != self.first):
            count += 1
            current = current.next
        return count

    def length(self):
        if (self.first == None):
            return 0
        
        current = self.first
        length = 0.0
        while (True):
            length += current.point.distanceTo(current.next.point)
            current = current.next
            if (current == self.first):
                break
        return length

    def draw(self):
        if (self.first == None):
            return
        current = self.first
        while True:
            current.point.draw()
            current.point.drawTo(current.next.point)
            current = current.next
            if (current == self.first):
                break
    
    def insertNearest(self, x):
        # create new node
        p = Node(x)

        # if tour is empty, insert as first node
        if (self.first == None):
            self.first = p
            p.next = self.first
            return
        
        # keep track of closest point and its distance to p
        minDist = math.inf
        length = 0.0

        nearest = None
        current = self.first
        while (True):
            if (current.point.distanceTo(p.point) < minDist):
                minDist = length
                nearest = p
            current = current.next
            if (current == self.first):
                break
        
        p.next = nearest.next
        nearest.next = p
    
    def insertSmallest(self, x):
        # create new node with point x
        p = Node(x)

        # insert as first if tour is empty
        if (self.first == None):
            self.first = p
            p.next = self.first
            return
        
        current = self.first
        after = None
        minIncrease = math.inf
        increase = 0.0

        while (True):
            newDist = current.point.distanceTo(p.point) + current.next.point.distanceTo(p.point)
            increase = newDist - current.point.distanceTo(current.next.point)
            if (increase < minIncrease):
                minIncrease = increase
                after = current
            current = current.next

            if (current == self.first):
                break
        p.next = after.next
        after.next = p
