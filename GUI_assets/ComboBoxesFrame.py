import customtkinter as ctk


class ComboBoxesFrame(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk, label_text: str, combobox_options: list) -> None:
        super().__init__(master)
        self.label_text = label_text
        self.combobox_options = combobox_options

        self.combo_box_label = ctk.CTkLabel(self, text=self.label_text)
        self.combo_box = ctk.CTkComboBox(self, values=self.combobox_options, state="readonly")

        self.combo_box.set(self.combobox_options[0])
        self.set_widgets()

    def set_widgets(self) -> None:
        for i in range(2):
            self.grid_rowconfigure(i, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.combo_box_label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.combo_box.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
