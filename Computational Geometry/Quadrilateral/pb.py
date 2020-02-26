import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'P({self.x}, {self.y})'

def coord_vect(p, q):
    return q.x - p.x, q.y - p.y

def scalar(a, b, l, m):
    return a*l + b*m

def norma(a, b):
    return math.sqrt((a**2 + b**2))

def cos(A, i, j, k):
    a, b = coord_vect(A[i], A[j])
    c, d = coord_vect(A[i], A[k])
    numarator = scalar(a, b, c, d)
    numitor = norma(a, b) * norma(c, d)
    return (numarator/numitor)

def orientation_counterclock(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)

    if val < 0:
        return True
    return False

def orientation_clock(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)

    if val > 0:
        return True
    return False

def check(A):
    if orientation_counterclock(A[0], A[1], A[2]):
        if orientation_counterclock(A[1], A[2], A[3]):
            return True
    elif orientation_clock(A[0], A[1], A[2]):
        if orientation_clock(A[1], A[2], A[3]):
            return True
    return False

def main():
    A = []
    A.append(Point(0, 0))
    A.append(Point(0, 1))
    A.append(Point(1, 0))
    A.append(Point(1, 1))

    if check(A):
        print(f'Punctele A1, A2, A3, A4 (in aceasta ordine) formeaza un patrulater convex')
        cos_A2 = cos(A, 1, 0, 2)
        cos_A4 = cos(A, 3, 0, 2)
        if math.acos(cos_A2) + math.acos(cos_A4) == math.pi:
            print('pe cerc')
        elif math.acos(cos_A2) + math.acos(cos_A4) < math.pi:
            print('exterior cerc')
        else:
            print('interior')
    else:
        print(f'Punctele A1, A2, A3, A4 (in aceasta ordine) nu formeaza un patrulater convex')


if __name__ == "__main__":
    main()