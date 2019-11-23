# encoding:utf-8
import sys
from PyQt5.QtCore import Qt, QSequentialAnimationGroup, QPropertyAnimation, QEasingCurve, QAbstractAnimation, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget
from resource.Ui_QR_code import Ui_Form


# 二维码界面实现类
class QR_code(QWidget, Ui_Form):
    # 定义退出此界面的信号
    exit_signal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super(QR_code, self).__init__(parent, *args, **kwargs)
        self.setupUi(self)

        self.animation_target = [self.pushButton_2]
        self.animation_target_pos = [target.pos() for target in self.animation_target]

    # 实现点击二维码的收缩动画
    def show_hide_menu(self, checked):
        animation_group = QSequentialAnimationGroup(self)
        for idx, target in enumerate(self.animation_target):
            animation = QPropertyAnimation()
            animation.setTargetObject(target)
            animation.setPropertyName(b"pos")
            animation.setEndValue(self.pushButton.pos())
            animation.setStartValue(self.animation_target_pos[idx])
            animation.setDuration(200)
            animation.setEasingCurve(QEasingCurve.InOutBounce)
            animation_group.addAnimation(animation)

        animation_group.setDirection(not checked)
        animation_group.start(QAbstractAnimation.DeleteWhenStopped)

    # 退出按钮实现
    def show_menu(self):
        # 绑定退出信号
        self.exit_signal.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    qR = QR_code()
    qR.show()
    sys.exit(app.exec())
