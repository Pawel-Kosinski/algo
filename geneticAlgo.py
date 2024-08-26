# Importowanie klas Population i Chromosome oraz funkcji set_const z odpowiednich modułów
from population import Population
from chromosom import Chromosome
from chromosom import set_const

# Ustawienie stałych używanych przez algorytm genetyczny
set_const(-20, 20, 25, 1000, 4)

# Inicjalizacja obiektu Chromosome, który będzie reprezentował osobniki w populacji10
chromosome = Chromosome(4)

# Inicjalizacja listy przechowującej najlepsze znalezione rozwiązania
best_solutions = []

# Utworzenie obiektu Population, który reprezentuje populację osobników
population = Population(chromosome)

groups = population.how_Many_Groups()

# Pętla ewolucji populacji przez 1000 generacji
for i in range(1000):
    # Znalezienie najlepszego rozwiązania w aktualnej populacji i dodanie go do listy best_solutions
    best_solutions = population.best_solution(i, best_solutions)

    # Ewolucja populacji - krzyżowanie i mutacja
    population.evolve(
        groups_Amount=groups,
        selection_Method='Tournament Selection',  # or 'Best Selection' or 'Roulette Selection'
        crossOver_Method='three_point',  # choose between 'one_point', 'two_point', 'three_point', etc.
        mutation_Method='Two Point Mutation',  # choose between 'Edge Mutation', 'One Point Mutation', etc.
        mutation_Probability=0.2  # or any other probability value
    )
# Wyświetlenie najlepszego znalezionego rozwiązania po zakończeniu ewolucji
population.print_best(best_solutions)