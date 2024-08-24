import sys
class Population:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.population = self.makePopulation()

    def fitness(self, params: list) -> float:
        """Oblicza wartość funkcji przystosowania dla zestawu parametrów."""
        x = params[0]
        foo_value = x**2 + 5
        return 1 / (foo_value)  if foo_value != 0 else 999999 # Odwrócenie wartości, aby zminimalizować funkcję

    def makePopulation(self) -> list:
        population = []
        for params in self.chromosome.chromosome:
            fitness_value = self.fitness(params)
            population.append((params, fitness_value))
        return population

    def evolve(self) -> None:
        parents = [ind[0] for ind in sorted(self.population, key=lambda x: x[1], reverse=True)[:10]]
        new_generation = self.chromosome.multiplication(parents)
        self.population = [(x, self.fitness(x)) for x in new_generation]

    def best_solution(self, i: int, best_solutions: list) -> list:
        best_solution = max(self.population, key=lambda x: x[1])
        best_solutions.append(best_solution)
        print(f"Gen {i} best solution")
        print(best_solution)
        if best_solution[1] < 1e-6:
            self.print_best(best_solutions)
            sys.exit()
        return best_solutions

    def print_best(self, best_solutions: list) -> None:
        smallest_solution = max(best_solutions, key=lambda x: x[1])
        print("Smallest best solution found:")
        print(f"{smallest_solution[0]}, {1 / smallest_solution[1]}")
