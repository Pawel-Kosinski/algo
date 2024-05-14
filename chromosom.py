import random
import math

# Aktualnie chromosom przyjmuje tylko x -> trzeba zmienic na obsługę wielu zmiennych

# Zmienne określające zakres działań, zmienialne są w mainie; default [-10,10]
rangeA = -10
rangeB = 10

# Określa dokładność binarnej reprezentacji chromosomu np. do 6 cyfr znaczących.
decimalApprox = 6

# Długość łańcucha binarnego chromosomu.
bin_len = math.ceil(math.log2((rangeB - rangeA) * (10 ** decimalApprox)))

# Liczba potomków generowanych w każdej nowej generacji.
childPerGen = 100

# Powyższe zmienne są ustawione DEFAULTOWO, można je zmieniać w mainie za pomocą poniższej funkcji:

def set_const (valueA:float,valueB:float,approxValue:int,childCount:int):
    '''Funkcja zmieniająca stałe używane w chromosomie i aktualizująca bin_len.

    Args:
        valueA (float): Zakres działań od.
        valueB (float): Zakres działań do.
        approxValue (int): Dokładność binarnej reprezentacji chromosomu, liczba cyfr znaczących.
        childCount (int): Liczba potomków w generacji.
    '''
    global rangeA, rangeB, decimalApprox, bin_len, childPerGen
    rangeA = valueA
    rangeB = valueB
    decimalApprox = approxValue
    bin_len = math.ceil(math.log2((rangeB-rangeA)*(10**decimalApprox)))
    childPerGen = childCount



def dec_to_bin(dec: float) -> str:
    """Zamiana liczby dziesiętnej na binarną zgodnie ze wzorem Książka.

    Args:
        dec (float): Wartość dziesiętna do przekonwertowania.

    Returns:
        str: Binarna reprezentacja wartości dziesiętnej.
    """
    if not rangeA <= dec <= rangeB:
        raise ValueError(f"Input should be within the interval [{rangeA}, {rangeB}]")

    scaled_value = int((dec - rangeA) / (rangeB - rangeA) * (2 ** bin_len - 1))
    return format(scaled_value, f'0{bin_len}b')



def bin_to_dec(bin: str):
    """Zamiana liczby binarnej na dziesiętną zgodnie ze wzorem Książka.

    Args:
        bin (str): Wartość binarna do przekonwertowania.

    Returns:
        float: Dziesiętna reprezentacja wartości binarnej.
    """
    integer = int(bin, 2)  # Zamiana binarnej na integer
    return rangeA + integer * (rangeB - rangeA) / (2 ** bin_len - 1)



class Chromosome:
    """Klasa Chromosome zawiera metody do przeprowadzania krzyżowania i mutacji na chromosomach oraz funkcję multiplication,
        która wykonuje zadane krzyżowanie i mutację na podanej populacji osobników."""

    def __init__(self):
        '''Tworzy tablicę losowych wartości od rangeA do rangeB.'''
        self.chromosome = [random.uniform(rangeA, rangeB) for _ in range(100)] # Przedział [a,b]

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

    def edge_mutation(self, child, mutation_prob):
        """Przeprowadza mutację krawędziową na potomku."""
        if random.random() < mutation_prob:
            child = ('1' if child[0] == '0' else '0') + child[1:-1] + ('1' if child[-1] == '0' else '0')
        return child

    def one_point_mutation(self, child, mutation_prob):
        """Przeprowadza mutację jednopunktową na potomku."""
        if random.random() < mutation_prob:
            mutation_point = random.randint(0, len(child) - 1)
            child = child[:mutation_point] + ('1' if child[mutation_point] == '0' else '0') + child[mutation_point + 1:]
        return child

    def two_point_mutation(self, child, mutation_prob):
        """Przeprowadza mutację dwupunktową na potomku."""
        if random.random() < mutation_prob:
            mp1, mp2 = sorted(random.sample(range(len(child)), 2))
            child = (child[:mp1] + ('1' if child[mp1] == '0' else '0') +
                     child[mp1 + 1:mp2] + ('1' if child[mp2] == '0' else '0') +
                     child[mp2 + 1:])
        return child

    def mutation(self, child, mutation_type, mutation_prob):
        """Wybiera i przeprowadza odpowiednią metodę mutacji na potomku."""
        if mutation_type == "edge":
            child = self.edge_mutation(child, mutation_prob)
        elif mutation_type == "one_point":
            child = self.one_point_mutation(child, mutation_prob)
        elif mutation_type == "two_point":
            child = self.two_point_mutation(child, mutation_prob)
        return child

    def multiplication(self, parents, crossover_type="two_point", mutation_type="edge", mutation_prob=0.2) -> list:
        '''Funkcja przeprowadzająca krzyżowanie i mutację na podanej populacji.

        Args:
            parents (list): Populacja osobników do przekształcenia.
            crossover_type (str): Typ krzyżowania. Domyślnie "two_point".
            mutation_type (str): Typ mutacji. Domyślnie "edge".
            mutation_prob (float): Prawdopodobieństwo mutacji. Domyślnie 0.2.

        Returns:
            list: Nowa populacja po przeprowadzeniu krzyżowania i mutacji.
        '''
        new_generation = []

        for _ in range(childPerGen):
            parent1, parent2 = random.sample(parents, 2)
            parent1, parent2 = dec_to_bin(parent1), dec_to_bin(parent2)

            if crossover_type == "one_point":
                child = self.one_point_crossover(parent1, parent2)
            elif crossover_type == "two_point":
                child = self.two_point_crossover(parent1, parent2)
            elif crossover_type == "three_point":
                child = self.three_point_crossover(parent1, parent2)
            elif crossover_type == "uniform":
                child = self.uniform_crossover(parent1, parent2)
            elif crossover_type == "grainy":
                child = self.grainy_crossover(parent1, parent2)

            child = self.mutation(child, mutation_type, mutation_prob)

            new_generation.append(bin_to_dec(child))

        return new_generation

