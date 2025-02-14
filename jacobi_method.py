import numpy as np
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from ui.jacobi_method import Ui_JacobiMethod


class JacobiMethodApp(QMainWindow, Ui_JacobiMethod):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.size_spinbox.setValue(3)
        self.iterations_spinbox.setValue(1000)
        self.size_spinbox.valueChanged.connect(self.update_table_size)

        self.solve_button.clicked.connect(self.solve_system)

        self.update_table_size()

    def update_table_size(self):
        n = self.size_spinbox.value()

        self.coeff_table.setRowCount(n)
        self.coeff_table.setColumnCount(n + 1)

        self.initial_guess_table.setRowCount(1)
        self.initial_guess_table.setColumnCount(n)

        for i in range(n):
            for j in range(n + 1):
                self.coeff_table.setItem(i, j, QTableWidgetItem(str(0)))
            self.initial_guess_table.setItem(0, i, QTableWidgetItem("0"))

    def solve_system(self):
        try:
            n = self.size_spinbox.value()
            a = np.zeros((n, n))
            b = np.zeros(n)

            for i in range(n):
                for j in range(n):
                    a[i, j] = float(self.coeff_table.item(i, j).text())
                b[i] = float(self.coeff_table.item(i, n).text())

            x0 = np.zeros(n)

            for j in range(n):
                x0[j] = float(self.initial_guess_table.item(0, j).text())

            max_iter = self.iterations_spinbox.value()

            solution = self.jacobi_method(a, b, x0, 1e-6, max_iter)
            self.solution_table.setRowCount(1)
            self.solution_table.setColumnCount(n)

            if solution != "no conv":
                for j in range(n):
                    self.solution_table.setItem(0, j, QTableWidgetItem(f"{solution[j]:.6f}"))
            else:
                for j in range(n):
                    self.solution_table.setItem(0, j, QTableWidgetItem("No conv"))
        except Exception as e:
            self.show_error(f"Unexpected Error: {e}")

    def jacobi_method(self, a, b, x0, tol=1e-6, max_iter=1000):
        n = len(b)
        x = x0
        for _ in range(max_iter):
            x_new = np.zeros_like(x)
            for i in range(n):
                summation = sum(a[i][j] * x[j] for j in range(n) if j != i)
                x_new[i] = (b[i] - summation) / a[i][i]

            if np.linalg.norm(x_new - x, ord=np.inf) < tol:
                return x_new
            x = x_new

        return "no conv"

    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("Error")
        msg.setText(message)
        msg.exec()