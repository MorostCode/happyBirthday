# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget
from happyBirthdayUI import Ui_MainWindow
from staticImg import iconCake
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
import selfQtools
import sys

# 口令密码
# lsl生日快乐
titlePassword = ""


class MainWindow(Ui_MainWindow, QMainWindow):
    # 初始化
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)  # 加载Ui
        # loadUi("happyBirthday.ui", self)  # 加载Ui文件
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SplashScreen)  # 隐藏主窗口边界
        self.setAttribute(Qt.WA_TranslucentBackground)  # 隐藏背景（透明化

        self.setFixedSize(841, 911)  # 设定窗口尺寸(固定尺寸)
        screenSize = QDesktopWidget().screenGeometry()  # 获取屏幕尺寸
        selfSize = self.geometry()  # 获取程序窗口尺寸
        newLeft = int((screenSize.width() - selfSize.width()) / 2)
        newTop = int((screenSize.height() - selfSize.height()) / 2)
        self.move(newLeft, newTop)  # 移动到居中位置
        self.pushButton.setIcon(QIcon(selfQtools.base642pixmap(iconCake)))  # 设置按钮图标

        # # 获取图片数据并缩放成合适大小
        # pixmap = selfQtools.base642pixmap(imgToSet)
        # selfQtools.pixmap2label(pixmap, self.image)

        # 绑定按钮
        self.pushButton.clicked.connect(self.if_close)

    # 只有输对口令才可以关闭程序
    def if_close(self):
        if self.lineEdit.text() == titlePassword:
            sys.exit()


if __name__ == '__main__':
    # 创建QApplication类的实例
    app = QApplication(sys.argv)
    # 实例化一个窗口类
    main_window = MainWindow()
    # 显示窗口
    main_window.show()
    # 进入程序主循环 通过exit函数确保主循环安全结束
    sys.exit(app.exec_())
