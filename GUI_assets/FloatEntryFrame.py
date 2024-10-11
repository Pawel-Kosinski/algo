from GUI_assets.EntryFrame import EntryFrame


class FloatEntryFrame(EntryFrame):
    def validate_entry_content(self, event=None):
        self.entry_content = self.entry.get()
        try:
            self.entry_content = float(self.entry_content)
            if self.entry_content > 1. or self.entry_content < 0.:
                raise ValueError
            self.validation_label.configure(text="✔", text_color="green")
        except ValueError:
            self.validation_label.configure(text="✘", text_color="red")

    def get_entry_content(self):
        return float(self.entry_content)
