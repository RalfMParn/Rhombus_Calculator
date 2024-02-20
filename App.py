from Model import Rhombus
from View import View


class App:
    def __init__(self):
        self.view = View(self)
        self.model = Rhombus()

    def main(self):
        self.view.main()


if __name__ == "__main__":
    rhombus = App()
    rhombus.main()

