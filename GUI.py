import customtkinter as ctk


class GUI(ctk.CTk):
    def __init__(self):
        "Function build up whole GUI using other functions defined in this class"
        super().__init__()
        self.error_list = ["Incorrect beginning of the range", "Incorrect end of the range",
                           "Incorrect population amount", "Incorrect number of bits", "Incorrect generations amount",
                           "Incorrect groups amount", "Incorrect mutation probability", " "]
        self.geometry("500x800")
        self.title("Evolution Algorithms")
        self.create_widgets()
        self.set_widgets()
        self.update_combobox()

    def run_gui(self):
        "Function executes the GUI"
        self.mainloop()

    def create_widgets(self) -> None:
        "Function creates Widgets objects"
        self.overview_label = ctk.CTkLabel(master=self,
                                           text="Genetic Algorithm for finding solution of the given equation.")

        self.equation_entry = ctk.CTkEntry(master=self,placeholder_text="Enter the equation...")
        self.equation_entry.configure(fg_color="#FFDDC1", border_color="#FF4500", text_color="#00008B", height=40)

        self.range_start_entry = ctk.CTkEntry(master=self, placeholder_text="Enter the begining of the range...")
        self.range_end_entry = ctk.CTkEntry(master=self, placeholder_text="Enter the end of the range...")
        self.population_amount_entry = ctk.CTkEntry(master=self, placeholder_text="Enter the population amount...")
        self.number_of_bits_entry = ctk.CTkEntry(master=self, placeholder_text="Enter number of approximation bits...")
        self.generations_amount_entry = ctk.CTkEntry(master=self, placeholder_text="Enter number of generations...")
        self.groups_amount_entry = ctk.CTkEntry(master=self, placeholder_text="Enter Groups amount for tournament selection...")
        self.mutation_probability_entry = ctk.CTkEntry(master=self,
                                                       placeholder_text="Enter a mutation probability value...")

        self.selection_method_label = ctk.CTkLabel(master=self, text="Choose Selection Method")
        self.selection_method_comboBox = ctk.CTkComboBox(master=self)

        self.cross_method_label = ctk.CTkLabel(master=self, text="Choose Cross Method")
        self.cross_method_comboBox = ctk.CTkComboBox(master=self)

        self.mutation_method_label = ctk.CTkLabel(master=self, text="Choose Mutation Method")
        self.mutation_method_comboBox = ctk.CTkComboBox(master=self)

        self.error_label = ctk.CTkLabel(master=self, text="", text_color="red")

        self.start_algorithm_Button = ctk.CTkButton(master=self, text="Start", command=None)

    def set_widgets(self) -> None:
        "Function sets widgets in adequate places."
        for i in range(16):
            self.grid_rowconfigure(i, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.overview_label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.equation_entry.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.range_start_entry.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
        self.range_end_entry.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        self.population_amount_entry.grid(row=4, column=0, padx=5, pady=5, sticky="ew")
        self.number_of_bits_entry.grid(row=5, column=0, padx=5, pady=5, sticky="ew")
        self.generations_amount_entry.grid(row=6, column=0, padx=5, pady=5, sticky="ew")
        self.groups_amount_entry.grid(row=7, column=0, padx=5, pady=5, sticky="ew")
        self.mutation_probability_entry.grid(row=8, column=0, padx=5, pady=5, sticky="ew")

        self.selection_method_label.grid(row=9, column=0, padx=5, pady=5, sticky="ew")
        self.selection_method_comboBox.grid(row=10, column=0, padx=5, pady=5, sticky="ew")

        self.cross_method_label.grid(row=11, column=0, padx=5, pady=5, sticky="ew")
        self.cross_method_comboBox.grid(row=12, column=0, padx=5, pady=5, sticky="ew")

        self.mutation_method_label.grid(row=13, column=0, padx=5, pady=5, sticky="ew")
        self.mutation_method_comboBox.grid(row=14, column=0, padx=5, pady=5, sticky="ew")

        self.error_label.grid(row=15, column=0, padx=5, pady=5, sticky="ew")

        self.start_algorithm_Button.grid(row=16, column=0, padx=5, pady=5, sticky="ew")

    def update_combobox(self) -> None:
        "Function add options to select into ComboBox and configure them"
        selection_methods = ["Best Selection", "Tournament Selection", "Roulette Selection"]
        self.selection_method_comboBox.configure(values=selection_methods, state="readonly")
        self.selection_method_comboBox.set(selection_methods[0])

        crossing_methods = ["One Point CrossOver", "Two Point CrossOver", "Three Point CrossOver", "Uniform CrossOver",
                            "Grainy CrossOver"]
        self.cross_method_comboBox.configure(values=crossing_methods, state="readonly")
        self.cross_method_comboBox.set(crossing_methods[0])

        mutation_methods = ["Edge Mutation", "One Point Mutation", "Two Point Mutation"]
        self.mutation_method_comboBox.configure(values=mutation_methods, state="readonly")
        self.mutation_method_comboBox.set(mutation_methods[0])

    def check_if_correct_entry(self) -> int:
        try:
            float(self.range_start_entry.get())
        except ValueError:
            return 0

        try:
            float(self.range_end_entry.get())
        except ValueError:
            return 1
        if self.range_start_entry.get() >= self.range_end_entry.get():
            return 1

        try:
            int(self.population_amount_entry.get())
        except ValueError:
            return 2

        try:
            int(self.number_of_bits_entry.get())
        except ValueError:
            return 3

        try:
            int(self.generations_amount_entry.get())
        except ValueError:
            return 4

        try:
            int(self.groups_amount_entry.get())
        except ValueError:
            return 5

        try:
            float(self.mutation_probability_entry.get())
        except ValueError:
            return 6

        if self.mutation_probability_entry.get() >= 1:
            return 6

        return 7


my_gui = GUI()
my_gui.run_gui()
