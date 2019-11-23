# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'I:\python_base_Code\PyQt5学习\PyQt_Demo\resource\UI\register.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


# 注册界面实现
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(520, 350)
        Form.setMinimumSize(QtCore.QSize(520, 350))
        Form.setMaximumSize(QtCore.QSize(520, 350))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/login/QQ.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QWidget#Form{\n"
"    \n"
"    \n"
"    border-image: url(:/login/登录图片.png);\n"
"}")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 230, 150, 35))
        self.pushButton.setMinimumSize(QtCore.QSize(150, 35))
        self.pushButton.setMaximumSize(QtCore.QSize(150, 35))
        self.pushButton.setStyleSheet("background-color:rgb(244, 244, 244) ;\n"
"font: 75 9pt \"微软雅黑\";\n"
"border-radius:6px;\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/login/添加好友.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 310, 30, 30))
        self.pushButton_2.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_2.setStyleSheet("image: url(:/login/QQ.png);\n"
"background-color:transparent ;")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(470, 310, 30, 30))
        self.pushButton_3.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setStyleSheet("background-color:transparent ;\n"
"image: url(:/login/二维码.png);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.login_btn_2 = QtWidgets.QPushButton(Form)
        self.login_btn_2.setEnabled(True)
        self.login_btn_2.setGeometry(QtCore.QRect(140, 290, 230, 35))
        self.login_btn_2.setMinimumSize(QtCore.QSize(230, 35))
        self.login_btn_2.setMaximumSize(QtCore.QSize(230, 35))
        self.login_btn_2.setStyleSheet("QPushButton{\n"
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
        self.login_btn_2.setCheckable(False)
        self.login_btn_2.setObjectName("login_btn_2")

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.exit_register_pane)
        self.pushButton.clicked.connect(Form.open_register_link)
        self.login_btn_2.clicked.connect(Form.exit_register_pane)
        self.pushButton_3.clicked.connect(Form.show_qrcode_pane)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "添加账号"))
        self.pushButton.setText(_translate("Form", " 注册QQ账号"))
        self.login_btn_2.setText(_translate("Form", "登录"))
import rc.login_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
