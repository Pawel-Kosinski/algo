import random

#cały chromosom działa na zadanym przedziale (bez obliczania jeszcze odpowiedniego ciągu znaków od książka)
#chromosom przyjmuje póki co tylko x
#poniżej zawarte są funkcje dec_to_bin, bin_to_dec - ich nie trzeba tłumaczyć chyba
#w klasie chromosom inicjalizacja tablicy (liczby sys dziesiętny)
#następnie są funkcje obsługujące różne rodzaje mutacji
#funkcja multuplication która obsługuje różne rodzaje krzyżowań, mutacji (wybór przez string) z zadanym prawdopodobieństwem - na binarnych
#multiplication zwraca listę skrzyżowanych, zmutowanych, dziesiętnych liczb

#funckja dec to bin jest do dostosowania - zgodnie ze wzorem książka + konfiguracja dokładności
def dec_to_bin(dec:float , a : float, b: float) -> str:
    """zamiana chromosomu na binarny
        n : podawana wartosc z przedzialu
        a : poczatek przedzialu
        b : koniec przedzialu """
    dec = round(dec)
    if not a <= dec <= b:
        raise ValueError(f"Input should be within the interval [{a}, {b}]")
    return format(dec & 0b1111111111111111111111111, '025b')

def bin_to_dec(bin:str, a : float, b: float):
    """zamiana chromosomu na int
        n : podawana wartosc z przedzialu
        a : poczatek przedzialu
        b : koniec przedzialu """
    return int(bin, 2)

class Chromosome:
    def __init__(self, a: float, b: float):
        """przedzial od a do b"""
        self.a = a
        self.b = b
        self.chromosome = [random.uniform(self.a, self.b) for _ in range(100)] #przedział [a,b]

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
            parent1, parent2 = dec_to_bin(parent1,self.a,self.b), dec_to_bin(parent2,self.a,self.b)

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

            new_generation.append(bin_to_dec(child,self.a,self.b))
        return new_generation
