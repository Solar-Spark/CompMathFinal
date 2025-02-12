import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from ui.graph_method import Ui_GraphMethod


class GraphMethodApp(QMainWindow, Ui_GraphMethod):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.function_text_edit.setPlainText("x**3 - 4*x + 1")
        self.xstart_text_edit.setPlainText("0")
        self.xend_text_edit.setPlainText("3")

        self.plot_graph_button.clicked.connect(self.plot_graph)
        self.calculate_error_button.clicked.connect(self.calculate_error)

    def plot_graph(self):
        try:
            expr = self.function_text_edit.toPlainText()
            x_start = float(self.xstart_text_edit.toPlainText())
            x_end = float(self.xend_text_edit.toPlainText())

            def f(x):
                return eval(expr, {"x": x, "np": np})

            x = np.linspace(x_start, x_end, 400)
            y = [f(val) for val in x]

            plt.figure(figsize=(4, 4))
            plt.plot(x, y, label=f"f(x) = {expr}", color="blue")
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
            print("Graph creation error:", e)

    def calculate_error(self):
        try:
            expr = self.function_text_edit.toPlainText()
            x_start = float(self.xstart_text_edit.toPlainText())
            x_end = float(self.xend_text_edit.toPlainText())

            def f(x):
                return eval(expr, {"x": x, "np": np})

            exact_root = secant_method(f, x_start, x_end)

            approx_root = float(self.approx_root_text_edit.toPlainText())

            abs_error = abs(exact_root - approx_root)

            self.exact_root_label.setText(f"{exact_root:.6f}")
            self.abs_err_label.setText(f"{abs_error:.6f}")

        except Exception as e:
            print("Error calculation error:", e)


def secant_method(f, x0, x1, tol=1e-6):
    while abs(f(x1)) > tol:
        x_temp = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0, x1 = x1, x_temp
    return x1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GraphMethodApp()
    window.show()
    sys.exit(app.exec())
