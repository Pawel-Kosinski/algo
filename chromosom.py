import random

class Chromosome:
    def __init__(self):
        self.chromosome = []
        while len(self.chromosome) < 100:
            self.chromosome.append(random.uniform(-10, 10))
    
    def multiplication(self, parents):
        newChrom = []
        for _ in range(100):
            parent1, parent2 = random.sample(parents, 2)
            offspring = (parent1 + parent2) / 2

            # Mutation: Perturb the offspring slightly
            offspring += random.uniform(-0.1, 0.1)
            newChrom.append(offspring)
            
        return newChrom