#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QPixmap사용

import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QSplitter
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtGui import QHoverEvent
from PyQt5.QtWidgets import QSizeGrip
from PyQt5.QtWidgets import QRubberBand
from PyQt5.QtCore import QEvent
from PyQt5.QtCore import QRect
from PyQt5.QtCore import QSize
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QGraphicsOpacityEffect


__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Label(QLabel):
    selection_changed = pyqtSignal(QRect, name="selectionChanged")

    def __init__(self):
        QLabel.__init__(self)
        self.rb = QRubberBand(QRubberBand.Rectangle, self)
        self.setMouseTracking(True)

    def mousePressEvent(self, event: QMouseEvent):
        self.origin = event.pos()
        self.rb.setGeometry(QRect(self.origin, QSize()))
        self.rb.show()
        QLabel.mousePressEvent(self, event)

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.rb.isVisible():
            self.rb.setGeometry(
                QRect(self.origin, event.pos()).normalized())
        QWidget.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        if self.rb.isVisible():
            self.rb.hide()
        self.selection_changed.emit(self.rb.geometry())
        QLabel.mouseReleaseEvent(self, event)


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

        lb_1 = Label()

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

        lb_1.selection_changed.connect(self.crop_image)

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