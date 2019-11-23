- [功能](#功能)
- [项目说明](#项目说明)
- [输出](#输出)
- [运行环境](#运行环境)
- [使用说明](#使用说明)
    - [下载脚本](#1下载脚本)
    - [安装依赖](#2安装依赖)
    - [运行脚本](#5运行脚本)
- [项目作业bug说明](#bug说明)

## 功能

**功能**: 代码实现的效果为登录注册界面，登录成功还有计算器界面。可以当成pyqt5的一个小项目。

## 项目说明

**说明信息**<br>

使用pyqt5进行实验的设计，**为啥不使用tkinter来开发python图形界面呢？**，对于这个问题，首先tkinter是python自带的模块，但是其功能是真的少，而且设置界面非常复杂，几乎全在代码中度过。此时就可以使用第三方优秀模块**pyqt5**，而且pyqt5还有图形化设置界面，非常方便用户设计图形界面，而且还可以把ui文件转换python文件。<br>

此项目仅仅只是pyqt5的一个小小实践Demo。项目中的登录时有效的，只设置了一个账号，所以这个账号为：**账号: 1234567890      密码: 123456789**。去尝试登录计算器吧，哈哈哈。

## 输出

**登录界面信息**<br>

**1**. 登录第一窗口

![登录第一窗口](https://i.loli.net/2019/11/23/RTPEBgdp3sQkDyW.png)

**2**. 密码输入情况

![密码输入情况](https://i.loli.net/2019/11/23/cnDmHCJsMzqXftx.png)

**注册界面**<br>

![注册界面](https://i.loli.net/2019/11/23/Y63pSuVaI7cdUJe.png)

**代理设置界面**<br>

**1**. 代理设置第一界面

![代理设置界面](https://i.loli.net/2019/11/23/7Aj5XCStz2TGuaN.png)

**2**. 当复选框有内容时界面

![](https://i.loli.net/2019/11/23/zITEg1lJxHmtMSp.png)

**二维码界面**<br>

**1**. 初始化界面

![](https://i.loli.net/2019/11/23/pmYR8vBA9zXLKDa.png)

**2**. 点击二维码状态

![](https://i.loli.net/2019/11/23/cDgpvE9qGOxuhRn.png)

**计算器界面**

**1**. 初始化界面

![](https://i.loli.net/2019/11/23/X37TvaI259wNDPQ.png)

**2**. 计算器界面

![](https://i.loli.net/2019/11/23/ZWMy9dnSgKAoP1f.png)

## 运行环境

- 开发语言：python3
- 系统： Windows/Linux

## 使用说明

### 1.下载脚本

```bash
$ git clone https://github.com/zengbolin/pyqt5_python-.git
```

运行上述命令，将本项目下载到当前目录，如果下载成功当前目录会出现一个名为"pyqt5_python-"的文件夹；

### 2.安装依赖

```bash
# 进入requirements文件夹，用cmd安装
$ pip install -r requirements.txt
```

### 3.运行脚本

大家可以根据自己的运行环境选择运行方式，Linux或widows可以通过

```bash
$ python main.py
```

运行;

## 项目作业bug说明

**1**. 计算器输入0.的时候<br>

![](https://i.loli.net/2019/11/23/qr2ZQ97dLlentvi.png)


**2**. 计算超过两位小数的算式<br>

![](https://i.loli.net/2019/11/23/WdYLZfKVP6SOric.png)
