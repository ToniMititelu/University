import math
import random
import statistics
import matplotlib.pyplot as plt

'''
Genetic algorithm to find minimum of a function
f - function
N - population size
D - field of def
p - precision
p_cross - probability of crossover
p_mut - probability of mutation
nr - no of steps
'''

f = (-1, 1, 2)
D = (-1, 2)
N = 20
p = 6
p_cross = 0.25
p_mut = 0.01
nr = 50
l = math.ceil(math.log2((D[1]-D[0]) * 10**p))

def create_binary(l):
    binary = []
    for i in range(0, l):
        rand = random.random()
        if rand <= 0.5:
            binary.append('0')
        else:
            binary.append('1')
    return ''.join(binary)

def write_in_file(s, maxime, nr):
    s += f'\nEvolutia maximului\n'
    for i in reversed(maxime):
        s += f'{i}\n'

    with open('output.txt', 'w') as file:
        file.write(s)

    avg_maxime = []
    for i in range(1, nr):
        avg_maxime.append(statistics.mean(maxime[:i]))
    
    plt.plot(maxime[::-1])
    plt.show()

def get_x(D, X, l, p):
    return round(((D[1]-D[0])/(2**l - 1) * int(X, 2) + D[0]), p)

def get_f(f, D, X, l, p):
    x = get_x(D, X, l, p)
    return (f[0]*x**2 + f[1]*x + f[2])

def get_probabilities(suma, N, population):
    probabilities = []
    s = '\nProbabilitati selectie\n'
    for i in range(N):
        probabilities.append(population[i][2]/suma)
        s += f'cromozom {i+1} prob {probabilities[i]}\n'
    return probabilities, s

def get_intervals(probabilities, N):
    new_prob = [probabilities[0]]
    s = '\nIntervale prob selectie\n'
    for i in range(1, N):
        new = probabilities[i]
        for j in range(0, i):
            new = new + probabilities[j]
        new_prob.append(new)
        s += f'{new} '
    
    return new_prob, s

def help_func(N, intervals, u):
    for i in range(1, N):
        if u > intervals[i-1] and u < intervals[i]:
            return i

def selection(population, N, intervals):
    new_population = [k for k in population]
    s1, s2 = '', '\nDupa selectie\n'
    for i in range(N):
        u = random.random()
        j = help_func(N, intervals, u)
        if j:    
            new_population[i] = population[j]
        s1 += f'u={u} selectam crom {j}\n'
        s2 += f'{i+1}: {new_population[i][0]}, x={new_population[i][1]}, f={new_population[i][2]}\n'

    s = s1 + s2

    return new_population, s

def crossover(N, new_population, p_cross, l):
    s = f'\nProb de incrucisare {p_cross}\n'
    marked = []
    for i in range(N):
        u = random.random()
        if u < p_cross:
            marked.append((new_population[i], i))
            s += f'{new_population[i][0]} u={u} < {p_cross} -> participa\n'
        else:
            s += f'{new_population[i][0]} u={u}\n'

    if len(marked)%2 == 1:
        marked.pop()
    
    for i in range(1, len(marked)):
        u = random.randrange(0, l, 1)
        new_c_x = marked[i-1][0][0][0:u] + marked[i][0][0][u:]
        new_c_y = marked[i][0][0][0:u] + marked[i-1][0][0][u:]
        new_population[marked[i-1][1]][0] = new_c_x
        new_population[marked[i-1][1]][1] = get_x(D, new_c_x, l, p)
        new_population[marked[i-1][1]][2] = get_f(f, D, new_c_x, l, p)
        new_population[marked[i][1]][0] = new_c_y
        new_population[marked[i][1]][1] = get_x(D, new_c_y, l, p)
        new_population[marked[i][1]][2] = get_f(f, D, new_c_y, l, p)

    s += f'\nDupa recombinare\n'
    for i in range(N):
        s += f'{i+1}: {new_population[i][0]}, x={new_population[i][1]}, f={new_population[i][2]}\n'

    return new_population, s

def mutation(N, population, l, p_mut):
    s = f'\nprob de mutatie pt fiecare gena {p_mut}\nAu fost modificati crom:\n'
    for i in range(N):
        u = random.random()
        if u < p_mut:
            s += f'{population[i][0]}\n'
            k = random.randrange(0, l-1, 1)
            c = '1' if population[i][0][k] == '0' else '0'
            if k >= 0 and k < l:
                new_string = population[i][0][:k] + c + population[i][0][k+1:]
                population[i][0] = new_string
                population[i][1] = get_x(D, new_string, l, p)
                population[i][2] = get_f(f, D, new_string, l, p)
    
    s += f'Dupa mutatie:\n'
    for i in range(N):
        s += f'{i+1}: {population[i][0]}, x={population[i][1]}, f={population[i][2]}\n'    

    return population, s

def find_max(population):
    maxim = population[0][2]
    for i in range(1, len(population)):
        if maxim < population[i][2]:
            maxim = population[i][2]
    return maxim

def main():
    population = []
    for i in range(0, N):
        X = create_binary(l)
        x = get_x(D, X, l, p)
        population.append([X, x, get_f(f, D, X, l, p)])
    
    s = 'Prima populatie\n'

    for i in range(N):
        s += f'{i+1}: {population[i][0]}, x={population[i][1]}, f={population[i][2]}\n'
    

    maxime = []
    check = True
    for i in range(nr):
        suma = sum([c[2] for c in population])
        probabilities, s1 = get_probabilities(suma, N, population)
        intervals, s2 = get_intervals(probabilities, N)
        new_population, s3 = selection(population, N, intervals)
        crossover_population, s4 = crossover(N, new_population, p_cross, l)
        mut_population, s5 = mutation(N, crossover_population, l, p_mut)
        maxim = find_max(mut_population)      
        population = mut_population
        maxime.append(maxim)
        if check:
            s = s + s1 + s2 + s3 + s4 + s5
        check = False

    write_in_file(s, maxime, nr)


if __name__ == "__main__":
    main()