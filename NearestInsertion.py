import matplotlib.pyplot as plt
import sys

from Point import Point
from Tour import Tour

with open('tsp8.txt') as tsp8:
    dimen = tsp8.readline()
    dimens = dimen.split(' ')
    dimens[1] = dimens[1].removesuffix('\n')
    width = int(dimens[0])
    height = int(dimens[1])
    plt.rcParams["figure.figsize"] = [width, height]
    plt.rcParams["figure.autolayout"] = True
    plt.autoscale(True)
    plt.grid(False)
    plt.axis('off')

    # Run smallest insertion heuristic
    tour = Tour()
    for line in tsp8:
        coords = line.split(' ')
        coords[1] = coords[1].removesuffix('\n')
        p = Point(float(coords[0]), float(coords[1]))
        tour.insertNearest(p)

tour.draw()
plt.text(20, 0, "length = " + str(tour.length()))
plt.show()