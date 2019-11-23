# encoding:utf-8
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QPushButton


# 计算器按键类
class Caculator_btn(QPushButton):
    # 定义一个按键按下去的信号
    key_pressed = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super(Caculator_btn, self).__init__(parent, *args, **kwargs)

    # 重写鼠标按下事件
    def mousePressEvent(self, *args, **kwargs):
        super(Caculator_btn, self).mousePressEvent(*args, **kwargs)
        self.key_pressed.emit(self.text(), self.property("role"))

    # 重写改变窗口大小的事件
    def resizeEvent(self, *args, **kwargs):
        # 设置按键的样式和颜色，以及部分事件的按键改变样式
        self.setStyleSheet("""
                    QPushButton[bg='gray']{
                        color : white;
                        background-color :rgb(88, 88, 88);
                    }
                    QPushButton[bg='gray']:hover{
                        background-color:rgb(150, 150, 150);
                    }
                    QPushButton[bg='orange'],QPushButton[bg='equal']{
                        color : white;
                        background-color :rgb(207, 138, 0);
                    }
                    QPushButton[bg='orange']:hover,QPushButton[bg='equal']:hover{
                        background-color :rgb(238, 159, 0);
                    }
                    QPushButton[bg='orange']:checked{
                        color : rgb(207, 138, 0);
                        background-color :white;
                    }
                    QPushButton[bg='lightgray']{
                        color : black;
                        background-color :rgb(200, 200, 200);
                    }
                    QPushButton[bg='lightgray']:hover{
                        background-color :rgb(230, 230, 230);
                    }
                """ + """
                    QPushButton[bg]{
                        font-size:28px;
                        border-radius:%dpx;
                        min-width:50px;
                        min-height:50px;
                    }
                """ % (min(self.height(), self.width()) * 0.5))
