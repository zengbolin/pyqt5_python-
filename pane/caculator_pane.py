# encoding:utf-8
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from resource.Ui_caculator import Ui_MainWindow

from tools.Caculator import Caculators


# 计算器面板类实现
class Caculator(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None, *args, **kwargs):
        super(Caculator, self).__init__(parent, *args, **kwargs)
        # 显示头图，可有可无
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        # 定义显示文本的信号以及连接函数
        self.caculators = Caculators()
        self.caculators.show_content.connect(self.show_content)

    # 获取按键
    def get_key(self, title, role):
        self.caculators.parse_key_model({"title": title, "role": role})

    # 显示内容到文本框
    def show_content(self, content):
        self.lineEdit.setText(content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    caculator_pane = Caculator()
    caculator_pane.show()
    sys.exit(app.exec())
