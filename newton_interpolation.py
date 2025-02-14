import numpy as np
from PyQt6.QtWidgets import QDialog, QMessageBox
from ui.newton_forward_interpolation import Ui_NewtonInterpolation

class NewtonInterpolationApp(QDialog, Ui_NewtonInterpolation):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.compute_button.clicked.connect(self.compute_interpolation)

    def compute_interpolation(self):
        try:
            x_str = self.x_input.text().strip()
            y_str = self.y_input.text().strip()
            interp_str = self.interp_input.text().strip()

            if not x_str or not y_str or not interp_str:
                raise ValueError("Please enter x values, y values, and an interpolation point.")

            x_values = np.array(list(map(float, x_str.split(','))))
            y_values = np.array(list(map(float, y_str.split(','))))
            x_interp = float(interp_str)

            if len(x_values) != len(y_values):
                raise ValueError("Number of x and y values must be equal.")
            if len(x_values) < 2:
                raise ValueError("At least two points are required for interpolation.")

            result = self.newton_forward_interpolation(x_values, y_values, x_interp)
            self.result_label.setText(f"Estimated value: {result:.5f}")

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def newton_forward_interpolation(self, x, y, x_interp):
        n = len(x)
        h = x[1] - x[0]
        p = (x_interp - x[0]) / h

        diff_table = np.zeros((n, n))
        diff_table[:, 0] = y

        for j in range(1, n):
            for i in range(n - j):
                diff_table[i][j] = diff_table[i + 1][j - 1] - diff_table[i][j - 1]

        result = y[0]
        factorial = 1
        product = 1

        for i in range(1, n):
            factorial *= i
            product *= (p - (i - 1))
            result += (product * diff_table[0][i]) / factorial

        return result
