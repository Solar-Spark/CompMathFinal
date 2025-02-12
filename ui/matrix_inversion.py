# Form implementation generated from reading ui file '.\matrix_inversion.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MatrixInversion(object):
    def setupUi(self, MatrixInversion):
        MatrixInversion.setObjectName("MatrixInversion")
        MatrixInversion.resize(562, 497)
        self.layoutWidget = QtWidgets.QWidget(parent=MatrixInversion)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 541, 481))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.matrix_table = QtWidgets.QTableWidget(parent=self.layoutWidget)
        self.matrix_table.setObjectName("matrix_table")
        self.matrix_table.setColumnCount(0)
        self.matrix_table.setRowCount(0)
        self.verticalLayout.addWidget(self.matrix_table)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.inverse_matrix_table = QtWidgets.QTableWidget(parent=self.layoutWidget)
        self.inverse_matrix_table.setObjectName("inverse_matrix_table")
        self.inverse_matrix_table.setColumnCount(0)
        self.inverse_matrix_table.setRowCount(0)
        self.verticalLayout_2.addWidget(self.inverse_matrix_table)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.size_spinbox = QtWidgets.QSpinBox(parent=self.layoutWidget)
        self.size_spinbox.setMinimumSize(QtCore.QSize(140, 30))
        self.size_spinbox.setMaximumSize(QtCore.QSize(140, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.size_spinbox.setFont(font)
        self.size_spinbox.setObjectName("size_spinbox")
        self.horizontalLayout.addWidget(self.size_spinbox)
        self.solve_button = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.solve_button.setMinimumSize(QtCore.QSize(150, 30))
        self.solve_button.setMaximumSize(QtCore.QSize(150, 30))
        self.solve_button.setObjectName("solve_button")
        self.horizontalLayout.addWidget(self.solve_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(MatrixInversion)
        QtCore.QMetaObject.connectSlotsByName(MatrixInversion)

    def retranslateUi(self, MatrixInversion):
        _translate = QtCore.QCoreApplication.translate
        MatrixInversion.setWindowTitle(_translate("MatrixInversion", "Iterative Method for Matrix Inversion"))
        self.label.setText(_translate("MatrixInversion", "Matrix"))
        self.label_2.setText(_translate("MatrixInversion", "Inverse Matrix"))
        self.label_3.setText(_translate("MatrixInversion", "Matrix Size"))
        self.solve_button.setText(_translate("MatrixInversion", "Solve"))
