import numpy as np
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from ui.newton_forward_derivative import Ui_NewtonForwardDerivative


class NewtonForwardDerivativeApp(QMainWindow, Ui_NewtonForwardDerivative):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.calculate_button.clicked.connect(self.compute_derivative)

    def compute_derivative(self):
        try:
            x_str = self.x_values_input.text().strip()
            y_str = self.y_values_input.text().strip()
            x_values = np.array(list(map(float, x_str.split(','))))
            y_values = np.array(list(map(float, y_str.split(','))))

            x_target = float(self.x_value_input.text())

            if x_target not in x_values:
                raise ValueError(f"x={x_target} not found in the dataset.")

            index = np.where(x_values == x_target)[0][0]

            h = x_values[1] - x_values[0]

            if index == 0:
                derivative = (y_values[index + 1] - y_values[index]) / h
            elif index == len(x_values) - 1:
                derivative = (y_values[index] - y_values[index - 1]) / h
            else:
                derivative = (y_values[index + 1] - y_values[index - 1]) / (2 * h)

            self.result_label.setText(f"dy/dx at x={x_target} ≈ {derivative:.6f}")

        except ValueError as ve:
            self.show_error(f"Input Error: {ve}")
        except Exception as e:
            self.show_error(f"Unexpected Error: {e}")

    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("Error")
        msg.setText(message)
        msg.exec()
