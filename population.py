class Population:
    """
    Klasa reprezentująca populację w algorytmie genetycznym.

    Atrybuty:
        chromosome (object): Obiekt chromosomu reprezentujący osobniki w populacji.
        population (list): Lista zawierająca osobniki w populacji, wraz z ich wartościami przystosowania.
    """

    def __init__(self, chromosome):
        """
        Konstruktor klasy Population.

        Args:
            chromosome (object): Obiekt chromosomu reprezentujący osobniki w populacji.

        Returns:
            None
        """
        self.chromosome = chromosome
        self.population = self.makePopulation()

    def fitness(self, x: float) -> float:
        """
        Oblicza wartość funkcji przystosowania dla określonej wartości x.

        Args:
            x (float): Wartość x dla której obliczana jest wartość funkcji przystosowania.

        Returns:
            float: Wartość funkcji przystosowania dla danego x.
        """
        y = 2 * x ** 2 + 5
        if y == 0:
            return 99999
        else:
            return 1 / y

    def makePopulation(self) -> list:
        """
        Tworzy początkową populację na podstawie chromosomu (patrz plik chromosom, def __init__).

        Returns:
            list: Lista zawierająca osobniki w populacji wraz z ich wartościami przystosowania.
        """
        population = []
        for x in self.chromosome.chromosome:
            y = self.fitness(x)
            population.append((x, y))
        return population

    def evolve(self) -> None:
        """
        Ewoluuje populację, wybierając najlepszych rodziców i tworząc nowe pokolenie.

        Returns:
            None
        """
        #wybiera 10 najlepszych osobników (rodziców) z populacji na podstawie ich wartości przystosowania
        parents = [ind[0] for ind in sorted(self.population, key=lambda x: x[1], reverse=True)[:10]]
        new_generation = self.chromosome.multiplication(parents, "uniform", "two_point", 0.2) # metoda krzyżowania i mutacji, prawdopodobieństwo mutacji
        self.population = [(x, self.fitness(x)) for x in new_generation]

    def best_solution(self, i: int, best_solutions: list) -> list:
        """
        Znajduje najlepsze rozwiązanie w populacji.

        Args:
            i (int): Numer aktualnej generacji.
            best_solutions (list): Lista zawierająca najlepsze rozwiązania znalezione do tej pory.

        Returns:
            list: Lista zawierająca najlepsze rozwiązania.
        """
        best_solution = max(self.population, key=lambda x: x[1])
        best_solutions.append(best_solution)
        print(f"Gen {i} best solution")
        print(best_solution)
        if best_solution[1] < 1e-6:
            self.print_best(best_solutions)
            sys.exit()
        return best_solutions

    def print_best(self, best_solutions: list) -> None:
        """
        Drukuje najmniejsze najlepsze rozwiązanie znalezione w populacji.

        Args:
            best_solutions (list): Lista zawierająca najlepsze rozwiązania znalezione do tej pory.

        Returns:
            None
        """
        smallest_solution = max(best_solutions, key=lambda x: x[1])
        print("Smallest best solution found:")
        print(f"{smallest_solution[0]:.8f}, {1 / smallest_solution[1]}")
