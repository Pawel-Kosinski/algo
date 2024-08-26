import random
import math

def set_const(valueA: float, valueB: float, approxValue: int, childCount: int, num_params: int):
    '''Funkcja zmieniająca stałe używane w chromosomie i aktualizująca bin_len.'''
    global rangeA, rangeB, decimalApprox, bin_len, childPerGen
    rangeA = valueA
    rangeB = valueB
    decimalApprox = approxValue
    bin_len = math.ceil(math.log2((rangeB - rangeA) * (10 ** decimalApprox))) * num_params
    childPerGen = childCount

def dec_to_bin(dec: list) -> str:
    """Zamiana listy liczb dziesiętnych na jeden ciąg binarny."""
    binary_string = ""
    param_bin_len = bin_len // len(dec)
    for val in dec:
        if not rangeA <= val <= rangeB:
            raise ValueError(f"Input should be within the interval [{rangeA}, {rangeB}]")
        scaled_value = int((val - rangeA) / (rangeB - rangeA) * (2 ** param_bin_len - 1))
        binary_string += format(scaled_value, f'0{param_bin_len}b')
    return binary_string

def bin_to_dec(bin_str: str, num_params: int) -> list:
    """Zamiana ciągu binarnego na listę liczb dziesiętnych."""
    param_len = len(bin_str) // num_params
    dec_values = []
    for i in range(num_params):
        bin_part = bin_str[i * param_len:(i + 1) * param_len]
        integer = int(bin_part, 2)
        dec_values.append(rangeA + integer * (rangeB - rangeA) / (2 ** param_len - 1))
    return dec_values

class Chromosome:
    def __init__(self, num_params: int):
        '''Tworzy tablicę losowych wartości dla każdego z parametrów od rangeA do rangeB.'''
        self.num_params = num_params
        self.chromosome = [[random.uniform(rangeA, rangeB) for _ in range(num_params)] for _ in range(100)]

    def one_point_crossover(self, parent1, parent2):
        """Przeprowadza krzyżowanie jednopunktowe między dwoma rodzicami."""
        crossover_point = random.randint(1, len(parent1) - 1)
        child = parent1[:crossover_point] + parent2[crossover_point:]
        return child

    def two_point_crossover(self, parent1, parent2):
        """Przeprowadza krzyżowanie dwupunktowe między dwoma rodzicami."""
        cp1, cp2 = sorted(random.sample(range(1, len(parent1) - 1), 2))
        child = parent1[:cp1] + parent2[cp1:cp2] + parent1[cp2:]
        return child

    def three_point_crossover(self, parent1, parent2):
        """Przeprowadza krzyżowanie trzypunktowe między dwoma rodzicami."""
        cp1, cp2, cp3 = sorted(random.sample(range(1, len(parent1) - 1), 3))
        child = parent1[:cp1] + parent2[cp1:cp2] + parent1[cp2:cp3] + parent2[cp3:]
        return child

    def uniform_crossover(self, parent1, parent2):
        """Przeprowadza krzyżowanie jednorodne między dwoma rodzicami."""
        child_bits = [parent1[i] if random.random() < 0.5 else parent2[i] for i in range(len(parent1))]
        child = ''.join(child_bits)
        return child

    def grainy_crossover(self, parent1, parent2):
        """Przeprowadza krzyżowanie ziarniste między dwoma rodzicami."""
        grain_size = random.randint(1, 5)
        child_bits = []
        use_parent1 = True
        i = 0
        while i < len(parent1):
            end = min(i + grain_size, len(parent1))
            child_bits.append(parent1[i:end] if use_parent1 else parent2[i:end])
            use_parent1 = not use_parent1
            i = end
        child = ''.join(child_bits)
        return child

    def edge_mutation(self, child: str, mutation_prob: float) -> str:
        """Przeprowadza mutację krawędziową na potomku."""
        if random.random() < mutation_prob:
            child = ('1' if child[0] == '0' else '0') + child[1:-1] + ('1' if child[-1] == '0' else '0')
        return child

    def one_point_mutation(self, child: str, mutation_prob: float) -> str:
        """Przeprowadza mutację jednopunktową na potomku."""
        if random.random() < mutation_prob:
            mutation_point = random.randint(0, len(child) - 1)
            child = child[:mutation_point] + ('1' if child[mutation_point] == '0' else '0') + child[mutation_point + 1:]
        return child

    def two_point_mutation(self, child: str, mutation_prob: float) -> str:
        """Przeprowadza mutację dwupunktową na potomku."""
        if random.random() < mutation_prob:
            mp1, mp2 = sorted(random.sample(range(len(child)), 2))
            child = (child[:mp1] + ('1' if child[mp1] == '0' else '0') +
                     child[mp1 + 1:mp2] + ('1' if child[mp2] == '0' else '0') +
                     child[mp2 + 1:])
        return child

    def mutation(self, child: str, mutation_method: str, mutation_prob: float) -> str:
        """Wybiera i przeprowadza odpowiednią metodę mutacji na potomku."""
        if mutation_method == "Edge Mutation":
            child = self.edge_mutation(child, mutation_prob)
        elif mutation_method == "One Point Mutation":
            child = self.one_point_mutation(child, mutation_prob)
        elif mutation_method == "Two Point Mutation":
            child = self.two_point_mutation(child, mutation_prob)
        return child

    def multiplication(self, parents, crossover_type="three_point", mutation_method="Two Point Mutation", mutation_prob=0.2) -> list:
        """Przeprowadza krzyżowanie i mutację na podanej populacji."""
        new_generation = []

        for _ in range(childPerGen):
            parent1, parent2 = random.sample(parents, 2)
            parent1_bin, parent2_bin = dec_to_bin(parent1), dec_to_bin(parent2)

            # Wybór rodzaju krzyżowania
            if crossover_type == "one_point":
                child_bin = self.one_point_crossover(parent1_bin, parent2_bin)
            elif crossover_type == "two_point":
                child_bin = self.two_point_crossover(parent1_bin, parent2_bin)
            elif crossover_type == "three_point":
                child_bin = self.three_point_crossover(parent1_bin, parent2_bin)
            elif crossover_type == "uniform":
                child_bin = self.uniform_crossover(parent1_bin, parent2_bin)
            elif crossover_type == "grainy":
                child_bin = self.grainy_crossover(parent1_bin, parent2_bin)
            else:
                # Domyślne krzyżowanie w przypadku nieznanego typu
                child_bin = self.two_point_crossover(parent1_bin, parent2_bin)

            # Mutacja na nowo utworzonym chromosomie
            child_bin = self.mutation(child_bin, mutation_method, mutation_prob)
            new_generation.append(bin_to_dec(child_bin, self.num_params))

        return new_generation
