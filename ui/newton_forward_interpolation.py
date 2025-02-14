# Form implementation generated from reading ui file 'newton_forward_interpolation.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_NewtonInterpolation(object):
    def setupUi(self, NewtonInterpolation):
        NewtonInterpolation.setObjectName("NewtonInterpolation")
        NewtonInterpolation.resize(190, 200)
        self.widget = QtWidgets.QWidget(parent=NewtonInterpolation)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_x = QtWidgets.QLabel(parent=self.widget)
        self.label_x.setObjectName("label_x")
        self.verticalLayout.addWidget(self.label_x)
        self.x_input = QtWidgets.QLineEdit(parent=self.widget)
        self.x_input.setObjectName("x_input")
        self.verticalLayout.addWidget(self.x_input)
        self.label_y = QtWidgets.QLabel(parent=self.widget)
        self.label_y.setObjectName("label_y")
        self.verticalLayout.addWidget(self.label_y)
        self.y_input = QtWidgets.QLineEdit(parent=self.widget)
        self.y_input.setObjectName("y_input")
        self.verticalLayout.addWidget(self.y_input)
        self.label_interp = QtWidgets.QLabel(parent=self.widget)
        self.label_interp.setObjectName("label_interp")
        self.verticalLayout.addWidget(self.label_interp)
        self.interp_input = QtWidgets.QLineEdit(parent=self.widget)
        self.interp_input.setObjectName("interp_input")
        self.verticalLayout.addWidget(self.interp_input)
        self.compute_button = QtWidgets.QPushButton(parent=self.widget)
        self.compute_button.setObjectName("compute_button")
        self.verticalLayout.addWidget(self.compute_button)
        self.result_label = QtWidgets.QLabel(parent=self.widget)
        self.result_label.setObjectName("result_label")
        self.verticalLayout.addWidget(self.result_label)

        self.retranslateUi(NewtonInterpolation)
        QtCore.QMetaObject.connectSlotsByName(NewtonInterpolation)

    def retranslateUi(self, NewtonInterpolation):
        _translate = QtCore.QCoreApplication.translate
        NewtonInterpolation.setWindowTitle(_translate("NewtonInterpolation", "Newton\'s Forward Interpolation"))
        self.label_x.setText(_translate("NewtonInterpolation", "Enter X values (comma-separated):"))
        self.label_y.setText(_translate("NewtonInterpolation", "Enter Y values (comma-separated):"))
        self.label_interp.setText(_translate("NewtonInterpolation", "Enter X value to interpolate:"))
        self.compute_button.setText(_translate("NewtonInterpolation", "Compute Interpolation"))
        self.result_label.setText(_translate("NewtonInterpolation", "Result will be displayed here"))
