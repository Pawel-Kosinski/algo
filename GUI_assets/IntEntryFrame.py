from GUI_assets.EntryFrame import EntryFrame
import customtkinter as ctk


class IntEntryFrame(EntryFrame):
    def validate_entry_content(self, event=None):
        self.entry_content = self.entry.get()
        try:
            self.entry_content = int(self.entry_content)
            self.validation_label.configure(text="✔", text_color="green")
        except ValueError:
            self.validation_label.configure(text="✘", text_color="red")

    def get_entry_content(self):
        return int(self.entry_content)


class IntervalEndEntryFrame(IntEntryFrame):
    def __init__(self, master: ctk.CTk, label_text: str, entry_text: str, interval_start_frame: IntEntryFrame):
        super().__init__(master, label_text, entry_text)
        self.interval_start_value = interval_start_frame.get_entry_content()

    def validate_entry_content(self, event=None):
        super().validate_entry_content(self)
        if self.interval_start_value < self.get_entry_content():
            self.validation_label.configure(text="✘", text_color="red")
