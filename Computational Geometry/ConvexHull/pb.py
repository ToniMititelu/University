class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
         return self.x < other.x

def left_index(points):
    min = 0
    for i in range(1, len(points)):
        if points[i].x < points[min].x:
            min = i
        elif points[i].x == points[min].x and points[i].y > points[min].y:
            min = i
    return min

def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)

    if val == 0:
        return 0 #coliniare
    elif val > 0:
        return 1 #clockwise
    else: 
        return 2 #counterclock

def coliniaritate(points):
    if orientation(points[0], points[1], points[2]) == 0:
        if orientation(points[1], points[2], points[3]) == 0:
            points.sort()
        else: 
            return False
    else:
        return False 
    return True  
    

def convex_hull(points, n):
    l = left_index(points)
    hull, coliniare = [], []

    p = l
    q = 0

    while True:
        hull.append(p)
        q = (p+1) % n
        for i in range(n):
            if(orientation(points[p], points[i], points[q]) == 2):
                q = i

        p = q
        if(p == l):
            break
    
    if len(hull) == 3:
        I = ''
        for each in hull:
            I += f'({str(points[each].x)}, {str(points[each].y)}) '
        print('I = ' + I)   
        for i in range(n):
            if i not in hull:
                point = points[i]
        print(f'J = ({point.x}, {point.y})')
    
    elif coliniaritate(points) == False:
        print(f'I = ({points[hull[0]].x}, {points[hull[0]].y}), ({points[hull[2]].x}, {points[hull[2]].y})')
        print(f'J = ({points[hull[1]].x}, {points[hull[1]].y}), ({points[hull[3]].x}, {points[hull[3]].y})')
    else:
        ok = coliniaritate(points)
        print(f'I = ({points[0].x}, {points[0].y}), ({points[3].x}, {points[3].y})')
        print(f'J = ({points[1].x}, {points[1].y}), ({points[2].x}, {points[2].y})')


def main():
    #points = [Point(0, 2), Point(3, 0), Point(0, 3), Point(0, 0)]
    #points = [Point(2, 2), Point(1, 1), Point(3, 3), Point(0, 0)]
    #points = [Point(0, 1), Point(1, 0), Point(1, 1), Point(0, 0)]
    points = [Point(0, 0), Point(2, 2), Point(3, 3), Point(1, 1)]
    convex_hull(points, len(points))

if __name__ == "__main__":
    main()
