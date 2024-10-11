# Importowanie klas Population i Chromosome oraz funkcji set_const z odpowiednich modułów
from population import Population
from chromosom import Chromosome
from chromosom import set_const
from GUI import GUI


class GeneticAlgorithm:
    def __init__(self):
        self.app = GUI()
        self.chromosome = None
        self.best_solutions = []
        self.population = None
        self.groups = None

        self.equation_vars = None
        self.equation = None
        self.interval_start = None
        self.interval_end = None
        self.approximation_bits = None
        self.child_count = None
        self.num_params = None
        self.groups_amount = None
        self.mutation_probability = None
        self.crossover_method = None
        self.mutation_method = None
        self.selection_method = None

        self.app.algorithm_activation_button.configure(command=self.start_algorithm)

    def update_records(self):
        self.equation_vars = self.app.equation_frame.get_entry_content()[0]
        self.equation = self.app.equation_frame.get_entry_content()[1]
        self.interval_start = self.app.interval_start_frame.get_entry_content()
        self.interval_end = self.app.interval_end_frame.get_entry_content()
        self.approximation_bits = self.app.interval_start_frame.get_entry_content()
        self.child_count = self.app.number_of_child_per_population_frame.get_entry_content()
        self.groups_amount = self.app.number_of_groups_frame.get_entry_content()
        self.mutation_probability = self.app.mutation_probability_frame.get_entry_content()
        self.crossover_method = self.app.crossover_methods_frame.combo_box.get()
        self.mutation_method = self.app.mutation_methods_frame.combo_box.get()
        self.selection_method = self.app.selection_methods_frame.combo_box.get()

    def is_invalid(self, validation_label):
        text = validation_label.cget("text")
        return text == "✘" or text == " "

    def start_algorithm(self):
        if any(self.is_invalid(frame.validation_label) for frame in [
            self.app.equation_frame,
            self.app.interval_start_frame,
            self.app.interval_end_frame,
            self.app.number_of_approximation_bits_frame,
            self.app.number_of_groups_frame,
            self.app.mutation_probability_frame
        ]):
            return

        self.update_records()
        set_const(self.interval_start, self.interval_end, self.approximation_bits, self.child_count, len(self.equation_vars))
        self.chromosome = Chromosome(len(self.equation_vars), self.equation_vars, self.equation)
        self.population = Population(self.chromosome)
        self.groups = self.population.how_Many_Groups(self.groups_amount)

        for i in range(1000):
            self.best_solutions = self.population.best_solution(i, self.best_solutions)
            (self.population.evolve
                (
                    groups_Amount=self.groups,
                    selection_Method=self.selection_method,
                    crossOver_Method=self.crossover_method,
                    mutation_Method=self.mutation_method,
                    mutation_Probability=self.mutation_probability
                ))
        self.population.print_best(self.best_solutions)


program = GeneticAlgorithm()
program.app.run_gui()

"""
set_const(-20, 20, 25, 1000, 5)

# Inicjalizacja obiektu Chromosome, który będzie reprezentował osobniki w populacji10
chromosome = Chromosome(5)

# Inicjalizacja listy przechowującej najlepsze znalezione rozwiązania
best_solutions = []

# Utworzenie obiektu Population, który reprezentuje populację osobników
population = Population(chromosome)

groups = population.how_Many_Groups(10)

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
population.print_best(best_solutions)"""
