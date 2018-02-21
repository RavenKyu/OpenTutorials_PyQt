#!/usr/bin/env python

# 예제 내용
# * 드래그 앤 드랍 사용

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QApplication

from PyQt5.QtGui import QDragEnterEvent
from PyQt5.QtGui import QDropEvent
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QBoxLayout

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Button(QPushButton):
    def __init__(self, title):
        QPushButton.__init__(self, title)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e: QDragEnterEvent):
        """
        여기서 event 진행의 허락을 결정해야 한다.
        """
        if e.mimeData().hasFormat('text/plain'):
            # mime타입이 text/plain 타입인지 검
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e: QDropEvent):
        self.setText(e.mimeData().text())


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)

        self.init_widget()

    def init_widget(self):
        """
        현재 위젯의 모양등을 초기화
        """
        self.setWindowTitle("Hello World")
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, self)
        self.setLayout(form_lbx)

        le = QLineEdit()
        le.setDragEnabled(True)  # 드래그가 가능

        btn = Button("Button!")
        form_lbx.addWidget(le)
        form_lbx.addWidget(btn)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
