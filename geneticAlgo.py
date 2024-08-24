# Importowanie klas Population i Chromosome oraz funkcji set_const z odpowiednich modułów
from population import Population
from chromosom import Chromosome
from chromosom import set_const

# Ustawienie stałych używanych przez algorytm genetyczny
set_const(-10, 10, 25, 100, 1)

# Inicjalizacja obiektu Chromosome, który będzie reprezentował osobniki w populacji
chromosome = Chromosome(1)

# Inicjalizacja listy przechowującej najlepsze znalezione rozwiązania
best_solutions = []

# Utworzenie obiektu Population, który reprezentuje populację osobników
population = Population(chromosome)

# Pętla ewolucji populacji przez 1000 generacji
for i in range(1000):
    # Znalezienie najlepszego rozwiązania w aktualnej populacji i dodanie go do listy best_solutions
    best_solutions = population.best_solution(i, best_solutions)

    # Ewolucja populacji - krzyżowanie i mutacja
    population.evolve()

# Wyświetlenie najlepszego znalezionego rozwiązania po zakończeniu ewolucji
population.print_best(best_solutions)