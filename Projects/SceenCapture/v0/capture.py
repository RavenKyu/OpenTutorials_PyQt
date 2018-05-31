#!/usr/bin/env python
# coding: utf-8

# 스크린 캡쳐를 하는 프로그램 제작

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton

from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtGui import QScreen

from PyQt5.QtGui import QWindow
from PyQt5.QtGui import QResizeEvent
from PyQt5.QtCore import QSize

from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication


class UI(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.lb_captured_screen = QLabel(self)
        self.lb_captured_screen.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.lb_captured_screen.setStyleSheet("background-color: red")
        self.lb_captured_screen.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
        screen_geometry = QApplication.desktop().screenGeometry(self)
        self.lb_captured_screen.setMinimumSize(
            screen_geometry.width() / 8, screen_geometry.height() / 8)

        self.captured_pixmap = QPixmap()
        self.pb = QPushButton("Capture Screen")
        vlayout = QVBoxLayout(self)
        vlayout.addWidget(self.lb_captured_screen)
        vlayout.addWidget(self.pb)


class Form(UI):
    def __init__(self):
        UI.__init__(self)
        self.pb.clicked.connect(self.capture)
        self.capture()

    def resizeEvent(self, event: QResizeEvent):
        scale_size: QSize = self.captured_pixmap.size()
        scale_size.scale(self.lb_captured_screen.size(), Qt.KeepAspectRatio)

        if not self.lb_captured_screen.pixmap() \
                or scale_size != self.lb_captured_screen.pixmap().size():
            self.update_screen_capture()
        UI.resizeEvent(self, event)

    def capture(self):
        self.hide()
        screen: QScreen = QGuiApplication.primaryScreen()
        window: QWindow = self.windowHandle()
        if window:
            screen = window.screen()
        if not screen:
            return

        self.captured_pixmap: QPixmap = screen.grabWindow(0)
        self.update_screen_capture()
        self.show()

    def update_screen_capture(self):
        self.lb_captured_screen.setPixmap(self.captured_pixmap.scaled(
            self.lb_captured_screen.size(),
            Qt.KeepAspectRatio, Qt.SmoothTransformation))


if "__main__"== __name__:
    import sys
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())

