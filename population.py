import sys


class Population:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.population = self.makePopulation()

    def fitness(self, x:float):
        y = 2 * x ** 2 + 5
        if y == 0:
            return 99999
        else:
            return 1 / y

    def makePopulation(self):
        population = []
        for x in self.chromosome.chromosome:
            y = self.fitness(x)
            population.append((x, y))
        return population

    def evolve(self):
        parents = [ind[0] for ind in sorted(self.population, key=lambda x: x[1], reverse=True)[:10]]
        new_generation = self.chromosome.multiplication(parents, "uniform", "two_point", 0.2) #metoda krzyzowan i mutacji, prawdop mutacji
        self.population = [(x, self.fitness(x)) for x in new_generation]

    def best_solution(self, i, best_solutions):
        best_solution = max(self.population, key=lambda x: x[1])
        best_solutions.append(best_solution)
        print(f"Gen {i} best solution")
        print(best_solution)
        if best_solution[1] < 1e-6:
            self.print_best(best_solutions)
            sys.exit()
        return best_solutions

    def print_best(self, best_solutions):
        smallest_solution = max(best_solutions, key=lambda x: x[1])
        print("Smallest best solution found:")
        print(f"{smallest_solution[0]:.8f}, {1 / smallest_solution[1]}")