import math
import matplotlib.pyplot as plt
import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(%s, %s)" % (self.x, self.y)


def orientation(p, q, r):
    ''' 
    0 --> p, q and r are colinear  
    1 --> Clockwise  
    2 --> Counterclockwise  
    '''
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)

    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2


def distance(P, Q):
    return math.sqrt((P.x - Q.x) * (P.x - Q.x) + (P.y - Q.y) * (P.y - Q.y))


def closestPoint(points, Q):
    ind = 0
    dist = 9999999
    for i in range(len(points)):
        if distance(points[i], Q) < dist:
            dist = distance(points[i], Q)
            ind = i
    return ind


A = []

with open("E:\Informatica\poligon.txt", "r") as file:
    for line in file:
        n, m = line.split()
        n, m = int(n), int(m)
        A.append(Point(n, m))

Q = Point(9, 9)

index1 = closestPoint(A, Q)
Index1 = index1 - 1
if Index1 == -1:
    Index1 = len(A) - 1

while orientation(Q, A[index1], A[Index1]) == 1:
    index1 -= 1
    if index1 == -1:
        index1 = len(A) - 1
    Index1 = index1 - 1
    if Index1 == -1:
        Index1 = len(A) - 1

index2 = closestPoint(A, Q)
Index2 = index2 + 1
if Index2 == len(A):
    Index2 = 0

while orientation(Q, A[index2], A[Index2]) == 2:
    index2 += 1
    if index2 == len(A):
        index2 = 0
    Index2 = index2 + 1
    if Index2 == len(A):
        Index2 = 0

# print(index1, index2)

i = index2
print(Q)
print(A[i])
while(i != index1):
    i += 1
    if i == len(A):
        i = 0
    print(A[i])


################################## AFISARE ##################################


fig, ax = plt.subplots()
ax.set_xlim((-10, 10))
ax.set_ylim((-10, 10))

for i in range(len(A)):
    ax.scatter(A[i].x, A[i].y, color="red")

for i in range(len(A) - 1):
    ax.plot([A[i].x, A[i + 1].x], [A[i].y, A[i + 1].y], color="blue")
ax.plot([A[i + 1].x, A[0].x], [A[i + 1].y, A[0].y], color="blue")

ax.scatter(Q.x, Q.y, color="green")

ax.plot([Q.x, A[index1].x], [Q.y, A[index1].y], color="magenta")
ax.plot([Q.x, A[index2].x], [Q.y, A[index2].y], color="magenta")

plt.show()
