# encoding:utf-8
from PyQt5.QtCore import QObject, pyqtSignal


# 计算器逻辑实现
class Caculators(QObject):
    # 定义显示文本信号
    show_content = pyqtSignal(str)

    def __init__(self):
        super(Caculators, self).__init__()

        # 数字键位 num 运算符 opartor
        self.key_models = []

    def parse_key_model(self, key_model):

        # AC键的功能实现
        if key_model["role"] == 'clear':
            print("清空所有内容")
            self.key_models = []
            # 文本显示初始状态为 0
            self.show_content.emit('0')
            return

        # =号的功能实现
        if key_model['role'] == 'caculater':
            print("计算所有内容")
            # 使用参数接受运算结果
            result = self.caculate()
            # 文本显示暂时的结果
            self.show_content.emit(str(result))
            return

        # 数字键和运算符
        # 开始状态为长度为0的时刻，处理用户一开始输入.的操作
        if len(self.key_models) == 0:
            if key_model['role'] == 'num':
                if key_model['title'] == '.':
                    key_model['title'] = '0.'
                # 序列拼接
                self.key_models.append(key_model)
                # 文本显示 0.
                self.show_content.emit(self.key_models[-1]['title'])
            return

        # 处理正负号和百分号
        if key_model['title'] in ('%', '+/-'):
            # 若符号前面不为数字，就当作用户输入问题，不处理
            if self.key_models[-1]['role'] != 'num':
                return
            else:
                # 当用户输入%的逻辑处理
                if key_model['title'] == '%':
                    # * 0.01
                    self.key_models[-1]['title'] = str(float(self.key_models[-1]['title']) / 100)
                # 当用户输入负号的逻辑处理
                elif key_model['title'] == '-':
                    self.key_models[-1]['title'] = str(float(self.key_models[-1]['title']) * (-1))
                # 文本显示内容5% 就显示为 0.05
                self.show_content.emit(self.key_models[-1]['title'])
            return

        # 合并数字和运算符
        # 先判断前一个字符和后一个字符的类型是否一样
        if key_model['role'] == self.key_models[-1]['role']:
            # 当前一个输入为数字，后一个也为数字的逻辑
            if key_model['role'] == 'num':
                # 当前面输入有小数点，后面再输入小数点的逻辑处理
                if key_model['title'] == '.' and self.key_models[-1]['title'].__contains__('.'):
                    return
                # 当0和0的拼接逻辑
                if self.key_models[-1]['title'] != '0':
                    # 当第一个字符不为0
                    self.key_models[-1]['title'] += key_model['title']
                else:
                    self.key_models[-1]['title'] = key_model['title']
                # 展示最终拼接结果
                self.show_content.emit(self.key_models[-1]['title'])
            else:
                # 两个类型一样，但是只有一个为num类型
                self.key_models[-1]['title'] = key_model['title']
                # 展示显示结果
                self.show_content.emit(str(self.caculate()))
        # 前后输入的类型不一样
        else:
            # 当有 . % +/- 等直接返回
            if key_model['title'] in (".", "%", "+/-"):
                return
            # 当为数字键时，直接在文本框显示
            if key_model['role'] == 'num':
                # 显示数字键
                self.show_content.emit(key_model['title'])
            else:
                # 显示计算结果 为=
                self.show_content.emit(str(self.caculate()))
            # 增加运算表达式
            self.key_models.append(key_model)

    def caculate(self):
        # 判断表达式是否成立
        if len(self.key_models) > 0 and self.key_models[-1]['role'] == 'opartor':
            # 去掉等号
            self.key_models.pop(-1)
        expression = ""
        # 拼接等式
        for model in self.key_models:
            expression += model['title']

        # 计算表达式
        result = eval(expression)
        # print(result)
        return result
