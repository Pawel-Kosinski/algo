from population import Population
from chromosom import Chromosome
from chromosom import set_const

set_const(-10,10,25,100)

chromosome = Chromosome()
best_solutions = []
population = Population(chromosome)
for i in range(1000):
    best_solutions = population.best_solution(i, best_solutions)
    population.evolve()

population.print_best(best_solutions)