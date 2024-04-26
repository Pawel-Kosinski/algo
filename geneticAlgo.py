from population import Population
from chromosom import Chromosome


chromosome = Chromosome(-10,10) #tutaj wprowadzamy teraz przedział od [-10,10]
best_solutions = []
population = Population(chromosome)
for i in range(10):
    best_solutions = population.best_solution(i, best_solutions)
    population.evolve()

population.print_best(best_solutions)

