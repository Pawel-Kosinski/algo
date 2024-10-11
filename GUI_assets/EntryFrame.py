import customtkinter as ctk


class EntryFrame(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk, label_text: str, entry_text: str):
        super().__init__(master)
        self.label_text = label_text
        self.entry_text = entry_text
        self.entry_content = None

        self.entry_label = ctk.CTkLabel(self, text=self.label_text)
        self.entry = ctk.CTkEntry(self, placeholder_text=self.entry_text)
        self.validation_label = ctk.CTkLabel(self, text=" ")

        self.entry.bind("<KeyRelease>", self.validate_entry_content)

        self.set_widgets()

    def set_widgets(self):
        for i in range(3):
            self.grid_rowconfigure(i, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.entry_label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.entry.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        self.validation_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

    def validate_entry_content(self, event=None):
        pass
