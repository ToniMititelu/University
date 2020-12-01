import numpy as np
import math

def sub_desc(U, C, n):
    x = np.zeros(n)
    x[n-1] = C[n-1] / U[n-1, n-1]
    k = n-2
    while k:
        x[k] = (C[k] - sum([el for el in (U[k, k+1:] * C[k+1:])])) / U[k, k]
        k -= 1

    return x 

def sub_asc(U, C, n):
    x = np.zeros(n)
    x[0] = C[0] / U[0, 0]
    for k in range(1, n):
        l = (C[k] - sum(sum([el for el in (U[k, :k] * C[:k])]))) / U[k, k]
        x[k] = l

    return x


def gauss_pivotare_totala(matrice, termeni_liberi):
    n = matrice.shape[0]
    indici = np.arange(0, n)
    matricea_extinsa = np.concatenate((matrice, termeni_liberi), axis=1)

    for i in range(n-1):
        submatrice = matricea_extinsa[i:, i:n]

        # indicii elementului maxim din submatrice
        (index_linie, index_coloana) = np.unravel_index(np.argmax(submatrice), submatrice.shape)

        if submatrice[index_linie][index_coloana] == 0:
            print('Sist. incomp. sau comp. nedet.')
            return 

        # indicii in matricea mare
        index_linie, index_coloana = index_linie + i, index_coloana + i

        # Schimba linia
        if index_linie != i:
            matricea_extinsa[[i, index_linie]] = matricea_extinsa[[index_linie, i]]

        # Schimb coloana si indicii necunoscutelor
        if index_coloana != i: 
            matricea_extinsa[:, [i, index_coloana]] = matricea_extinsa[:, [index_coloana, i]]
            indici[[i, index_coloana]] = indici[[index_coloana, i]]

        # Modific matricea
        linie_curenta = matricea_extinsa[i, :]
        for j in range(i+1, n):
            m = matricea_extinsa[j, i] / matricea_extinsa[i, i]
            matricea_extinsa[j, :] = matricea_extinsa[j, :] - m * linie_curenta
    
    U = matricea_extinsa[:, :n]
    C = matricea_extinsa[:, n]

    return sub_desc(U, C, n)

# Exercitiul 1
def ex1():
    matrice = np.array([
        [0, -1, 5, 7], 
        [-1, -4, 1, -8], 
        [-4, -8, -4, -4], 
        [1, -2, -10, 7],
    ], dtype=float)

    termeni_liberi = np.array([[52], [-50], [-68], [-9]], dtype=float)

    det = np.linalg.det(matrice)

    if det == 0:
        print('Sist. incomp. sau comp. nedet.')
        return 

    print(gauss_pivotare_totala(matrice, termeni_liberi))


# Exercitiul 2
def ex2():
    matrice = np.array([
        [0, 8, 3, 6], 
        [8, 4, -9, -6], 
        [2, -2, 1, -1], 
        [8, 2, -5, -6],
    ], dtype=float)

    termeni_liberi = np.array([
        [1, 0, 0, 0], 
        [0, 1, 0, 0], 
        [0, 0, 1, 0], 
        [0, 0, 0, 1]
    ], dtype=float) 

    inversa = np.zeros(shape=matrice.shape)

    # Ca sa calculam inversa putem lua fiecare coloana din In si sa creeam sistemul Matrice * x = Coloana din In
    # Calculam astfel fiecare linie din Inversa
    for i, coloana in enumerate(termeni_liberi):
        inversa[i] = gauss_pivotare_totala(matrice, np.reshape(coloana, (-1, 1)))
        break

    inversa = inversa.T
    print(inversa)

# Exercitiul 3
def ex3():
    matrice = np.array([
        [0, -10, 8, -2], 
        [9, -1, 2, -6], 
        [5, 5, -1, 9], 
        [2, -7, 1, -1],
    ], dtype=float)

    termeni_liberi = np.array([
        [-12],
        [-3],
        [84],
        [-23]
    ])

    n = matrice.shape[0]
    indici = np.arange(0, n)
    matricea_extinsa = np.concatenate((matrice, termeni_liberi), axis=1)
    L = np.zeros((n, n))
    for i in range(n):
        L[i, i] = 1

    for i in range(n-1):
        coloana = matricea_extinsa[i:, i]

        # indicii elementului maxim de pe coloana
        index = np.argmax(np.abs(coloana))

        if coloana[index] == 0:
            print('A nu admite factorizarea LU')
            return

        # Schimba liniile
        if index != i:
            matricea_extinsa[[i, index]] = matricea_extinsa[[index, i]]
            L[[i, index]] = L[[index, i]]
            indici[[i, index]] = indici[[index, i]]

        # Modifica matricea 
        linie_curenta = matricea_extinsa[i, :]
        for j in range(i+1, n):
            m = matricea_extinsa[j, i] / matricea_extinsa[i, i]
            matricea_extinsa[j, :] = matricea_extinsa[j, :] - m * linie_curenta

        if matricea_extinsa[n-1, n-1] == 0:
            print('A nu admite factorizarea LU')
            return

    # Ne raman 2 sisteme triunghiulare.
    # L * y = _b, apelam sub_asc si rezultatul y il vom folosi pt a rezolva sistemul matrice * x = y
    # Rezultatul x este solutia sistemului initial
    _b = [termeni_liberi[wk] for wk in indici]
    y = sub_asc(L[:, :n], _b, n)
    return sub_desc(matricea_extinsa[:, :n], y, n)


# Exercitiul 4
def ex4():
    matrice = np.array([
        [9, 0, 9, 18],
        [0, 4, -2, 14],
        [9, -2, 74, -5],
        [18, 14, -5, 114],
    ], dtype=float)

    n = matrice.shape[0]
    L = np.zeros((n, n))

    # Verific daca exista descompunerea Cholesky
    if not (matrice == matrice.T).all():
        print('matrice asimetrica')
        return

    if np.linalg.det(matrice[:2, :2]) < 0 or np.linalg.det(matrice[:3, :3]) < 0:
        print('matricea nu e pozitiv definita')
        return

    alfa = matrice[0, 0]
    if alfa <= 0:
        print('matricea nu e pozitiv definita')
        return
    
    # Completez prima linie
    L[0, 0] = math.sqrt(alfa)
    for i in range(1, n):
        L[i, 0] = matrice[i, 0] / L[0, 0]
    
    # Restul
    for i in range(1, n):
        alfa = matrice[i, i] - sum([el**2 for el in L[i, :i]])
        if alfa <= 0:
            print('matricea nu e pozitiv definita')
            return

        L[i, i] = math.sqrt(alfa)
        for j in range(i+1, n):
            L[j, i] = (matrice[j, i] - sum([el for el in (L[j, :i] * L[i, :i])])) / L[i, i]
        
    print(L)

ex2()