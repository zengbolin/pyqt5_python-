# encoding:utf-8
import sys

from PyQt5.QtCore import Qt, pyqtSignal, QPropertyAnimation, QPoint, QAbstractAnimation, QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QApplication, QWidget
from resource.Ui_login import Ui_Form


# 登录面板实现类，也是第一窗口
class Login(QWidget, Ui_Form):
    # 定义点击登录信号、点击注册信号、点击二维码信号、点击设置信号
    login_signal = pyqtSignal(str, str)
    show_register_pane_signal = pyqtSignal()
    show_qrcode_signal = pyqtSignal()
    show_setup_pane_signal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super(Login, self).__init__(parent, *args, **kwargs)
        # 显示背景图，因为pyqt5设置问题
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

    # 是否登录
    def check_login(self):
        # 获取文本框内容
        account_text = self.name_line.currentText()
        password_text = self.password_line.text()
        # 检查文本框输入内容是否符合再去让按钮变亮
        if 6 <= len(account_text) <= 10 and len(password_text) > 8 and 100000 < int(account_text) < 100000000000:
            self.login_btn.setEnabled(True)
        else:
            self.login_btn.setEnabled(False)

    # 是否登录成功
    def checked_login(self):
        # 获取账号密码文本
        account_text = self.name_line.currentText()
        password_text = self.password_line.text()
        # 将内容返回给登录信号
        self.login_signal.emit(account_text, password_text)

    # 显示注册界面函数
    def show_register_pane(self):
        # print("121212")
        # 绑定显示注册界面信号
        self.show_register_pane_signal.emit()

    # 显示二维码界面
    def show_qrcode_pane(self):
        # 绑定显示二维码界面信号
        self.show_qrcode_signal.emit()

    # 实现记住密码复选框的点击
    def rember_pwd(self, checked):
        # print(checked)
        if not checked:
            self.antologin_checkbox.setChecked(False)

    # 实现自动登录的点击
    def auto_login(self, checked):
        # print(checked)
        if checked:
            self.rember_checkbox.setChecked(True)

    # 实现界面的动态效果，例如登录错误的窗口抖动动画
    def show_error_animation(self):
        animation = QPropertyAnimation(self)
        animation.setTargetObject(self.login_widget)
        animation.setPropertyName(b"pos")
        animation.setKeyValueAt(0, self.login_widget.pos())
        animation.setKeyValueAt(0.2, self.login_widget.pos() - QPoint(15, 0))
        animation.setKeyValueAt(0.5, self.login_widget.pos())
        animation.setKeyValueAt(0.7, self.login_widget.pos() - QPoint(-15, 0))
        animation.setKeyValueAt(1, self.login_widget.pos())
        animation.setDuration(200)
        animation.setLoopCount(5)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    # 显示设置界面
    def show_setup_pane(self):
        # 绑定显示设置界面的信号
        self.show_setup_pane_signal.emit()

    # 将忘记密码的链接绑定到指定qq忘记密码界面
    def show_findpwd_link(self):
        link = "https://aq.qq.com/v2/uv_aq/html/reset_pwd/pc_reset_pwd_input_account.html"
        QDesktopServices.openUrl(QUrl(link))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    login.login_signal.connect(lambda a, p: print(a, p))
    login.show()
    sys.exit(app.exec())
