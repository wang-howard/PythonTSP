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
        current = self.first.next
        count = 1
        while (current != self.fist):
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
            first = p
            p.next = first
            return
        
        # keep track of closest point and its distnace to p
        closest = None
        minDist = float('inf')
        length = 0.0

        current = first
        while (True):
            length = current.point.distanceTo(p.point)
            if (length < minDist):
                minDist = length
                closest = current
            current = current.next
            if (current == self.first):
                break
        
        p.next = closest.next
        closest.next = p
    
    def insertSmallest(self, x):
        # create new node with point x
        p = Node(x)

        # insert as first if tour is empty
        if (self.first == None):
            first = p
            p.next = first
            return
        
        current = first;
        after = first;
        minIncrease = float('inf')
        increase = 0.0
        newDist = 0.0

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
    
