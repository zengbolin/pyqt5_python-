# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'I:\python_base_Code\PyQt5学习\PyQt_Demo\resource\UI\QR_code.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


# 二维码界面实现
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(520, 350)
        Form.setMinimumSize(QtCore.QSize(520, 350))
        Form.setMaximumSize(QtCore.QSize(520, 350))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/login/QQ.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(1, 1, 520, 30))
        self.widget.setMinimumSize(QtCore.QSize(520, 30))
        self.widget.setMaximumSize(QtCore.QSize(520, 30))
        self.widget.setStyleSheet("image: url(:/login/版图.png);")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(1, 31, 520, 319))
        self.widget_2.setStyleSheet("background-color: rgb(235, 242, 249);")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(140, 60, 221, 31))
        self.label.setStyleSheet("font: 11pt \"黑体\";\n"
                                 "")
        self.label.setObjectName("label")
        self.login_btn = QtWidgets.QPushButton(self.widget_2)
        self.login_btn.setEnabled(True)
        self.login_btn.setGeometry(QtCore.QRect(140, 260, 230, 35))
        self.login_btn.setMinimumSize(QtCore.QSize(230, 35))
        self.login_btn.setMaximumSize(QtCore.QSize(230, 35))
        self.login_btn.setStyleSheet("QPushButton{\n"
                                     "    background-color:rgb(85, 170, 255);\n"
                                     "    font: 10pt \"微软雅黑\";\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "    border-radius:6px;\n"
                                     "}\n"
                                     "QPushButton:pressed{\n"
                                     "    background-color:rgb(0, 170, 255);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover{\n"
                                     "    background-color:rgb(25, 225, 255);\n"
                                     "}\n"
                                     "")
        self.login_btn.setCheckable(False)
        self.login_btn.setObjectName("login_btn")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(110, 120, 121, 121))
        self.pushButton.setStyleSheet("border-image: url(:/login/QR_code.jpg);")
        self.pushButton.setText("")
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 120, 121, 121))
        self.pushButton_2.setStyleSheet("border-image: url(:/login/scan.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label.raise_()
        self.login_btn.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Form)
        self.pushButton.clicked['bool'].connect(Form.show_hide_menu)
        self.login_btn.clicked.connect(Form.show_menu)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "扫描二维码"))
        self.label.setText(_translate("Form", "用微信扫描二维码添加好友"))
        self.login_btn.setText(_translate("Form", "返回"))


import rc.login_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
