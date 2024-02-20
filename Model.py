from cmath import sqrt

class Model:
    pass


class Rhombus:
    def __init__(self):
        self.view = None

    @staticmethod
    def is_number(user_input):
        try:
            int(user_input)
            return True
        except ValueError:
            return False
    def calculate_rhombus_values(self, side_length, height):
        self.side_length = side_length
        self.height = height
        # Calculate area and perimeter of rhombus
        area = self.side_length * self.height

        perimeter = 4 * self.side_length
        diagonal1 = 2 * self.height
        diagonal2 = 2 * sqrt(self.side_length ** 2 - (self.height / 2) ** 2)

        perimeter = round(perimeter.real, 6)
        diagonal1 = round(diagonal1.real, 6)
        diagonal2 = round(diagonal2.real, 6)

        if diagonal1 > diagonal2:
            lng_diag = diagonal1
        else:
            lng_diag = diagonal2

        return area, perimeter, diagonal1, diagonal2, lng_diag
