import numpy as np
import matplotlib.pyplot as plt

EPSILON = 1e-7
norm = lambda x : np.linalg.norm(x, ord=2)


def plot_3d(f, X, Y):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.plot_surface(X, Y, f(X, Y))

    plt.show()


# Sylvester: se calculează toți determinanții formați din primele linii și primele coloane ale matricii; 
# dacă toți au valoare strict mai mare decât zero atunci matricea este pozitiv definită. 
def pozitiv_definita(A):
    return all([np.linalg.det(A[:i, :i]) > 0 for i in range(A.shape[0])])


# Trebuie sa fie simetrica si pozitiv definita
def are_punct_minim(A):
    return all([np.all(A == A.T), pozitiv_definita(A)])


# Se alege un punct x0 apropiat de minim (am ales P(-1, 1)) si 
# mergem in directia gradientului minimizand forma patratica a matricii A
def pasul_descendent(A, b):
    # Punct initial
    x = np.array([[-1], [1]])

    puncte = [x]

    residue = b - np.matmul(A, x)

    while norm(residue) > EPSILON:
        # Determin cât de mare trebuie să fie următorul pas
        lr = np.matmul(residue.T, residue) / np.matmul(np.matmul(residue.T, A), residue)
        x = x + lr * residue
        residue = b - np.matmul(A, x)
        puncte.append(x)

    print("Metoda pasului descendent - Punct de minim:", (x[0][0], x[1][0]))

    return puncte


# Se alege un punct x0 apropiat de minim (am ales P(-1, 1)) 
def gradienti_conjugati(A, b):
    # Punct initial
    x = np.array([[-1], [1]])
    puncte = [x]

    residue = b - np.matmul(A, x)
    d = residue

    while norm(residue) > EPSILON:
        lr = np.matmul(d.T, residue) / np.matmul(np.matmul(d.T, A), d)
        x = x + lr * d
        _residue = residue - lr * np.matmul(A, d)
        d_rate = np.matmul(_residue.T, _residue) / np.matmul(residue.T, residue)
        d = _residue + d_rate * d
        residue = _residue
        puncte.append(x)

    print("Metoda gradientilor conjugati - Punct de minim:", (x[0][0], x[1][0]))

    return puncte


def reprezentare_pe_graficul_curbelor_de_nivel(f, X, Y, puncte_pasul_descendent, puncte_gradienti_conjugati):
    plt.figure()

    cs = plt.contour(X, Y, f(X, Y))
    plt.clabel(cs)

    puncte_pasul_descendent = np.array(puncte_pasul_descendent)
    plt.plot(puncte_pasul_descendent[:, 0], puncte_pasul_descendent[:, 1], label='Pas descendent')

    puncte_gradienti_conjugati = np.array(puncte_gradienti_conjugati)
    plt.plot(puncte_gradienti_conjugati[:, 0], puncte_gradienti_conjugati[:, 1], label='Gradienti conjugati')

    plt.legend()
    plt.show()


def ex1():
    # Functia
    f = lambda x, y : 24.5 * (x ** 2) + 7 * x * y + 3 * x + 13 * (y ** 2) - 4 * y
    
    # afisarea 3d a functiei
    step = 0.25
    X, Y = np.mgrid[-2:2:step, -3:3:step]
    plot_3d(f, X, Y)
    
    # Derivatele pentru creeare matricilor
    dx = lambda x, y : 49 * x + 7 * y + 3
    dy = lambda x, y : 7 * x + 26 * y - 4

    # Matricile rezultate din derivatele partiale
    A = np.array([
        [49, 7],
        [7, 26],
    ], dtype=float)

    b = np.array([
        [3],
        [-4],
    ], dtype=float)

    # Verificam daca matricea admite punct minim
    if not are_punct_minim(A):
        print('Matricea nu admite punct minim')
        return

    print('Matricea admite punct minim')
    puncte_pasul_descendent = pasul_descendent(A, b)
    puncte_gradienti_conjugati = gradienti_conjugati(A, b)
    reprezentare_pe_graficul_curbelor_de_nivel(f, X, Y, puncte_pasul_descendent, puncte_gradienti_conjugati)


# clasa ajutatoare
class Interval:
    def __init__(self, minim, maxim):
        self.minim = minim
        self.maxim = maxim

    def __str__(self):
        return f'({self.minim}, {self.maxim})'


