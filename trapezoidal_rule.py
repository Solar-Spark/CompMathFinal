import numpy as np
from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox
from ui.trapezoidal_rule import Ui_TrapezoidalRule

class TrapezoidalRuleApp(QDialog, Ui_TrapezoidalRule):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_calculate.clicked.connect(self.calculate_integral)
    
    def function(self, x):
        return x**2 + x

    def calculate_integral(self):
        try:
            a = float(self.lineEdit_a.text().strip())
            b = float(self.lineEdit_b.text().strip())
            n = int(self.lineEdit_n.text().strip())
            
            if n <= 0:
                raise ValueError("Number of subintervals must be positive.")
            
            h = (b - a) / n
            x_values = np.linspace(a, b, n + 1)
            y_values = self.function(x_values)
            
            integral_approx = (h / 2) * (y_values[0] + 2 * np.sum(y_values[1:-1]) + y_values[-1])
            exact_value = (b**3 / 3 + b**2 / 2) - (a**3 / 3 + a**2 / 2)
            
            result_text = (f"<b>Approximate Integral:</b> {integral_approx:.6f}<br>"
                           f"<b>Exact Integral:</b> {exact_value:.6f}<br>"
                           f"<b>Error:</b> {abs(integral_approx - exact_value):.6f}")
            self.label_result.setText(result_text)
        
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))