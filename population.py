import sys
import random
import sympy as sp


class Population:
    def __init__(self, chromosome : list , equation : sp.Expr):
        self.chromosome = chromosome
        self.y_Equation = equation
        self.population = self.make_Population()
 


    def make_Population(self) -> list:
        population = []
        for x_Value in self.chromosome.chromosome:
            y_Var = self.fitness(x_Value)
            population.append((x_Value, y_Var))
        return population


    def fitness(self , x_Value : float) -> float:

        if self.y_Equation.subs( "x" , x_Value) == 0:
            return 99999
        else:
            return 1 / self.y_Equation.subs("x" ,x_Value)

    
    def best_Selection(self) -> list:
        parents = [ind[0] for ind in sorted(self.population, key=lambda x: x[1], reverse=True)[:10]]
        return parents
    

    def how_Many_Groups(self) -> int:
        groups = int(input("How many groups in the tournament? "))
        # check
        if len(self.population) % groups != 0:
            raise ValueError("Population size must be divisible by the number of groups")
        return groups
    

    def tournament(self, groups : int) -> list:
        size_Groups = len(self.population) // groups
        random.shuffle(self.population) 
        parents = []
   
        for i in range(groups):
            group_Start = i * size_Groups
            group_End = group_Start + size_Groups
            group_Participants = self.population[group_Start : group_End]
            
            winner = max(group_Participants, key=lambda x: x[1])
            parents.append(winner[0])
        
        return parents


    def roulette(self) -> list:
        suma = sum(value[1] for value in self.population)
        pp = 0
        distributor = []
        parents = []
        for x in self.population:          
            pp += x[1]/suma
            distributor.append((x[0], pp))
        
        for _ in range(10):
            spin = random.uniform(0,1)
            for d in distributor:
                if (d[1] >= spin):
                    parents.append(d[0])
                    break
        return parents


    def evolve(self, groups_Amount : int , selection_Method : str , crossOver_Method : str , mutation_Method : str , mutation_Probability : float) -> None:

        if (selection_Method == 'Best Selection'):
            parents = self.best_Selection() 

        elif (selection_Method == 'Tournament Selection'):
            parents = self.tournament(groups_Amount)

        elif (selection_Method == 'Roulette Selection'):
            parents = self.roulette()

        else:
            print("Wrong selection")
            exit(0)

        new_Generation = self.chromosome.multiplication(parents, crossOver_Method, mutation_Method, mutation_Probability) 
        self.population = [(x, self.fitness(x)) for x in new_Generation]


    def best_Solution(self, curr_Generation_Number : int, best_Solutions : list) -> list:
        best_Solution = max(self.population, key=lambda x: x[1])
        best_Solutions.append(best_Solution)
        print(f"Gen {curr_Generation_Number} best solution")
        print(best_Solution)

        if best_Solution[1] < 1e-6:
            self.print_Best(best_Solutions)
            sys.exit()

        return best_Solutions


    def print_Best(self, best_Solutions : list) -> None:
        smallest_Solution = max(best_Solutions, key=lambda x: x[1])
        print("Smallest best solution found:")
        print(f"{smallest_Solution[0]:.8f}, {1 / smallest_Solution[1]}")
        return smallest_Solution[0] , smallest_Solution[1]
