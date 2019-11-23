# encoding:utf-8
import sys

from PyQt5.QtCore import Qt, pyqtSignal, QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QApplication, QWidget
from resource.Ui_register import Ui_Form


# 注册界面实现类
class Register(QWidget, Ui_Form):
    # 定义退出信号和显示二维码信号
    exit_signal = pyqtSignal()
    show_qrcode_signal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super(Register, self).__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

    # 退出按钮实现
    def exit_register_pane(self):
        # 绑定退出信号
        self.exit_signal.emit()

    # 点击注册QQ按钮，跳转qq注册界面
    def open_register_link(self):
        link = "http://zc.qq.com/"
        QDesktopServices.openUrl(QUrl(link))

    # 二维码按钮实现
    def show_qrcode_pane(self):
        # 绑定二维码信号
        self.show_qrcode_signal.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    register = Register()
    register.show()
    sys.exit(app.exec())
