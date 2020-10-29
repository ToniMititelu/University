import math
import matplotlib.pyplot as plt
import numpy as np


# ex 1
# f(x) = x ** 2 - 11
# a = sqrt from the biggest perfect square that is smaller than 11 -> sqrt(9)
# b = sqrt from the smallest perfect square that is bigger than 11 -> sqrt(16)
# a = 3, b = 4 => f(a)*f(b) < 0
# expected: 3.3166247
# actual result with epsilon 10 ** -8: 3.3166247...


# ex 2
# f(x) = e ** (x - 2) 
# g(x) = cos(e ** (x - 2)) + 1
# see on plot that the intersection point is between 2 and 2.5
# make new function h(x) = f(x) - g(x) 
# a = 2, b = 2.5 => f(a)*f(b) < 0


def bisection_search(f, a, b, epsilon=1e-5):
    try:
        assert f(a) * f(b) < 0
    except AssertionError:
        return
    
    x_num = (a+b) / 2
    N = math.floor(math.log2((b - a) / epsilon) - 1) + 1
    i = 0
    while i < N:
        if f(x_num) == 0:
            return x_num
        elif f(a)*f(x_num) < 0:
            b = x_num
        else:
            a = x_num
        x_num = (a+b) / 2
        i += 1

    return x_num


def solve_eq_2(f, g, h):
    # Genereate points
    x = np.linspace(start=0, stop=5, num=100)

    # Create figure
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.plot(x, f(x), label='f(x) = e^(x-2)')
    plt.plot(x, g(x), label='g(x) = cos(e^(x-2)) + 1')
    plt.legend(loc='upper left')
    plt.show()

    # From figure -> intersection point between 2 and 2.5
    return bisection_search(h, 2, 2.5)


def pozitie_falsa(f, a, b, epsilon=1e-5):
    k, a_prim, b_prim = 0, a, b

    x = (a_prim * f(b_prim) - b_prim * f(a_prim)) / (f(b_prim) - f(a_prim))

    x_num = x

    while abs(x - x_num) / abs(x_num) < epsilon:
        k += 1

        if f(x_num) == 0:
            return x_num, k
        
        elif f(a_prim) * f(x_num) < 0:
            b_prim = x_num
            x = (a_prim * f(b_prim) - b_prim * f(a_prim)) / (f(b_prim) - f(a_prim))
        
        elif f(a_prim) * f(x_num) > 0:
            a_prim = x_num
            x = (a_prim * f(b_prim) - b_prim * f(a_prim)) / (f(b_prim) - f(a_prim))

    return x, k

def solve_eq_3(f):
    # Genereate points
    x = np.linspace(start=-5, stop=5, num=100)

    # Create figure
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.plot(x, f(x))
    plt.legend(loc='upper left')

    # From figure -> intervals [-4.5, -4), [0.5, 1.5), [3.5 , 4.5]
    (sol_1, _), (sol_2, _), (sol_3, _) = pozitie_falsa(f, -4.5, -4), pozitie_falsa(f, 0.5, 1.5), pozitie_falsa(f, 3.5, 4.5)
    print(f'x1={sol_1}, x2={sol_2}, x3={sol_3}')

    plt.scatter(sol_1, f(sol_1))
    plt.scatter(sol_2, f(sol_2))
    plt.scatter(sol_3, f(sol_3))
    plt.show()

def secanta(f, a, b, x0, x1, epsilon=1e-5):
    k, x_0, x_1 = 0, x0, x1

    while abs(x_1 - x_0) / abs(x_0) >= epsilon:
        k += 1
        x_num = (x_0 * f(x_1) - x_1 * f(x_0)) / (f(x_1) - f(x_0))
        x_0 = x_1
        x_1 = x_num
        
        if x_1 < a or x_1 > b:
            break
    
    return x_1, k


def solve_eq_4(f):
    # Genereate points
    x = np.linspace(start=-3, stop=3, num=100)

    # Create figure
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.plot(x, f(x))
    plt.legend(loc='upper left')
    plt.show()

    return


def main():
    f1 = lambda x : x ** 2 - 11
    f2 = lambda x : math.e ** (x - 2)
    f3 = lambda x : np.cos(math.e ** (x - 2)) + 1
    f4 = lambda x : f2(x) - f3(x)
    f5 = lambda x : x ** 3 - 21 * x + 20
    f6 = lambda x : x ** 3 + 3 * x ** 2 + 2 * x

    # print(f'EXERCITIUL 1: {bisection_search(f1, 3, 4, 1e-8)}')
    # print(f'EXERCITIUL 2: {solve_eq_2(f2, f3, f4)}')
    solve_eq_3(f5)

main()
