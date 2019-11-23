# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'I:\python_base_Code\PyQt5学习\PyQt_Demo\resource\UI\login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


# 登录界面实现
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
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
        self.login_widget = QtWidgets.QWidget(Form)
        self.login_widget.setGeometry(QtCore.QRect(0, 190, 520, 160))
        self.login_widget.setMinimumSize(QtCore.QSize(520, 160))
        self.login_widget.setMaximumSize(QtCore.QSize(520, 160))
        self.login_widget.setObjectName("login_widget")
        self.pushButton_2 = QtWidgets.QPushButton(self.login_widget)
        self.pushButton_2.setGeometry(QtCore.QRect(479, 117, 30, 30))
        self.pushButton_2.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_2.setStyleSheet("background-color:transparent ;\n"
                                        "image: url(:/login/二维码.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.password_btn = QtWidgets.QPushButton(self.login_widget)
        self.password_btn.setGeometry(QtCore.QRect(390, 50, 93, 28))
        self.password_btn.setStyleSheet("\n"
                                        "background-color:transparent ;\n"
                                        "color: rgb(0, 170, 255);")
        self.password_btn.setFlat(True)
        self.password_btn.setObjectName("password_btn")
        self.login_btn = QtWidgets.QPushButton(self.login_widget)
        self.login_btn.setEnabled(False)
        self.login_btn.setGeometry(QtCore.QRect(159, 107, 230, 35))
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
                                     "QPushButton:disabled{\n"
                                     "    background-color:rgb(172, 172, 172);\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "    background-color:rgb(25, 225, 255);\n"
                                     "}\n"
                                     "")
        self.login_btn.setCheckable(False)
        self.login_btn.setObjectName("login_btn")
        self.head_widget = QtWidgets.QWidget(self.login_widget)
        self.head_widget.setEnabled(True)
        self.head_widget.setGeometry(QtCore.QRect(39, 21, 101, 101))
        self.head_widget.setStyleSheet("border-radius:16px;\n"
                                       "border-image: url(:/login/1.jpeg);")
        self.head_widget.setObjectName("head_widget")
        self.state_btn_2 = QtWidgets.QPushButton(self.head_widget)
        self.state_btn_2.setGeometry(QtCore.QRect(80, 80, 20, 20))
        self.state_btn_2.setMinimumSize(QtCore.QSize(20, 20))
        self.state_btn_2.setMaximumSize(QtCore.QSize(20, 20))
        self.state_btn_2.setStyleSheet("image: url(:/login/在线.png);\n"
                                       "image: url(:/login/在线.png);")
        self.state_btn_2.setText("")
        self.state_btn_2.setCheckable(True)
        self.state_btn_2.setChecked(False)
        self.state_btn_2.setObjectName("state_btn_2")
        self.antologin_checkbox = QtWidgets.QCheckBox(self.login_widget)
        self.antologin_checkbox.setGeometry(QtCore.QRect(303, 82, 87, 19))
        self.antologin_checkbox.setStyleSheet("font: 9pt \"微软雅黑\";\n"
                                              "color:rgb(191, 197, 203);")
        self.antologin_checkbox.setObjectName("antologin_checkbox")
        self.register_btn_2 = QtWidgets.QPushButton(self.login_widget)
        self.register_btn_2.setGeometry(QtCore.QRect(9, 117, 30, 30))
        self.register_btn_2.setMinimumSize(QtCore.QSize(30, 30))
        self.register_btn_2.setMaximumSize(QtCore.QSize(30, 30))
        self.register_btn_2.setStyleSheet("image: url(:/login/添加好友.png);\n"
                                          "background-color:transparent ;\n"
                                          "")
        self.register_btn_2.setText("")
        self.register_btn_2.setObjectName("register_btn_2")
        self.rember_checkbox = QtWidgets.QCheckBox(self.login_widget)
        self.rember_checkbox.setEnabled(True)
        self.rember_checkbox.setGeometry(QtCore.QRect(160, 82, 87, 19))
        self.rember_checkbox.setStyleSheet("font: 9pt \"微软雅黑\";\n"
                                           "color:rgb(191, 197, 203);")
        self.rember_checkbox.setObjectName("rember_checkbox")
        self.register_btn = QtWidgets.QPushButton(self.login_widget)
        self.register_btn.setGeometry(QtCore.QRect(390, 22, 93, 28))
        self.register_btn.setStyleSheet("background-color:transparent ;\n"
                                        "color: rgb(0, 170, 255);\n"
                                        "QPushButton {\n"
                                        "    color: rgb(0, 170, 255);\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    font-color:rgb(0, 0, 0);\n"
                                        "    color: rgb(0, 170, 255);\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    color: rgb(0, 170, 255);\n"
                                        "}")
        self.register_btn.setFlat(True)
        self.register_btn.setObjectName("register_btn")
        self.password_line = QtWidgets.QLineEdit(self.login_widget)
        self.password_line.setGeometry(QtCore.QRect(159, 47, 230, 30))
        self.password_line.setMinimumSize(QtCore.QSize(230, 30))
        self.password_line.setMaximumSize(QtCore.QSize(230, 30))
        self.password_line.setStyleSheet("QLineEdit{\n"
                                         "    font-size:16px;\n"
                                         "    border:none;\n"
                                         "    border-bottom:1px solid lightgray;\n"
                                         "    background-color:transparent;\n"
                                         "    font: 10pt \"黑体\";\n"
                                         "}\n"
                                         "QLineEdit:hover{\n"
                                         "    border-bottom:1px solid gray;\n"
                                         "}\n"
                                         "QLineEdit:focus{\n"
                                         "    border-bottom:1px solid rgb(18,183,245);\n"
                                         "}\n"
                                         "")
        self.password_line.setText("")
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line.setClearButtonEnabled(True)
        self.password_line.setObjectName("password_line")
        self.name_line = QtWidgets.QComboBox(self.login_widget)
        self.name_line.setGeometry(QtCore.QRect(160, 20, 230, 30))
        self.name_line.setMinimumSize(QtCore.QSize(230, 30))
        self.name_line.setMaximumSize(QtCore.QSize(230, 30))
        self.name_line.setStyleSheet("QComboBox{\n"
                                     "    font-size:20px;\n"
                                     "    border:none;\n"
                                     "    border-bottom:1px solid lightgray;\n"
                                     "    background-color:transparent;\n"
                                     "}\n"
                                     "QComboBox:hover{\n"
                                     "    border-bottom:1px solid gray;\n"
                                     "}\n"
                                     "QComboBox:focus{\n"
                                     "    border-bottom:1px solid rgb(18,183,245);\n"
                                     "}\n"
                                     "QComboBox::drop-down{\n"
                                     "    background-color:transparent;\n"
                                     "    width:40px;\n"
                                     "    height:30px;\n"
                                     "}\n"
                                     "QComboBox::down-arrow{\n"
                                     "    image: url(:/login/下拉.png);\n"
                                     "    width:60px;\n"
                                     "    height:20px;\n"
                                     "}\n"
                                     "QComboBox QAbstractItemView{\n"
                                     "    min-height:60px;\n"
                                     "}\n"
                                     "QComboBox QAbstractItemView:item{\n"
                                     "    color:lightblus;\n"
                                     "}")
        self.name_line.setEditable(True)
        self.name_line.setObjectName("name_line")
        self.name_line.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/login/file.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.name_line.addItem(icon1, "")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.pushButton.setStyleSheet("background-color:transparent ;\n"
                                      "border-image: url(:/login/下拉.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        self.name_line.editTextChanged['QString'].connect(Form.check_login)
        self.password_line.textChanged['QString'].connect(Form.check_login)
        self.rember_checkbox.clicked['bool'].connect(Form.rember_pwd)
        self.antologin_checkbox.clicked['bool'].connect(Form.auto_login)
        self.login_btn.clicked.connect(Form.checked_login)
        self.register_btn_2.clicked.connect(Form.show_register_pane)
        self.pushButton_2.clicked.connect(Form.show_qrcode_pane)
        self.pushButton.clicked.connect(Form.show_setup_pane)
        self.register_btn.clicked.connect(Form.show_register_pane)
        self.password_btn.clicked.connect(Form.show_findpwd_link)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Tim登录"))
        self.password_btn.setText(_translate("Form", "找回密码"))
        self.login_btn.setText(_translate("Form", "登录"))
        self.antologin_checkbox.setText(_translate("Form", "自动登录"))
        self.rember_checkbox.setText(_translate("Form", "记住密码"))
        self.register_btn.setText(_translate("Form", "注册账号"))
        self.password_line.setPlaceholderText(_translate("Form", "请输入你的密码"))
        self.name_line.setItemText(0, _translate("Form", "1234567890"))
        self.name_line.setItemText(1, _translate("Form", "2345678901"))


import rc.login_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
