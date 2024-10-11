from .EntryFrame import EntryFrame
import customtkinter as ctk
import sympy as sp


class EquationEntryFrame(EntryFrame):
    def __init__(self,  master: ctk.CTk, label_text: str, entry_text: str):
        super().__init__(master, label_text, entry_text)
        self.params_number = None
        self.variables = None
        self.coefficients = None
        self.left_expr = None
        self.right_expr = None

    def validate_entry_content(self, event=None):
        self.entry_content = self.entry.get()
        if self.check_if_correct_equation():
            self.validation_label.configure(text="✔", text_color="green")
        else:
            self.validation_label.configure(text="✘", text_color="red")

    def check_if_correct_equation(self):
        try:
            if "=" not in self.entry_content:
                return False
            left_side, right_side = self.entry_content.split("=")

            self.left_expr = sp.sympify(left_side)
            self.right_expr = sp.sympify(right_side)

            self.entry_content = sp.Eq(self.left_expr, self.right_expr)
            return True

        except (sp.SympifyError, ValueError):
            return False

    def get_entry_content(self):
        variables = list(self.left_expr.free_symbols.union(self.right_expr.free_symbols))
        equation = self.left_expr - self.right_expr
        self.variables = variables
        return self.variables, equation

