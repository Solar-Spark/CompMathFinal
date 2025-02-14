import numpy as np
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from ui.trapezoidal_rule import Ui_TrapezoidalRule
from scipy.integrate import quad


class TrapezoidalRuleApp(QMainWindow, Ui_TrapezoidalRule):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.calculate_button.clicked.connect(self.compute_integral)

    def compute_integral(self):
        try:
            function = self.function_input.text()

            def f(x):
                return eval(function, {"x": x, "np": np})

            lower_limit = float(self.lower_limit_input.text())
            upper_limit = float(self.upper_limit_input.text())

            n = int(self.subintervals_number_input.text())
            if n <= 0:
                raise ValueError("Number of subintervals must be more than 0")

            integral_value = self.trapezoidal_rule(f, lower_limit, upper_limit, n)

            exact_value, _ = quad(f, lower_limit, upper_limit)

            error = abs(float(exact_value) - integral_value)

            self.calculated_value_label.setText(f"{integral_value:.6f}")
            self.exact_value_label.setText(f"{exact_value:.6f}")
            self.error_label.setText(f"{error:.6f}")

        except Exception as e:
            self.show_error(f"Input Error: {e}")

    def trapezoidal_rule(self, f, a, b, n):
        h = (b - a) / n
        x_values = np.linspace(a, b, n + 1)
        y_values = f(x_values)

        integral = h * (y_values[0] + 2 * sum(y_values[1:-1]) + y_values[-1])/2
        return integral

    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("Error")
        msg.setText(message)
        msg.exec()
