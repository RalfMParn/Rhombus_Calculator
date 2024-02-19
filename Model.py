from cmath import sqrt


class Model:
    def __init__(self):
        self.view = None

    @staticmethod
    def is_number(user_input):
        try:
            int(user_input)
            return True
        except ValueError:
            return False
    def calculate_rhombus_values(self, diag1, diag2):
        # Calculate area and perimeter of rhombus
        area = (diag1 * diag2) / 2
        perimeter = 2 * (sqrt(diag1 ** 2 + diag2 ** 2))
        #  lng_diag = sqrt(diag1 ** 2 + diag2 ** 2)
        if diag1 > diag2:
            lng_diag = diag1
        else:
            lng_diag = diag2

        # Rounds the number to 6 decimal places
        perimeter = round(perimeter.real, 6)
        lng_diag = round(lng_diag.real, 6)

        return area, perimeter, lng_diag
