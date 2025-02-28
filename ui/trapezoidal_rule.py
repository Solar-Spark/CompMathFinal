# Form implementation generated from reading ui file '.\trapezoidal_rule.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TrapezoidalRule(object):
    def setupUi(self, TrapezoidalRule):
        TrapezoidalRule.setObjectName("TrapezoidalRule")
        TrapezoidalRule.resize(310, 410)
        TrapezoidalRule.setMinimumSize(QtCore.QSize(310, 410))
        TrapezoidalRule.setMaximumSize(QtCore.QSize(310, 410))
        self.widget = QtWidgets.QWidget(parent=TrapezoidalRule)
        self.widget.setGeometry(QtCore.QRect(10, 20, 291, 381))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setMinimumSize(QtCore.QSize(240, 19))
        self.label.setMaximumSize(QtCore.QSize(240, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.function_input = QtWidgets.QLineEdit(parent=self.widget)
        self.function_input.setMinimumSize(QtCore.QSize(0, 30))
        self.function_input.setMaximumSize(QtCore.QSize(16777215, 30))
        self.function_input.setObjectName("function_input")
        self.verticalLayout.addWidget(self.function_input)
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(240, 20))
        self.label_2.setMaximumSize(QtCore.QSize(240, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(162, 25))
        self.label_3.setMaximumSize(QtCore.QSize(162, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lower_limit_input = QtWidgets.QLineEdit(parent=self.widget)
        self.lower_limit_input.setMinimumSize(QtCore.QSize(0, 30))
        self.lower_limit_input.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lower_limit_input.setObjectName("lower_limit_input")
        self.horizontalLayout.addWidget(self.lower_limit_input)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(162, 25))
        self.label_4.setMaximumSize(QtCore.QSize(162, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.upper_limit_input = QtWidgets.QLineEdit(parent=self.widget)
        self.upper_limit_input.setMinimumSize(QtCore.QSize(0, 30))
        self.upper_limit_input.setMaximumSize(QtCore.QSize(16777215, 30))
        self.upper_limit_input.setObjectName("upper_limit_input")
        self.horizontalLayout_2.addWidget(self.upper_limit_input)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        self.label_5.setMinimumSize(QtCore.QSize(200, 25))
        self.label_5.setMaximumSize(QtCore.QSize(162, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.subintervals_number_input = QtWidgets.QLineEdit(parent=self.widget)
        self.subintervals_number_input.setMinimumSize(QtCore.QSize(0, 30))
        self.subintervals_number_input.setMaximumSize(QtCore.QSize(16777215, 30))
        self.subintervals_number_input.setObjectName("subintervals_number_input")
        self.horizontalLayout_7.addWidget(self.subintervals_number_input)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.calculate_button = QtWidgets.QPushButton(parent=self.widget)
        self.calculate_button.setMinimumSize(QtCore.QSize(0, 30))
        self.calculate_button.setObjectName("calculate_button")
        self.verticalLayout.addWidget(self.calculate_button)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_14 = QtWidgets.QLabel(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QtCore.QSize(160, 30))
        self.label_14.setMaximumSize(QtCore.QSize(160, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_10.addWidget(self.label_14)
        self.exact_value_label = QtWidgets.QLabel(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exact_value_label.sizePolicy().hasHeightForWidth())
        self.exact_value_label.setSizePolicy(sizePolicy)
        self.exact_value_label.setMinimumSize(QtCore.QSize(117, 30))
        self.exact_value_label.setMaximumSize(QtCore.QSize(117, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exact_value_label.setFont(font)
        self.exact_value_label.setText("")
        self.exact_value_label.setObjectName("exact_value_label")
        self.horizontalLayout_10.addWidget(self.exact_value_label)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_12 = QtWidgets.QLabel(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(160, 30))
        self.label_12.setMaximumSize(QtCore.QSize(160, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.calculated_value_label = QtWidgets.QLabel(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calculated_value_label.sizePolicy().hasHeightForWidth())
        self.calculated_value_label.setSizePolicy(sizePolicy)
        self.calculated_value_label.setMinimumSize(QtCore.QSize(117, 30))
        self.calculated_value_label.setMaximumSize(QtCore.QSize(117, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calculated_value_label.setFont(font)
        self.calculated_value_label.setText("")
        self.calculated_value_label.setObjectName("calculated_value_label")
        self.horizontalLayout_6.addWidget(self.calculated_value_label)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_13 = QtWidgets.QLabel(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QtCore.QSize(160, 30))
        self.label_13.setMaximumSize(QtCore.QSize(160, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_8.addWidget(self.label_13)
        self.error_label = QtWidgets.QLabel(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error_label.sizePolicy().hasHeightForWidth())
        self.error_label.setSizePolicy(sizePolicy)
        self.error_label.setMinimumSize(QtCore.QSize(117, 30))
        self.error_label.setMaximumSize(QtCore.QSize(117, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.error_label.setFont(font)
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        self.horizontalLayout_8.addWidget(self.error_label)
        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.retranslateUi(TrapezoidalRule)
        QtCore.QMetaObject.connectSlotsByName(TrapezoidalRule)

    def retranslateUi(self, TrapezoidalRule):
        _translate = QtCore.QCoreApplication.translate
        TrapezoidalRule.setWindowTitle(_translate("TrapezoidalRule", "Trapezoidal Rule"))
        self.label.setText(_translate("TrapezoidalRule", "Enter your function:"))
        self.label_2.setText(_translate("TrapezoidalRule", "Enter Integral Limits:"))
        self.label_3.setText(_translate("TrapezoidalRule", "Lower limit:"))
        self.label_4.setText(_translate("TrapezoidalRule", "Upper limit:"))
        self.label_5.setText(_translate("TrapezoidalRule", "Enter subintervals number"))
        self.calculate_button.setText(_translate("TrapezoidalRule", "Calculate Integral"))
        self.label_14.setText(_translate("TrapezoidalRule", "Exact Integral: "))
        self.label_12.setText(_translate("TrapezoidalRule", "Calculated Integral: "))
        self.label_13.setText(_translate("TrapezoidalRule", "Absolute Error:"))
