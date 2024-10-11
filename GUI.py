import customtkinter as ctk
from GUI_assets import *

selection_methods = ["Best Selection", "Tournament Selection", "Roulette Selection"]
mutation_methods = ["Edge Mutation", "One Point Mutation", "Two Point Mutation"]
crossover_methods = ["One Point Crossover", "Two Point Crossover", "Three Point Crossover", "Uniform Crossover",
                     "Grainy Crossover"]


class GUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x1000")
        self.title("Evolution Algorithm")
        self.equation_frame = EquationEntryFrame(self, "Equation", "For instance x**2 = 5...")
        self.interval_start_frame = IntEntryFrame(self, "Beginning of an interval", "Enter the begginning of an interval..." )
        self.interval_end_frame = IntEntryFrame(self, "End of an interval", "Enter the end of an interval...")
        self.number_of_approximation_bits_frame = IntEntryFrame(self, "Number of approximation bits", "Enter the number of approximation bits...")
        self.number_of_child_per_population_frame = IntEntryFrame(self, "Number of children population", "Enter the number of children per population...")
        self.number_of_groups_frame = IntEntryFrame(self, "Groups Amount", "Enter the number of groups...")
        self.mutation_probability_frame = FloatEntryFrame(self, "Mutation Probability", "Enter the mutation probability...")
        self.selection_methods_frame = ComboBoxesFrame(self, "Selection Methods", selection_methods)
        self.mutation_methods_frame = ComboBoxesFrame(self, "Mutation Methods", mutation_methods)
        self.crossover_methods_frame = ComboBoxesFrame(self, "Crossover Methods", crossover_methods)

        self.algorithm_activation_button = ctk.CTkButton(self, text="Start Algorithm", command=None)

        self.set_frames()

    def set_frames(self):
        for i in range(11):
            self.grid_rowconfigure(i, weight=1)
        self.columnconfigure(0, weight=1)

        self.equation_frame.grid(row=0, column=0, sticky="nesw")
        self.interval_start_frame.grid(row=1, column=0, sticky="nesw")
        self.interval_end_frame.grid(row=2, column=0, sticky="nesw")
        self.number_of_approximation_bits_frame.grid(row=3, column=0, sticky="nesw")
        self.number_of_child_per_population_frame.grid(row=4, column=0, sticky="nesw")
        self.number_of_groups_frame.grid(row=5, column=0, sticky="nesw")
        self.mutation_probability_frame.grid(row=6, column=0, sticky="nesw")
        self.selection_methods_frame.grid(row=7, column=0, sticky="nesw")
        self.crossover_methods_frame.grid(row=8, column=0, sticky="nesw")
        self.mutation_methods_frame.grid(row=9, column=0, sticky="nesw")

        self.algorithm_activation_button.grid(row=10, column=0, padx=10, pady=10, sticky="nesw")

    def run_gui(self):
        self.mainloop()


