from population import Population
from chromosom import Chromosome

chromosome = Chromosome()
best_solutions = []
population = Population(chromosome)
for i in range(1000):

    best_solutions = population.best_solution(i, best_solutions)

    population.evolve()
    
population.print_best(best_solutions)