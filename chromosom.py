import random
import math


rangeStart = -10
rangeEnd = 10
decimalApproximation = 6                                                                
bin_len = math.ceil(math.log2((rangeEnd-rangeStart) * (10 ** decimalApproximation)))       
childPerGen = 100                                                                          


def set_Global_Values(start_Value : float, end_Value : float, number_Of_Approx_Bits : int, population_Amount : int) -> None:
    "Funkcja ustawia zmienne Globalne" 
    global rangeStart, rangeEnd, decimalApproximation, bin_len, childPerGen

    rangeStart = start_Value
    rangeEnd = end_Value
    decimalApproximation = number_Of_Approx_Bits
    bin_len = math.ceil(math.log2((rangeEnd - rangeStart) * (10 ** decimalApproximation)))
    childPerGen = population_Amount


def convert_Dec_to_Bin(dec : float) -> str:
    "Zamiana liczby decymalnej na binarna"
    if not rangeStart <= dec <= rangeEnd:
        raise ValueError(f"Input should be within the interval [{rangeStart}, {rangeEnd}]")
    
    scaled_value = int((dec - rangeStart) / (rangeEnd - rangeStart) * (2 ** bin_len - 1))
    return format(scaled_value, f'0{bin_len}b')


def convert_Bin_to_Dec(bin : str) -> float:
    "Zamienia liczbe binarną na decymalna"
    integer = int(bin, 2)  
    return rangeStart + integer * (rangeEnd - rangeStart) / (2 ** bin_len - 1)



class Chromosome:
    """Klasa Chromosome zawiera metody do przeprowadzania krzyżowania i mutacji na chromosomach oraz funkcję multiplication,
        która wykonuje zadane krzyżowanie i mutację na podanej populacji osobników."""

    def __init__(self):
        "Tworzy tablicę losowych wartości od rangeStart do rangeEnd."
        self.chromosome = [random.uniform(rangeStart, rangeEnd) for _ in range(100)] 


    def one_Point_Crossover(self, parent1 : str, parent2 : str) -> str:
        "Przeprowadza krzyżowanie jednopunktowe między dwoma rodzicami."
        crossover_Point = random.randint(1, len(parent1) - 1)
        child = parent1[:crossover_Point] + parent2[crossover_Point:]
        return child


    def two_Point_Crossover(self, parent1 : str, parent2 : str) -> str:
        "Przeprowadza krzyżowanie dwupunktowe między dwoma rodzicami."
        cross_Point_One, cross_Point_Two = sorted(random.sample(range(1, len(parent1) - 1), 2)) 
        child = parent1[:cross_Point_One] + parent2[cross_Point_One : cross_Point_Two] + parent1[cross_Point_Two:]
        return child


    def three_Point_Crossover(self, parent1 : str, parent2 : str) -> str:
        "Przeprowadza krzyżowanie trzypunktowe między dwoma rodzicami."
        cross_Point_One, cross_Point_Two, cross_Point_Three = sorted(random.sample(range(1, len(parent1) - 1), 3))
        child = parent1[:cross_Point_One] + parent2[cross_Point_One : cross_Point_Two] + parent1[cross_Point_Two : cross_Point_Three] + parent2[cross_Point_Three:]
        return child


    def uniform_Crossover(self, parent1 : str, parent2 : str) -> str:
        "Przeprowadza krzyżowanie jednorodne między dwoma rodzicami."
        child_Bits = [parent1[i] if random.random() < 0.5 else parent2[i] for i in range(len(parent1))]
        child = ''.join(child_Bits)
        return child


    def grainy_Crossover(self, parent1 : str, parent2 : str) -> str:
        "Przeprowadza krzyżowanie ziarniste między dwoma rodzicami."
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


    def edge_Mutation(self, child : str, mutation_prob : float) -> str:
        "Przeprowadza mutację krawędziową na potomku."
        if random.random() < mutation_prob:
            child = ('1' if child[0] == '0' else '0') + child[1:-1] + ('1' if child[-1] == '0' else '0')
        return child


    def one_Point_Mutation(self, child : str, mutation_prob : float) -> str:
        "Przeprowadza mutację jednopunktową na potomku."
        if random.random() < mutation_prob:
            mutation_point = random.randint(0, len(child) - 1)
            child = child[:mutation_point] + ('1' if child[mutation_point] == '0' else '0') + child[mutation_point + 1:]
        return child


    def two_Point_Mutation(self, child : str, mutation_prob : float) -> str:
        "Przeprowadza mutację dwupunktową na potomku."
        if random.random() < mutation_prob:
            mp1, mp2 = sorted(random.sample(range(len(child)), 2))
            child = (child[:mp1] + ('1' if child[mp1] == '0' else '0') +
                     child[mp1 + 1:mp2] + ('1' if child[mp2] == '0' else '0') +
                     child[mp2 + 1:])
        return child


    def mutation(self, child : str, mutation_Method : str, mutation_Probability : float) -> str:
        "Wybiera i przeprowadza odpowiednią metodę mutacji na potomku."
        
        if mutation_Method == "Edge Mutation":
            child = self.edge_Mutation(child, mutation_Probability)

        elif mutation_Method == "One Point Mutation":
            child = self.one_Point_Mutation(child, mutation_Probability)

        elif mutation_Method == "Two Point Mutation":
            child = self.two_Point_Mutation(child, mutation_Probability)
            
        return child


    def multiplication(self, parents : list, crossover_Method="two_point", mutation_Method="edge", mutation_Probability=0.2) -> list:
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
            parent1, parent2 = convert_Dec_to_Bin(parent1), convert_Dec_to_Bin(parent2)

            if crossover_Method == "One Point CrossOver":
                child = self.one_Point_Crossover(parent1, parent2)

            elif crossover_Method == "Two Point CrossOver":
                child = self.two_Point_Crossover(parent1, parent2)

            elif crossover_Method == "Three Point CrossOver":
                child = self.three_Point_Crossover(parent1, parent2)

            elif crossover_Method == "Uniform CrossOver":
                child = self.uniform_Crossover(parent1, parent2)

            elif crossover_Method == "Grainy CrossOver":
                child = self.grainy_Crossover(parent1, parent2)

            child = self.mutation(child, mutation_Method, mutation_Probability)

            new_generation.append(convert_Bin_to_Dec(child))

        return new_generation