# encoding:utf-8
import sys
import time
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QAbstractAnimation, QPoint
from PyQt5.QtWidgets import QApplication
from pane.login_pane import Login
from pane.register_pane import Register
from pane.QR_code_pane import QR_code
from pane.setup_pane import Setup
from pane.caculator_pane import Caculator


# 打开另外界面的实现动画效果
def splash_open_init(pane):
    animation = QPropertyAnimation(pane)
    animation.setTargetObject(pane)
    animation.setPropertyName(b"pos")
    animation.setStartValue(pane.pos())
    animation.setEndValue(QPoint(0, 0))
    animation.setEasingCurve(QEasingCurve.OutBounce)
    animation.setDuration(500)
    animation.start(QAbstractAnimation.DeleteWhenStopped)


# 退出当前界面的实现动画效果
def splash_exit_init(pane, pane1):
    animation = QPropertyAnimation(pane)
    animation.setTargetObject(pane)
    animation.setPropertyName(b"pos")
    animation.setEndValue(QPoint(0, pane1.width()))
    animation.setStartValue(QPoint(0, 0))
    animation.setEasingCurve(QEasingCurve.InBounce)
    animation.setDuration(500)
    animation.start(QAbstractAnimation.DeleteWhenStopped)


# 显示二维码面板
def show_qrcode_pane():
    splash_open_init(qrcode_pane)


# 显示注册面板
def show_register_pane():
    splash_open_init(register_pane)


# 显示退出面板
def exit_signal_func():
    splash_exit_init(register_pane, login_pane)


# 显示退出二维码面板
def exit_qrcode_pane():
    splash_exit_init(qrcode_pane, login_pane)


# 检查登录是否成功，账号为：1234567890 密码为123456789
def check_login(account, password):
    if account == "1234567890" and password == '123456789':
        time.sleep(1)
        # 登陆成功显示计算器界面，退出登录界面
        caculator_pane.show()
        login_pane.hide()
    else:
        # 显示错误动画效果
        login_pane.show_error_animation()


# 显示设置面板
def show_setup_pane():
    splash_open_init(setup_pane)


# 退出设置面板
def exit_setup_pane():
    splash_exit_init(setup_pane, login_pane)


# 主函数入口，主要实现多个界面的联动
# 作为一个中转站，可以防止耦合现象
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 登录界面实现
    login_pane = Login()

    # 注册界面的实现
    register_pane = Register(login_pane)
    register_pane.move(0, login_pane.height())
    register_pane.show()

    # 二维码界面实现
    qrcode_pane = QR_code(login_pane)
    qrcode_pane.move(0, login_pane.height())
    qrcode_pane.show()

    # 代理设置界面实现
    setup_pane = Setup(login_pane)
    setup_pane.move(0, login_pane.height())
    setup_pane.show()

    # 计算器界面实现
    caculator_pane = Caculator()

    # 登录界面各个按钮的槽函数连接
    login_pane.login_signal.connect(check_login)
    login_pane.show_register_pane_signal.connect(show_register_pane)
    login_pane.show_qrcode_signal.connect(show_qrcode_pane)
    login_pane.show_setup_pane_signal.connect(show_setup_pane)

    # 注册界面各个按钮的槽函数连接
    register_pane.exit_signal.connect(exit_signal_func)
    register_pane.show_qrcode_signal.connect(show_qrcode_pane)

    # 二维码界面各个按钮的槽函数连接
    qrcode_pane.exit_signal.connect(exit_qrcode_pane)

    # 代理设置界面各个按钮的槽函数连接
    setup_pane.exit_signal.connect(exit_setup_pane)

    login_pane.show()
    sys.exit(app.exec())