def err(y_real, y_approx, x_real, minim, maxim):
    eroare = np.abs(y_real - y_approx)
    eroare_maxima = np.max(eroare)

    plt.plot(x_real, eroare)
    plt.hlines(1e-5, xmin=minim, xmax=maxim)
    plt.hlines(eroare_maxima, label='Eroarea maximă', color='red', xmin=minim, xmax=maxim,)
    plt.legend()
    plt.show()


# functie pentru calcularea coeficientilor folosind metoda newton
def newton(N, x, y, k):
    return sum([y[i] * np.prod([(k - x[j])/(x[i] - x[j]) for j in range(N + 1) if i != j]) for i in range(N + 1)])


def ex2():
    # functia
    f = lambda x : 6 * np.sin(6 * x) + 1 * np.cos(4 * x) - 8.92 * x

    # intervalul pe care se lucreaza
    interval = Interval(-np.pi, +np.pi)

    # Gradul polinomului, 50 pentru o eroare cat mai mica
    N = 50
        
    x = np.linspace(interval.minim, interval.maxim, N+1)
    y = f(x)

    x_real = np.linspace(interval.minim, interval.maxim, 200)
    y_real = f(x_real)
    y_interpolat = [newton(N, x, y, t) for t in x_real]

    plt.figure()
    plt.plot(x_real, y_real, label='Funcția')

    plt.plot(x_real, y_interpolat, label='Polinomul de interpolare')

    plt.scatter(x, y, label='Nodurile de interpolare')

    plt.legend()
    plt.show()

    # eroare de trunchiere
    err(y_real, y_interpolat, x_real, interval.minim, interval.maxim)


# Putem afla b rezolvand sistemul 
def compute_b(N, x, a, h, dx):
    B = np.zeros((N + 1, N + 1))

    B[0, 0] = 1
    for i in range(1, N):
        B[i, i - 1] = 1
        B[i, i] = 4
        B[i, i + 1] = 1
    B[N, N] = 1

    W = np.zeros((N + 1, 1))
    W[0] = dx(x[0])
    for i in range(1, N):
        W[i] = 3 * (a[i + 1] - a[i - 1]) / h
    W[N] = dx(x[N])

    return np.linalg.solve(B, W)


# putem acum calcula c si d
def compute_c(N, a, b, h):
    c = np.zeros((N, 1))
    for i in range(N):
        c[i] = (3 * (a[i + 1] - a[i]) / h**2) - ((b[i + 1] + 2 * b[i]) / h)
    
    return c


def compute_d(N, a, b, h):
    d = np.zeros((N, 1))
    for i in range(N):
        d[i] = (- 2 * (a[i + 1] - a[i]) / h**3) + ((b[i + 1] + b[i]) / h**2)

    return d


def ex3():
    # Functia
    f = lambda x : np.sin(5 * x) + np.cos(-5 * x) - 21.54 * x

    # Derivata
    dx = lambda x : -5 * np.sin(5 * x) + 5 * np.cos(5 * x) - 21.54

    # Nr de subintervale, 200 pentru o eroare cat mai mica
    N = 200

    interval = Interval(-np.pi, +np.pi)

    x = np.linspace(interval.minim, interval.maxim, N+1)
    h = x[1] - x[0]

    a = f(x)
    b = compute_b(N, x, a, h, dx)
    c = compute_c(N, a, b, h)
    d = compute_d(N, a, b, h)

    # functie ajutatoare
    spline = lambda j : (lambda X : a[j] + b[j] * (X - x[j]) + c[j] * (X - x[j]) ** 2 + d[j] * (X - x[j]) ** 3)
    
    nr_puncte = 200
    x_real = np.linspace(interval.minim, interval.maxim, nr_puncte)
    y_real = f(x_real)
    
    # functie definita pe intervale
    y_aproximat = np.piecewise(
        x_real,
        [(x[i] <= x_real) & (x_real < x[i + 1]) for i in range(N - 1)],
        [spline(i) for i in range(N)]
    )
    plt.figure()
    plt.plot(x_real, y_real, label="Functia")
    plt.plot(x_real, y_aproximat, label="Interpolarea spline cubica")
    plt.scatter(x, a, label='Nodurile de interpolare')
    plt.legend()
    plt.show()
    
    # eroare de trunchiere
    err(y_real, y_aproximat, x_real, interval.minim, interval.maxim)

ex1()
ex2()
ex3()
