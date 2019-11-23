# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'I:\python_base_Code\PyQt5学习\PyQt_Demo\resource\UI\setup.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


# 代理设置界面设置
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
        self.widget_2.setGeometry(QtCore.QRect(1, 31, 520, 289))
        self.widget_2.setStyleSheet("background-color: rgb(235, 242, 249);\n"
                                    "font: 9pt \"黑体\";")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(30, 40, 72, 15))
        self.label.setStyleSheet("font: 10pt \"黑体\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 101, 16))
        self.label_4.setStyleSheet("font: 10pt \"黑体\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(50, 230, 72, 15))
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setGeometry(QtCore.QRect(90, 71, 111, 31))
        self.comboBox.setStyleSheet("font: 75 7pt \"微软雅黑\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(210, 80, 41, 21))
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(250, 70, 121, 31))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "    background-color:rgb(255, 255, 255);\n"
                                    "    border-radius:6px;\n"
                                    "}\n"
                                    "\n"
                                    "QLineEdit:disabled{\n"
                                    "    background-color:rgb(245, 248, 252);\n"
                                    "}")
        self.lineEdit.setObjectName("lineEdit")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setGeometry(QtCore.QRect(380, 80, 72, 15))
        self.label_7.setObjectName("label_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 70, 71, 31))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
                                      "    background-color:rgb(255, 255, 255);\n"
                                      "    border-radius:6px;\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:disabled{\n"
                                      "    background-color:rgb(245, 248, 252);\n"
                                      "}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 110, 113, 31))
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
                                      "    background-color:rgb(255, 255, 255);\n"
                                      "    border-radius:6px;\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:disabled{\n"
                                      "    background-color:rgb(245, 248, 252);\n"
                                      "}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setGeometry(QtCore.QRect(210, 120, 41, 20))
        self.label_8.setObjectName("label_8")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 110, 121, 31))
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
                                      "    background-color:rgb(255, 255, 255);\n"
                                      "    border-radius:6px;\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:disabled{\n"
                                      "    background-color:rgb(245, 248, 252);\n"
                                      "}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setGeometry(QtCore.QRect(390, 120, 21, 16))
        self.label_9.setObjectName("label_9")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setGeometry(QtCore.QRect(420, 110, 71, 31))
        self.lineEdit_5.setStyleSheet("QLineEdit{\n"
                                      "    background-color:rgb(255, 255, 255);\n"
                                      "    border-radius:6px;\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:disabled{\n"
                                      "    background-color:rgb(245, 248, 252);\n"
                                      "}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(420, 150, 71, 28))
        self.pushButton.setStyleSheet("background-color: rgb(240, 245, 250);\n"
                                      "font: 9pt \"黑体\";")
        self.pushButton.setObjectName("pushButton")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_2.setGeometry(QtCore.QRect(100, 221, 111, 31))
        self.comboBox_2.setStyleSheet("font: 75 7pt \"微软雅黑\";")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        self.label_10.setGeometry(QtCore.QRect(220, 230, 72, 15))
        self.label_10.setObjectName("label_10")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_3.setEnabled(False)
        self.comboBox_3.setGeometry(QtCore.QRect(270, 221, 101, 31))
        self.comboBox_3.setStyleSheet("QLineEdit{\n"
                                      "    background-color:rgb(85, 170, 255);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    border-radius:6px;\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:disabled{\n"
                                      "    background-color:rgb(245, 248, 252);\n"
                                      "}")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.setItemText(0, "")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_11 = QtWidgets.QLabel(self.widget_2)
        self.label_11.setGeometry(QtCore.QRect(380, 230, 72, 15))
        self.label_11.setObjectName("label_11")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setGeometry(QtCore.QRect(420, 220, 71, 31))
        self.lineEdit_6.setStyleSheet("QLineEdit{\n"
                                      "    background-color:rgb(255, 255, 255);\n"
                                      "    border-radius:6px;\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:disabled{\n"
                                      "    background-color:rgb(245, 248, 252);\n"
                                      "}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setGeometry(QtCore.QRect(1, 320, 520, 30))
        self.widget_3.setMinimumSize(QtCore.QSize(520, 30))
        self.widget_3.setMaximumSize(QtCore.QSize(520, 30))
        self.widget_3.setStyleSheet("background-color: rgb(205, 226, 242);")
        self.widget_3.setObjectName("widget_3")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget_3)
        self.buttonBox.setGeometry(QtCore.QRect(302, 0, 201, 28))
        self.buttonBox.setStyleSheet("color: rgb(85, 85, 85);\n"
                                     "background-color: rgb(242, 242, 242);\n"
                                     "font: 9pt \"黑体\";\n"
                                     "")
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Form)
        self.buttonBox.rejected.connect(Form.show_menu)
        self.buttonBox.accepted.connect(Form.show_menu)
        self.lineEdit.textChanged['QString'].connect(Form.enable_test)
        self.lineEdit_2.textChanged['QString'].connect(Form.enable_test)
        self.comboBox.activated['QString'].connect(Form.enable_test)
        self.comboBox_2.activated['QString'].connect(Form.enable_pane)
        self.comboBox_3.activated['QString'].connect(Form.enable_pane)
        self.lineEdit_6.textChanged['QString'].connect(Form.enable_pane)
        self.lineEdit_3.textChanged['QString'].connect(Form.enable_test)
        self.lineEdit_4.textChanged['QString'].connect(Form.enable_test)
        self.lineEdit_5.textChanged['QString'].connect(Form.enable_test)
        self.pushButton.clicked.connect(Form.enable_test)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "设置"))
        self.label.setText(_translate("Form", "网络设置"))
        self.label_2.setText(_translate("Form", " 类型："))
        self.label_3.setText(_translate("Form", "用户名："))
        self.label_4.setText(_translate("Form", "登录服务器"))
        self.label_5.setText(_translate("Form", "类型:"))
        self.comboBox.setItemText(0, _translate("Form", "不使用代理"))
        self.comboBox.setItemText(1, _translate("Form", "HTTP代理"))
        self.comboBox.setItemText(2, _translate("Form", "SOCKS5代理"))
        self.comboBox.setItemText(3, _translate("Form", "使用浏览器设置"))
        self.label_6.setText(_translate("Form", "地址:"))
        self.label_7.setText(_translate("Form", "端口："))
        self.label_8.setText(_translate("Form", "密码:"))
        self.label_9.setText(_translate("Form", "域:"))
        self.pushButton.setText(_translate("Form", "测试"))
        self.comboBox_2.setItemText(0, _translate("Form", "不使用高级选项"))
        self.comboBox_2.setItemText(1, _translate("Form", "UDP类型"))
        self.comboBox_2.setItemText(2, _translate("Form", "TCp类型"))
        self.label_10.setText(_translate("Form", "地址:"))
        self.comboBox_3.setItemText(1, _translate("Form", "183.60.48.174"))
        self.comboBox_3.setItemText(2, _translate("Form", "sz.tencent.com"))
        self.comboBox_3.setItemText(3, _translate("Form", "sz2.tencent.com"))
        self.comboBox_3.setItemText(4, _translate("Form", "sz3.tencent.com"))
        self.comboBox_3.setItemText(5, _translate("Form", "sz4.tencent.com"))
        self.comboBox_3.setItemText(6, _translate("Form", "sz5.tencent.com"))
        self.label_11.setText(_translate("Form", "端口:"))


import rc.login_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
