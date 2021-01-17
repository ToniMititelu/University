import numpy as np
import matplotlib.pyplot as plt


EPSILON = 1e-5


# clasa ajutatoare
class Interval:
    def __init__(self, minim, maxim):
        self.minim = minim
        self.maxim = maxim

    def __str__(self):
        return f'({self.minim}, {self.maxim})'


def plot(puncte, h, f_, f__, interval: Interval):
    y_real = f_(puncte)
    y_approx = f__(puncte, h)

    plt.suptitle('Aproximarea derivatei a II-a')
    plt.plot(puncte, y_real, label='derivata secunda reala')
    plt.plot(puncte, y_approx, label='folosind formula de aproximare prin diferente finite centrale')
    plt.legend()
    plt.show()

    plt.suptitle('Eroarea de trunchiere')
    plt.plot(puncte, np.abs(y_real - y_approx))
    plt.hlines(EPSILON, xmin=interval.minim, xmax=interval.maxim)
    plt.show()


def eroare_trunchiere():
    return


def ex1():
    # Functia
    f = lambda x : np.cos(-0.6 * x)
    
    # Derivata secunda actuala
    f_ = lambda x : -0.36 * np.cos(0.6 * x)

    # Formula de aproximare prin diferente finite centrale
    f__ = lambda x, h : (f(x + h) - 2 * f(x) + f(x - h)) / h ** 2

    # Interval
    interval = Interval(-np.pi/2, np.pi)

    # Nr de puncte echidistante (ales 155 dupa mai multe incercari)
    N = 155
    puncte = np.linspace(interval.minim, interval.maxim, N+1)

    # diviziune echidistanta cu pasul h
    h = puncte[1] - puncte[0]

    plot(puncte, h, f_, f__, interval)


class Metode:
    DREPTUNGHI = 'dreptunghi'
    TRAPEZ = 'trapez'
    SIMPSON = 'Simpson'


def integrare(f, x, metoda):
    y = f(x)
    h = x[1] - x[0]
    
    # Un dict pt metodele de integrare
    metode = dict(
        dreptunghi=lambda x : 2 * h * np.sum(y[::2]),
        trapez=lambda x : h/2 * (y[0] + 2 * np.sum(y[1:-1]) + y[-1]),
        Simpson=lambda x : h/3 * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[1:-2:2]) + y[-1]),
    )

    return metode[metoda](x)


def ex2():
    s = 1.0

    # Functia
    f = lambda x : (np.e ** (-x ** 2 / 2 * s ** 2)) / (s * np.sqrt(2 * np.pi))

    # Interval
    interval = Interval(-10, 10)

    # Nr diviziuni
    N = 10

    # Puncte
    puncte = np.linspace(interval.minim, interval.maxim, N)

    print(f'Integrare prin metoda de cuadratura sumata a dreptunghiului: {integrare(f, puncte, Metode.DREPTUNGHI)}')
    print(f'Integrare prin metoda de cuadratura sumata a trapezului: {integrare(f, puncte, Metode.TRAPEZ)}')
    print(f'Integrare prin metoda de cuadratura sumata Simpson: {integrare(f, puncte, Metode.SIMPSON)}')

ex1()
ex2()
