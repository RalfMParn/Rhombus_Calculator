from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from Controller import Controller


class View(Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        # Size of the frame
        self.__width = 550
        self.__height = 280
        self.default_Font = font.Font(family="Verdana", size=14)

        # Window characteristics
        self.title("Rhombi GUI")
        self.center_window(self.__width, self.__height)

        # Creates 2 frames
        self.top_frame = self.create_top_frame()
        self.bottom_frame = self.create_bottom_frame()

        # button creation
        (self.btn_arvuta, self.lbl_info, self.lbl_info2, self.diag_entry1, self.diag_entry2,
         self.text_box) = self.create_frame_widgets

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def main(self):
        self.mainloop()

    def center_window(self, width, height):
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (width // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_top_frame(self):
        frame = Frame(self, bg="#ffe5c5", height=15)
        frame.pack(expand=True, fill=BOTH)
        return frame

    def create_bottom_frame(self):
        frame = Frame(self)
        frame.pack(expand=True, fill=BOTH)
        return frame

    @property
    def create_frame_widgets(self):
        # Creates the calculate (arvuta) button
        btn_arvuta = Button(self.top_frame, text="Arvuta", font=self.default_Font, width=10, height=1,
                            command=lambda: Controller.calculate_and_display_values(self.controller))
        btn_arvuta.grid(row=1, column=3, padx=5, pady=5)

        lbl_info = Label(self.top_frame, text="Diagonal 1", bg="#ffe5c5", font=self.default_Font)
        lbl_info.grid(row=0, column=0, padx=5, pady=5)

        lbl_info2 = Label(self.top_frame, text="Diagonal 2", bg="#ffe5c5", font=self.default_Font)
        lbl_info2.grid(row=1, column=0, padx=5, pady=5)

        diag_entry1 = Entry(self.top_frame, font=self.default_Font)
        diag_entry1.grid(row=0, column=1, padx=5, pady=5)

        diag_entry2 = Entry(self.top_frame, font=self.default_Font)
        diag_entry2.grid(row=1, column=1, padx=5, pady=5)

        text_box = Text(self.bottom_frame, font=self.default_Font, state=DISABLED)
        scrollbar = Scrollbar(self.bottom_frame, orient="vertical")
        scrollbar.config(command=text_box.yview)
        text_box.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        text_box.pack(expand=True, fill=BOTH, padx=5, pady=5)

        return btn_arvuta, lbl_info, lbl_info2, diag_entry1, diag_entry2, text_box

    @staticmethod
    def display_error(error):
        messagebox.showerror("Viga", f"Raadius on vigane. Diagonals peab olema positiivne arv. Error: {error}")

    def on_close(self):
        if messagebox.askokcancel("Väljub kalkulaatorist", "Oled sa kindel, et tahad kalkulaatorist lahkuda?"):
            self.destroy()
