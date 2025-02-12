import numpy as np
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox
from ui.matrix_inversion import Ui_MatrixInversion


class MatrixInversionApp(QMainWindow, Ui_MatrixInversion):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.size_spinbox.setValue(3)
        self.size_spinbox.valueChanged.connect(self.update_table_size)

        self.solve_button.clicked.connect(self.compute_inverse)

        self.update_table_size()

    def update_table_size(self):
        n = self.size_spinbox.value()

        self.matrix_table.setRowCount(n)
        self.matrix_table.setColumnCount(n)

        self.inverse_matrix_table.setRowCount(n)
        self.inverse_matrix_table.setColumnCount(n)

        for i in range(n):
            for j in range(n):
                self.matrix_table.setItem(i, j, QTableWidgetItem("0"))

    def compute_inverse(self):
        try:
            n = self.size_spinbox.value()
            a = np.zeros((n, n))

            for i in range(n):
                for j in range(n):
                    item = self.matrix_table.item(i, j)
                    if item is None or item.text().strip() == "":
                        raise ValueError(f"Empty cell at A[{i}][{j}]")
                    a[i, j] = float(item.text())

            if np.linalg.det(a) == 0:
                raise ValueError("Matrix is singular and cannot be inverted.")

            inverse_matrix = self.iterative_inverse(a)

            if isinstance(inverse_matrix, np.ndarray):
                for i in range(n):
                    for j in range(n):
                        self.inverse_matrix_table.setItem(i, j, QTableWidgetItem(f"{inverse_matrix[i, j]:.6f}"))
            else:
                self.show_error("Method did not converge.")

        except ValueError as ve:
            self.show_error(f"Input Error: {ve}")
        except Exception as e:
            self.show_error(f"Unexpected Error: {e}")

    def iterative_inverse(self, A, tol=1e-6, max_iter=100):
        n = len(A)
        i = np.eye(n)
        trace_a = np.trace(A)
        if trace_a == 0:
            raise ValueError("Trace of matrix is zero. Cannot initialize x0.")
        x = (1 / trace_a) * i
        for _ in range(max_iter):
            x_new = 2 * x - x @ A @ x
            if np.linalg.norm(A @ x_new - i, ord=np.inf) < tol:
                return x_new.round(6)
            x = x_new
        return None

    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("Error")
        msg.setText(message)
        msg.exec()
