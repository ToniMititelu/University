class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'P({self.x}, {self.y})'
    
    def __lt__(self, other):
        if self.x != other.x:
            if self.x < other.x:
                return self
            return other
        if self.y < other.y:
            return self
        return other

    def __gt__(self, other):
        if self.x != other.x:
            if self.x < other.x:
                return other
            return self
        if self.y < other.y:
            return other
        return self 
    
    def __eq__(self, other):
        if self.x != other.x or self.y != other.y:
            return False
        return True
    
    def __ne__(self, other):
        if self.x == other.x and self.y == other.y:
            return False
        return True

def lin_eq(A, B):
    a = A.y - B.y
    b = A.x - B.x
    c = A.x*B.y - A.y*B.x
    return a, b, c

def cal_det(a1, b1, a2, b2):
    return a1*b2 - a2*b1

def cal_x(b1, c1, b2, c2, det):
    return ((-1)*c1*b2 - (-1)*c2*b1) / det

def cal_y(a1, c1, a2, c2, det):
    return ((-1)*c1*a2 - (-1)*c2*a1) / det

def main():
    A1 = Point(0, 0)
    A2 = Point(2, 2)
    A3 = Point(3, 3)
    A4 = Point(1, 1)

    a1, b1, c1 = lin_eq(A1, A2)
    a2, b2, c2 = lin_eq(A3, A4)

    det = cal_det(a1, b1, a2, b2)
    if det != 0:
        x = cal_x(b1, c1, b2, c2, det)
        y = cal_y(a1, c1, a2, c2, det)
        if (   (x < min(A1.x, A2.x) or x < min(A3.x, A4.x)) 
            or (x > max(A1.x, A2.x) or x > max(A3.x, A4.x))
            or (y < min(A1.y, A2.y) or y < min(A3.y, A4.y))
            or (y > max(A1.y, A2.y) or y > max(A3.y, A4.y))):
            print('Intersectia este multimea vida')
        else:
            print(f'Segmentele se intersecteaza in punctul {Point(x, y)}')
    else:
        if (((a1 * c2 - a2 * c1) != 0) or ((b1 * c2 - b2 * c1) != 0)):
            print('Intersectia este multimea vida')
        else:
            min1 = A1 < A2
            max1 = A1 > A2
            min2 = A3 < A4
            max2 = A3 > A4

            if min1 == min2 and max1 == max2:
                print('Segmente identice')
            elif (min1 < max2) != min1 or (min2 < max1) != min2:
                print('Intersectia este multimea vida')
            elif min1 == max2:
                print(f'Segmentele se intersecteaza in punctul {min1}')
            elif min2 == max1:
                print(f'Segmentele se intersecteaza in punctul {min2}')
            else:
                print(f'Intersectia este segmentul cu capetele {(min1 > min2)}, {(max1 < max2)}')

if __name__ == "__main__":
    main()
