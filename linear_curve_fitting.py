import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from ui.linear_curve_fitting import Ui_LinearCurveFitting


class LinearCurveFittingApp(QDialog, Ui_LinearCurveFitting):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.plot_button.clicked.connect(self.plot_fit)

        self.plot_area.setFixedSize(600, 400)

    def plot_fit(self):
        try:
            x_str = self.x_input.text().strip()
            y_str = self.y_input.text().strip()

            if not x_str or not y_str:
                raise ValueError("Please enter both x and y values.")

            x_values = np.array(list(map(float, x_str.split(','))))
            y_values = np.array(list(map(float, y_str.split(','))))

            if len(x_values) != len(y_values):
                raise ValueError("Number of x and y values must be equal.")
            if len(x_values) < 2:
                raise ValueError("At least two points are required for linear fitting.")

            coefficients = np.polyfit(x_values, y_values, 1)
            slope, intercept = coefficients
            fitted_y = slope * x_values + intercept

            plt.figure(figsize=(10, 8), dpi=100)
            plt.scatter(x_values, y_values, color='red', label='Data Points')
            plt.plot(x_values, fitted_y, color='blue', label=f'Fit: y = {slope:.3f}x + {intercept:.3f}')
            plt.xlabel("X values", fontsize=14)
            plt.ylabel("Y values", fontsize=14)
            plt.legend(fontsize=14)
            plt.title("Linear Curve Fitting", fontsize=16)
            plt.grid(True)

            plot_path = "linear_fit.png"
            plt.savefig(plot_path, dpi=150, bbox_inches='tight')
            plt.close()

            pixmap = QPixmap(plot_path)
            scaled_pixmap = pixmap.scaled(self.plot_area.width(), self.plot_area.height(), Qt.AspectRatioMode.KeepAspectRatio)

            self.plot_area.setPixmap(scaled_pixmap)
            self.plot_area.setAlignment(Qt.AlignmentFlag.AlignCenter)

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
