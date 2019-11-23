# encoding:utf-8
import sys

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget
from resource.Ui_setup import Ui_Form

# 代理设置实现类
class Setup(QWidget, Ui_Form):
    # 退出信号
    exit_signal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super(Setup, self).__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
    # 显示第一界面
    def show_menu(self):
        # 绑定退出信号
        self.exit_signal.emit()
    # 实现逻辑，当第一个下拉框有内容时，才让其他文本框可以编辑
    def enable_test(self):
        if self.comboBox.currentIndex():
            self.lineEdit.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
            self.lineEdit_4.setEnabled(True)
            self.lineEdit_5.setEnabled(True)
            # 实现按钮逻辑
            if len(self.lineEdit.text()) > 0 and len(self.lineEdit_2.text()) > 0:
                self.pushButton.setEnabled(True)
            else:
                self.pushButton.setEnabled(False)
        else:
            self.lineEdit.setEnabled(False)
            self.lineEdit_2.setEnabled(False)
            self.lineEdit_3.setEnabled(False)
            self.lineEdit_4.setEnabled(False)
            self.lineEdit_5.setEnabled(False)
    # 同上
    def enable_pane(self):
        if self.comboBox_2.currentIndex():
            self.comboBox_3.setEnabled(True)
            # self.comboBox_3.setCurrentIndex(1)
            self.lineEdit_6.setPlaceholderText("8080")
            self.lineEdit_6.setEnabled(True)
        else:
            self.comboBox_3.setEnabled(False)
            self.lineEdit_6.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    setup_pane = Setup()
    setup_pane.show()
    sys.exit(app.exec())
