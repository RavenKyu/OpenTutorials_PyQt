#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QPixmap사용

import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtCore import QRect
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QGraphicsOpacityEffect


__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Rectangle(QLabel):
    change_position = pyqtSignal(QRect, name="changePosition")

    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        self.is_pressed = False

    def mousePressEvent(self, event: QMouseEvent):
        self.grab_location = event.pos()
        QWidget.mousePressEvent(self, event)

    def mouseMoveEvent(self, event: QMouseEvent):
        pos = event.pos()
        pos = self.pos() + pos
        self.move(pos - self.grab_location)
        self.change_position.emit(QRect(self.geometry()))
        QWidget.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        QWidget.mouseReleaseEvent(self, event)


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.origin_pixmap = QPixmap("apple.jpg")
        self.init_ui()

    def init_ui(self):
        self.setMinimumWidth(320)
        self.setMinimumHeight(240)
        layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.setLayout(layout)

        lb_1 = QLabel()
        self.origin_pixmap = self.origin_pixmap.scaledToHeight(240)  # 사이즈가 조정
        lb_1.setPixmap(self.origin_pixmap)
        layout.addWidget(lb_1)

        # 자를 영역 선택, 복사
        rect = QRect(50, 50, 50, 50)
        cropped = self.origin_pixmap.copy(rect)

        self.lb_2 = QLabel()
        self.lb_2.setPixmap(cropped)
        self.lb_2.setFixedSize(100, 100)
        layout.addWidget(self.lb_2)

        w = Rectangle(parent=lb_1)
        w.setGeometry(0, 0, 100, 100)
        w.setStyleSheet("background-color: red")
        opacity_effect = QGraphicsOpacityEffect(self)
        opacity_effect.setOpacity(0.3)
        w.setGraphicsEffect(opacity_effect)

        w.change_position.connect(self.crop_image)

    @pyqtSlot(QRect, name="cropImage")
    def crop_image(self, crop_rect):
        # 자를 영역 선택, 복사
        cropped = self.origin_pixmap.copy(crop_rect)
        self.lb_2.setPixmap(cropped)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Window()
    form.show()
    exit(app.exec_())