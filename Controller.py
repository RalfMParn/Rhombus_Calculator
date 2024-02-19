from Model import Model
from tkinter import *


class Controller:
    def __init__(self):
        self.model = None
        self.view = None

    def set_view(self, view):
        self.model = Model()
        self.view = view
        self.view.btn_arvuta.config(command=self.calculate_and_display_values)

    def calculate_and_display_values(self):
        valid_input = False
        while not valid_input:
            try:
                diag1 = float(self.view.diag_entry1.get())
                diag2 = float(self.view.diag_entry2.get())
                if diag1 <= 0 or diag2 <= 0:
                    raise ValueError("Diagonals peab olema positiivne arv")
                valid_input = True
            except ValueError as e:
                self.view.display_error(str(e))
                break

        if valid_input:
            diag1 = float(self.view.diag_entry1.get())
            diag2 = float(self.view.diag_entry2.get())

            area, perimeter, lng_diag = self.model.calculate_rhombus_values(diag1, diag2)

            if isinstance(area, float) and area.is_integer():
                area = int(area)
            if isinstance(perimeter, float) and perimeter.is_integer():
                perimeter = int(perimeter)
            if isinstance(lng_diag, float) and lng_diag.is_integer():
                lng_diag = int(lng_diag)

            # Display the calculated values in the text box
            self.view.text_box.config(state=NORMAL)
            self.view.text_box.delete(1.0, END)  # Clear previous content
            self.view.text_box.insert(END, f"Pindala: {area}\nÜmbermõõt: {perimeter}\nPikkem Diagonal: {lng_diag}")
            self.view.text_box.config(state=DISABLED)


