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

    # From figure => intersection point between 2 and 2.5
    return bisection_search(h, 2, 2.5)


def main():
    f1 = lambda x : x ** 2 - 11
    f2 = lambda x : math.e ** (x - 2)
    f3 = lambda x : np.cos(math.e ** (x - 2)) + 1
    f4 = lambda x : math.e ** (x - 2) - np.cos(math.e ** (x - 2)) - 1

    print(f'EXERCITIUL 1: {bisection_search(f1, 3, 4, 1e-8)}')
    print(f'EXERCITIUL 2: {solve_eq_2(f2, f3, f4)}')


main()
