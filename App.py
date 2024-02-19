from Controller import Controller
from Model import Model
from View import View


class App:
    def __init__(self):
        self.view = View(self)
        self.model = Model()

    def main(self):
        self.view.main()


if __name__ == "__main__":
    rhombus = App()
    rhombus.main()
