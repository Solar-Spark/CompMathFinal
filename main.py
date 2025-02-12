import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt

from ui.main_menu import Ui_TaskSelect
from graph_method import GraphMethodApp
from root_finding_comparison import RootFindingComparisonApp
from jacobi_method import JacobiMethodApp


class TaskSelectApp(QMainWindow, Ui_TaskSelect):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_connections()
        self.active_window = None

    def setup_connections(self):
        self.graph_button.clicked.connect(self.graphical_method)
        self.root_button.clicked.connect(self.root_finding_comparison)
        self.jacobi_button.clicked.connect(self.jacobi_method)
        self.iterative_button.clicked.connect(self.iterative_matrix_inversion)
        self.linear_curve_button.clicked.connect(self.linear_curve_fitting)
        self.forward_interpolation_button.clicked.connect(self.newton_forward_interpolation)
        self.derivative_forward_button.clicked.connect(self.newton_forward_derivative)
        self.trapezoidal_button.clicked.connect(self.trapezoidal_rule)

    def graphical_method(self):
        self.active_window = GraphMethodApp()
        self.active_window.show()

    def root_finding_comparison(self):
        self.active_window = RootFindingComparisonApp()
        self.active_window.show()

    def jacobi_method(self):
        self.active_window = JacobiMethodApp()
        self.active_window.show()

    def iterative_matrix_inversion(self):
        print("Iterative Method for Matrix Inversion")

    def linear_curve_fitting(self):
        print("Linear Curve Fitting")

    def newton_forward_interpolation(self):
        print("Newton’s Forward Interpolation Formula ")

    def newton_forward_derivative(self):
        print("First Derivative Using Newton’s Forward Difference Formula")

    def trapezoidal_rule(self):
        print("Trapezoidal Rule")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaskSelectApp()
    window.show()
    sys.exit(app.exec())
