import random
import math

#cały chromosom działa na zadanym przedziale (bez obliczania jeszcze odpowiedniego ciągu znaków od książka)
#chromosom przyjmuje póki co tylko x
#poniżej zawarte są funkcje dec_to_bin, bin_to_dec - ich nie trzeba tłumaczyć chyba
#w klasie chromosom inicjalizacja tablicy (liczby sys dziesiętny)
#następnie są funkcje obsługujące różne rodzaje mutacji
#funkcja multuplication która obsługuje różne rodzaje krzyżowań, mutacji (wybór przez string) z zadanym prawdopodobieństwem - na binarnych
#multiplication zwraca listę skrzyżowanych, zmutowanych, dziesiętnych liczb

#Zmienne określające zakres działań, zmienialne są w mainie; default [-10,10]
rangeA = -10
rangeB = 10
#Określa dokładność binarnej reprezentacji chromosomu np. do 6 cyfr znaczących
decimalApprox = 6
#Długość łańcucha binarnego chromosomu
bin_len = math.ceil(math.log2((rangeB-rangeA)*(10**decimalApprox)))
#Powyższe zmienne są ustawione DEFAULTOWO, można je zmieniać w mainie za pomocą poniższej funkcji:
def set_const (valueA:float,valueB:float,approxValue:int):
    '''Funkcja zmieniajace stale uzywane w chromosom i aktualizujaca bin_len\n
        valueA - ustawia zakres działań od\n
        valueB - ustawia zakres działań do\n
        approxValue - ustawia dokładność bin reprezentacji chromosomu, liczba cyfr znaczacych'''
    global rangeA, rangeB, decimalApprox, bin_len
    rangeA = valueA
    rangeB = valueB
    decimalApprox = approxValue
    bin_len = math.ceil(math.log2((rangeB-rangeA)*(10**decimalApprox)))

#funckja dec to bin jest do dostosowania - zgodnie ze wzorem książka + konfiguracja dokładności
def dec_to_bin(dec:float) -> str:
    """zamiana chromosomu na binarny\n
        dec : podawana wartosc dziesietna"""
    if not rangeA <= dec <= rangeB:
        raise ValueError(f"Input should be within the interval [{rangeA}, {rangeB}]")
    scaled_value = int((dec - rangeA) / (rangeB - rangeA) * (2**bin_len - 1))
    return format(scaled_value, f'0{bin_len}b')

def bin_to_dec(bin:str):
    """zamiana chromosomu na int\n
        bin : podawana wartosc binarna"""
    integer = int(bin, 2)  # bin to integer
    return rangeA + integer * (rangeB - rangeA) / (2**bin_len - 1)

class Chromosome:
    def __init__(self):
        self.chromosome = [random.uniform(rangeA, rangeB) for _ in range(100)] #przedział [a,b]

    def edge_mutation(self, child, mutation_prob):
        if random.random() < mutation_prob:
            child = ('1' if child[0] == '0' else '0') + child[1:-1] + ('1' if child[-1] == '0' else '0')
        return child

    def one_point_mutation(self, child, mutation_prob):
        if random.random() < mutation_prob:
            mutation_point = random.randint(0, len(child) - 1)
            child = child[:mutation_point] + ('1' if child[mutation_point] == '0' else '0') + child[mutation_point + 1:]
        return child

    def two_point_mutation(self, child, mutation_prob):
        if random.random() < mutation_prob:
            mp1, mp2 = sorted(random.sample(range(len(child)), 2))
            child = (child[:mp1] + ('1' if child[mp1] == '0' else '0') +
                     child[mp1 + 1:mp2] + ('1' if child[mp2] == '0' else '0') +
                     child[mp2 + 1:])
        return child

    def multiplication(self, parents, crossover_type="two_point", mutation_type="edge", mutation_prob=0.2):
        new_generation = []
        for _ in range(100):
            parent1, parent2 = random.sample(parents, 2)
            parent1, parent2 = dec_to_bin(parent1), dec_to_bin(parent2)

            if crossover_type == "one_point":
                crossover_point = random.randint(1, len(parent1) - 1)
                child = parent1[:crossover_point] + parent2[crossover_point:]
            elif crossover_type == "two_point":
                cp1, cp2 = sorted(random.sample(range(1, len(parent1) - 1), 2))
                child = parent1[:cp1] + parent2[cp1:cp2] + parent1[cp2:]
            elif crossover_type == "three_point":
                cp1, cp2, cp3 = sorted(random.sample(range(1, len(parent1) - 1), 3))
                child = parent1[:cp1] + parent2[cp1:cp2] + parent1[cp2:cp3] + parent2[cp3:]
            elif crossover_type == "uniform":
                child_bits = [parent1[i] if random.random() < 0.5 else parent2[i] for i in range(len(parent1))]
                child = ''.join(child_bits)
            elif crossover_type == "grainy":
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

            # Apply mutation
            if mutation_type == "edge":
                child = self.edge_mutation(child, mutation_prob)
            elif mutation_type == "one_point":
                child = self.one_point_mutation(child, mutation_prob)
            elif mutation_type == "two_point":
                child = self.two_point_mutation(child, mutation_prob)

            new_generation.append(bin_to_dec(child))
        return new_generation
