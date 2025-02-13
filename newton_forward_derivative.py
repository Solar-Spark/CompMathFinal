import numpy as np
from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox
from ui.newton_forward_derivative import Ui_NewtonForwardDerivative

class NewtonForwardDerivativeApp(QDialog, Ui_NewtonForwardDerivative):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_calculate.clicked.connect(self.calculate_derivative)

    def calculate_derivative(self):
        try:
            x_str = self.lineEdit_x.text().strip()
            y_str = self.lineEdit_y.text().strip()
            
            if not x_str or not y_str:
                raise ValueError("Please enter both x and y values.")
            
            x_values = list(map(float, x_str.split(',')))
            y_values = list(map(float, y_str.split(',')))

            if len(x_values) != len(y_values):
                raise ValueError("Number of x and y values must be equal.")
            if len(x_values) < 3:
                raise ValueError("At least three points are required.")
            
            h = x_values[1] - x_values[0]
            for i in range(1, len(x_values)-1):
                if not np.isclose(x_values[i+1] - x_values[i], h):
                    raise ValueError("x values must be equally spaced.")
            
            mid_index = len(x_values) // 2
            target_x = x_values[mid_index]
            
            delta_y0 = y_values[1] - y_values[0]
            delta2_y0 = y_values[2] - 2 * y_values[1] + y_values[0]
            
            derivative = (delta_y0 / h) - (delta2_y0 / (2 * h))
            
            self.label_result.setText(
                f"<b>dy/dx at x={target_x:.2f}</b>: {derivative:.6f}"
            )
        
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
