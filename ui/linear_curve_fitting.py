# Form implementation generated from reading ui file '.\linear_curve_fitting.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LinearCurveFitting(object):
    def setupUi(self, LinearCurveFitting):
        LinearCurveFitting.setObjectName("LinearCurveFitting")
        LinearCurveFitting.resize(750, 440)
        LinearCurveFitting.setMinimumSize(QtCore.QSize(750, 440))
        LinearCurveFitting.setMaximumSize(QtCore.QSize(750, 440))
        self.plot_area = QtWidgets.QLabel(parent=LinearCurveFitting)
        self.plot_area.setGeometry(QtCore.QRect(320, 20, 400, 400))
        self.plot_area.setMinimumSize(QtCore.QSize(400, 400))
        self.plot_area.setMaximumSize(QtCore.QSize(400, 400))
        self.plot_area.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.plot_area.setObjectName("plot_area")
        self.label_x = QtWidgets.QLabel(parent=LinearCurveFitting)
        self.label_x.setGeometry(QtCore.QRect(39, 106, 250, 19))
        self.label_x.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_x.setFont(font)
        self.label_x.setObjectName("label_x")
        self.label_y = QtWidgets.QLabel(parent=LinearCurveFitting)
        self.label_y.setGeometry(QtCore.QRect(39, 216, 250, 19))
        self.label_y.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_y.setFont(font)
        self.label_y.setObjectName("label_y")
        self.x_input = QtWidgets.QLineEdit(parent=LinearCurveFitting)
        self.x_input.setGeometry(QtCore.QRect(40, 156, 250, 30))
        self.x_input.setMinimumSize(QtCore.QSize(250, 30))
        self.x_input.setMaximumSize(QtCore.QSize(250, 30))
        self.x_input.setObjectName("x_input")
        self.plot_button = QtWidgets.QPushButton(parent=LinearCurveFitting)
        self.plot_button.setGeometry(QtCore.QRect(40, 306, 250, 30))
        self.plot_button.setMinimumSize(QtCore.QSize(250, 30))
        self.plot_button.setMaximumSize(QtCore.QSize(250, 30))
        self.plot_button.setObjectName("plot_button")
        self.y_input = QtWidgets.QLineEdit(parent=LinearCurveFitting)
        self.y_input.setGeometry(QtCore.QRect(40, 270, 250, 30))
        self.y_input.setMinimumSize(QtCore.QSize(250, 30))
        self.y_input.setMaximumSize(QtCore.QSize(250, 30))
        self.y_input.setObjectName("y_input")

        self.retranslateUi(LinearCurveFitting)
        QtCore.QMetaObject.connectSlotsByName(LinearCurveFitting)

    def retranslateUi(self, LinearCurveFitting):
        _translate = QtCore.QCoreApplication.translate
        LinearCurveFitting.setWindowTitle(_translate("LinearCurveFitting", "Linear Curve Fitting"))
        self.plot_area.setText(_translate("LinearCurveFitting", "Graph will be displayed here"))
        self.label_x.setText(_translate("LinearCurveFitting", "Enter X values (comma-separated):"))
        self.label_y.setText(_translate("LinearCurveFitting", "Enter Y values (comma-separated):"))
        self.plot_button.setText(_translate("LinearCurveFitting", "Plot Fit"))
