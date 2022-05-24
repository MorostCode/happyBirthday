# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget
from happyBirthdayUI import Ui_MainWindow
from PyQt5.QtGui import QIcon, QPixmap
from img import imglsl, cakeIcon
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
import base64
import sys


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

        image = get_icon(imglsl)
        image = image.scaledToWidth(521)
        image = image.scaledToHeight(723)
        self.image.setPixmap(image)

        self.pushButton.clicked.connect(self.if_close)
        self.pushButton.setIcon(QIcon(get_icon(cakeIcon)))

    def if_close(self):
        if self.lineEdit.text() == "lsl生日快乐":
            sys.exit()


# 图标bytes转成pixmap
def get_icon(icon):
    icon_img = base64.b64decode(icon)  # 解码
    icon_pixmap = QPixmap()  # 新建QPixmap对象
    icon_pixmap.loadFromData(icon_img)  # 往QPixmap中写入数据
    return icon_pixmap


if __name__ == '__main__':
    # 创建QApplication类的实例
    app = QApplication(sys.argv)
    # 实例化一个窗口类
    main_window = MainWindow()
    # 显示窗口
    main_window.show()
    # 进入程序主循环 通过exit函数确保主循环安全结束
    sys.exit(app.exec_())
