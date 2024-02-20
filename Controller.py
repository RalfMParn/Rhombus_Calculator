from Model import Rhombus
from tkinter import *


class Controller:
    def __init__(self):
        self.model = None
        self.view = None

    def set_view(self, view):
        self.model = Rhombus()
        self.view = view
        self.view.btn_arvuta.config(command=self.calculate_and_display_values)

    def calculate_and_display_values(self):
        valid_input = False
        while not valid_input:
            try:
                diag1 = float(self.view.diag_entry1.get())
                diag2 = float(self.view.diag_entry2.get())
                if diag1 <= 0 or diag2 <= 0:
                    raise ValueError("Väärtused on vigane.Peab olema positiivne arv.")

                if diag2 > diag1:
                    raise ValueError("Kõrgus (h) peab olema rombi moodustamiseks väiksem või võrdne külje pikkusega (a).")
                valid_input = True
            except ValueError as e:
                self.view.display_error(str(e))
                break

        if valid_input:
            diag1 = float(self.view.diag_entry1.get())
            diag2 = float(self.view.diag_entry2.get())

            area, perimeter, diagonal1, diagonal2, lng_diag = self.model.calculate_rhombus_values(diag1, diag2)

            if isinstance(area, float) and area.is_integer():
                area = int(area)
            if isinstance(perimeter, float) and perimeter.is_integer():
                perimeter = int(perimeter)
            if isinstance(diagonal1, float) and diagonal1.is_integer():
                diagonal1 = int(diagonal1)
            if isinstance(diagonal2, float) and diagonal2.is_integer():
                diagonal2 = int(diagonal2)

            diag1 = str(diag1).rstrip('.0')
            diag2 = str(diag2).rstrip('.0')
            lng_diag = str(lng_diag).rstrip('.0')

            # Display the calculated values in the text box
            self.view.text_box.config(state=NORMAL)
            self.view.text_box.delete(1.0, END)  # Clear previous content
            self.view.diag_entry1.delete(0, END)
            self.view.diag_entry2.delete(0, END)
            self.view.text_box.insert(END, f"Kõrgus: {diag1}\nÄäre pikkus: {diag2}\nPindala: {area}\nÜmbermõõt: {perimeter}\nDiagonaal 1: {diagonal1}\nDiagonaal 2: {diagonal2}\nPikkem diagonaal: {lng_diag}")
            self.view.text_box.config(state=DISABLED)
