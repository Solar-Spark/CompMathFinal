import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from ui.linear_curve_fitting import Ui_LinearCurveFitting


class LinearCurveFittingApp(QDialog, Ui_LinearCurveFitting):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.plot_button.clicked.connect(self.plot_fit)

        self.plot_area.setFixedSize(400, 400)

    def plot_fit(self):
        try:
            x_str = self.x_input.text().strip()
            y_str = self.y_input.text().strip()

            if not x_str or not y_str:
                raise ValueError("Please enter both x and y values.")

            x = np.array(list(map(float, x_str.split(','))))
            y = np.array(list(map(float, y_str.split(','))))

            if len(x) != len(y):
                raise ValueError("Number of x and y values must be equal.")
            if len(x) < 2:
                raise ValueError("At least two points are required for linear fitting.")

            coefficients = np.polyfit(x, y, 1)
            m, c = coefficients
            fit_curve = m * x + c

            plt.figure(figsize=(4, 4))
            plt.scatter(x, y, color='red', label='Data Points')
            plt.plot(x, fit_curve, color='blue', label=f'Fit: y = {m:.3f}x + {c:.3f}')
            plt.axhline(0, color='black', linewidth=1)
            plt.axvline(0, color='black', linewidth=1)
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.legend()
            plt.title("Linear Curve Fitting")
            plt.grid(True)
            plot_path = "graph.png"
            plt.savefig(plot_path, bbox_inches='tight')
            plt.close()

            pixmap = QPixmap(plot_path)
            scaled_pixmap = pixmap.scaled(self.plot_area.width(), self.plot_area.height(), Qt.AspectRatioMode.KeepAspectRatio)

            self.plot_area.setPixmap(scaled_pixmap)
            self.plot_area.setAlignment(Qt.AlignmentFlag.AlignCenter)

        except Exception as e:
            QMessageBox.critical(self, "Error: ", str(e))
