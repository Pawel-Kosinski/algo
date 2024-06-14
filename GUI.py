import customtkinter as ctk
import tkinter as tk
from population import Population
from chromosom import Chromosome
from chromosom import set_Global_Values
import sympy as sp







class GUI(ctk.CTk):

    def __init__(self,app_name : str,resolution : str):
        "Function build up whole GUI using other functions defined in this class"
        super().__init__()
        self.geometry(resolution)
        self.create_Widgets()
        self.set_Widgets()
        self.update_ComboBoxes()
        self.title(app_name)



    def run_GUI(self) -> None:
        "Function executes the GUI"
        self.mainloop()


    def set_Appearance(self,appearance_theme : str, color : str) -> None:
        "Function sets appearance dark/light mode"
        ctk.set_appearance_mode(appearance_theme)
        ctk.set_default_color_theme(color)


    def create_Widgets(self) -> None:
        "Function creates Widgets objects"
        self.overview_Label = ctk.CTkLabel(master=self,text="Genetic Algorithm for finding solution of the given equation.")

        self.equation_Entry = ctk.CTkEntry(master=self, placeholder_text="Enter the equation...")

        self.range_start_Entry = ctk.CTkEntry(master=self,placeholder_text="Enter the begining of the range...")
        self.range_end_Entry = ctk.CTkEntry(master=self,placeholder_text="Enter the end of the range...")
        self.population_amount_Entry = ctk.CTkEntry(master=self,placeholder_text="Enter the population amount...")
        self.number_of_bits_Entry = ctk.CTkEntry(master=self,placeholder_text="Enter number of approxiamition bits...")
        self.generations_amount_Entry = ctk.CTkEntry(master=self,placeholder_text="Enter number of generations")
        self.groups_Amount_Entry = ctk.CTkEntry(master=self,placeholder_text="Enter Groups amount...")
        self.mutation_probability_Entry = ctk.CTkEntry(master=self,placeholder_text="Enter a mutation probability value...")

        self.selection_method_Label = ctk.CTkLabel(master=self,text="Choose Selection Method")
        self.selection_method_ComboBox = ctk.CTkComboBox(master=self)

        self.cross_method_Label = ctk.CTkLabel(master=self,text="Choose Cross Method")
        self.cross_method_ComboBox = ctk.CTkComboBox(master=self)

        self.mutation_method_Label = ctk.CTkLabel(master=self,text="Choose Mutation Method")
        self.mutation_method_ComboBox = ctk.CTkComboBox(master=self)

        self.start_algorithm_Button = ctk.CTkButton(master=self,text="Start",command=self.start_Button_Function)


    def set_Widgets(self) -> None:
        "Function sets widgets in adequate places."
        for i in range(15):
            self.grid_rowconfigure(i, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.overview_Label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.equation_Entry.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        self.equation_Entry.configure(fg_color="blue", text_color="white", height=40)

        self.range_start_Entry.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
        self.range_end_Entry.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        self.population_amount_Entry.grid(row=4, column=0, padx=5, pady=5, sticky="ew")
        self.number_of_bits_Entry.grid(row=5, column=0, padx=5, pady=5, sticky="ew")
        self.generations_amount_Entry.grid(row=6, column=0, padx=5, pady=5, sticky="ew")
        self.groups_Amount_Entry.grid(row=7, column=0, padx=5, pady=5, sticky="ew")
        self.mutation_probability_Entry.grid(row=8, column=0, padx=5, pady=5, sticky="ew")

        self.selection_method_Label.grid(row=9, column=0, padx=5, pady=5, sticky="ew")
        self.selection_method_ComboBox.grid(row=10, column=0, padx=5, pady=5, sticky="ew")

        self.cross_method_Label.grid(row=11, column=0, padx=5, pady=5, sticky="ew")
        self.cross_method_ComboBox.grid(row=12, column=0, padx=5, pady=5, sticky="ew")

        self.mutation_method_Label.grid(row=13, column=0, padx=5, pady=5, sticky="ew")
        self.mutation_method_ComboBox.grid(row=14, column=0, padx=5, pady=5, sticky="ew")

        self.start_algorithm_Button.grid(row=15, column=0, padx=5, pady=5, sticky="ew")


    def update_ComboBoxes(self) -> None:
        "Function add options to select into ComboBox and configure them"

        selection_Methods = ["Best Selection", "Tournament Selection", "Roulette Selection"]
        self.selection_method_ComboBox.configure(values = selection_Methods, state="readonly")
        self.selection_method_ComboBox.set(selection_Methods[0])

        crossing_Methods = ["One Point CrossOver", "Two Point CrossOver", "Three Point CrossOver", "Uniform CrossOver", "Grainy CrossOver"]
        self.cross_method_ComboBox.configure(values = crossing_Methods, state="readonly")
        self.cross_method_ComboBox.set(crossing_Methods[0])

        mutation_Methods = ["Edge Mutation", "One Point Mutation", "Two Point Mutation"]
        self.mutation_method_ComboBox.configure(values = mutation_Methods, state="readonly")
        self.mutation_method_ComboBox.set(mutation_Methods[0])


    def display_Error_Window(self, error_Message : str) -> None:
        "Function displays error window"

        error_Window = ctk.CTkToplevel()
        error_Window.title("Error")

        error_Window.geometry("300x100")

        error_Label = ctk.CTkLabel(master=error_Window, text=error_Message, text_color="red")
        error_Label.pack(pady=20, padx=20)

        close_Button = ctk.CTkButton(master=error_Window, text="Close", command=error_Window.destroy)
        close_Button.pack(pady=10)


    def display_Result_Window(self , result : tuple) -> None:
        "Function displays result of a Equation"

        result_Window = ctk.CTkToplevel()
        result_Window.title("Result")

        for i in range(5):
            result_Window.grid_rowconfigure(i, weight=1)
        result_Window.grid_columnconfigure(0, weight=1)

        result_Window.geometry("500x400")
        
        result_Label = ctk.CTkLabel(master=result_Window, text="The smallest best sollution:")
        result_Label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        xVar_Label = ctk.CTkLabel(master=result_Window, text=f"x: {result[0]}")
        xVar_Label.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        yVar_Label = ctk.CTkLabel(master=result_Window, text=f"y: {result[0]}")
        yVar_Label.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        close_Button = ctk.CTkButton(master=result_Window, text="Close", command=result_Window.destroy)
        close_Button.grid(row=3, column=0, padx=5, pady=5, sticky="ew")



    def reset_Widgets_Input(self) -> None:
        "Function Clear Inputs of Entries"

        self.range_start_Entry.delete(0, ctk.END)
        self.range_end_Entry.delete(0, ctk.END)
        self.population_amount_Entry.delete(0, ctk.END)
        self.number_of_bits_Entry.delete(0, ctk.END)
        self.generations_amount_Entry.delete(0, ctk.END)
        self.groups_Amount_Entry.delete(0, ctk.END)
        self.mutation_probability_Entry.delete(0, ctk.END)


    def interpret_Function(self, input_Equation : str) -> sp.Expr:
        "This function interprets string input into mathematical equation"
        x_Var = sp.symbols('x')

        function = sp.sympify(input_Equation)
        return function
      

    def start_Button_Function(self) -> None:
        "Function take inputs of entries and comboBoxes and then execute the algorithm"

        input_Equation = self.equation_Entry.get()

        range_start = self.range_start_Entry.get()
        range_end = self.range_end_Entry.get()
        population_amount = self.population_amount_Entry.get()
        number_of_bits = self.number_of_bits_Entry.get()
        generations_Amount = self.generations_amount_Entry.get()
        groups_Amount = self.groups_Amount_Entry.get()
        mutation_probability = self.mutation_probability_Entry.get()

        selection_method = self.selection_method_ComboBox.get()
        cross_method = self.cross_method_ComboBox.get()
        mutation_method = self.mutation_method_ComboBox.get()

        try:
            self.interpreted_Equation = self.interpret_Function(input_Equation)
        except (sp.SympifyError , TypeError):
            self.display_Error_Window("InCorrect Equation")
            self.reset_Widgets_Input()

        try:
            set_Global_Values(float(range_start) ,float(range_end) ,int(number_of_bits), int(population_amount))
        except ValueError as error:
            self.display_Error_Window("InCorrect Input")
            self.reset_Widgets_Input()
    

        self.chromosome = Chromosome()
        self.best_Solutions = []
        self.population = Population(self.chromosome, self.interpreted_Equation)


        for current_Epoch in range(int(generations_Amount)):
            self.best_Solutions = self.population.best_Solution(current_Epoch, self.best_Solutions)

            try:
                self.population.evolve(int(groups_Amount), selection_method, cross_method , mutation_method , float(mutation_probability))
            except ValueError as error:
                self.display_Error_Window("InCorrect Input")
                self.reset_Widgets_Input()
    
        self.display_Result_Window(self.population.print_Best(self.best_Solutions))   