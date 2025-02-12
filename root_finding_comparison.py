import numpy as np
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from ui.root_finding_comparison import Ui_RootFindingComparison


class RootFindingComparisonApp(QMainWindow, Ui_RootFindingComparison):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.function_text_edit.setPlainText("x**2 - 5")
        self.xstart_text_edit.setPlainText("2")
        self.xend_text_edit.setPlainText("3")

        self.calculate_button.clicked.connect(self.calculate_root)

    def calculate_root(self):
        try:
            expr = self.function_text_edit.toPlainText()
            a = float(self.xstart_text_edit.toPlainText())
            b = float(self.xend_text_edit.toPlainText())

            def f(x):
                return eval(expr, {"x": x, "np": np})

            root, iterations = None, 0

            if self.bisection_radio.isChecked():
                root, iterations = self.bisection_method(f, a, b)

            elif self.secant_radio.isChecked():
                root, iterations = self.secant_method(f, a, b)

            if root is not None:
                exact_root = np.sqrt(5)

                relative_error = abs((root - exact_root) / exact_root) * 100

                self.root_value_label.setText(f"{root:.8f}")
                self.iterations_label.setText(str(iterations))
                self.exact_root_label.setText(f"{exact_root:.8f}")
                self.error_label.setText(f"{relative_error:.8f}%")
            else:
                self.root_value_label.setText("Error")
                self.iterations_label.setText("Error")
                self.exact_root_label.setText("Error")
                self.error_label.setText("Error")

        except Exception as e:
            self.show_error(f"Unexpected Error: {e}")

    def bisection_method(self, f, a, b, tol=1e-6):
        if f(a) * f(b) >= 0:
            print("Invalid initial values. f(a) and f(b) must be of different signs")
            return None, 0

        iterations = 0
        midpoint = (a + b) / 2

        while abs(f(midpoint)) > tol:
            iterations += 1
            if f(a) * f(midpoint) < 0:
                b = midpoint
            else:
                a = midpoint
            midpoint = (a + b) / 2

        return midpoint, iterations

    def secant_method(self, f, a, b, tol=1e-6):
        iterations = 0
        x0, x1 = a, b

        while abs(f(x1)) > tol:
            iterations += 1
            if f(x1) - f(x0) == 0:
                return None, iterations
            x_new = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
            x0, x1 = x1, x_new

        return x1, iterations

    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("Error")
        msg.setText(message)
        msg.exec()
