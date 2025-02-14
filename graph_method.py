import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtGui import QPixmap
from ui.graph_method import Ui_GraphMethod


class GraphMethodApp(QMainWindow, Ui_GraphMethod):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.plot_graph_button.clicked.connect(self.plot_graph)
        self.calculate_error_button.clicked.connect(self.calculate_error)

    def plot_graph(self):
        try:
            function = self.function_text_edit.toPlainText()
            x_start = float(self.xstart_text_edit.toPlainText())
            x_end = float(self.xend_text_edit.toPlainText())

            def f(x):
                return eval(function, {"x": x, "np": np})

            x = np.linspace(x_start, x_end, 400)
            y = [f(val) for val in x]

            plt.figure(figsize=(4, 4))
            plt.plot(x, y, label=f"f(x) = {function}", color="blue")
            plt.axhline(0, color='black', linewidth=1)
            plt.axvline(0, color='black', linewidth=1)
            plt.grid()
            plt.legend()

            plt.savefig("graph.png")
            plt.close()

            pixmap = QPixmap("graph.png")
            self.graph_label.setPixmap(pixmap)
            self.graph_label.setScaledContents(True)

        except Exception as e:
            self.show_error(f"Unexpected Error: {e}")

    def calculate_error(self):
        try:
            expr = self.function_text_edit.toPlainText()
            x_start = float(self.xstart_text_edit.toPlainText())
            x_end = float(self.xend_text_edit.toPlainText())

            def f(x):
                return eval(expr, {"x": x, "np": np})

            exact_root = self.secant_method(f, x_start, x_end)

            approx_root = float(self.approx_root_text_edit.toPlainText())

            abs_error = abs(exact_root - approx_root)

            self.exact_root_label.setText(f"{exact_root:.6f}")
            self.abs_err_label.setText(f"{abs_error:.6f}")

        except Exception as e:
            print("Error calculation error:", e)

    def secant_method(self, f, x0, x1, tol=1e-6):
        while abs(f(x1)) > tol:
            x_new = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
            x0, x1 = x1, x_new
        return x1

    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("Error")
        msg.setText(message)
        msg.exec()