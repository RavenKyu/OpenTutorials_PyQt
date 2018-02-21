#!/usr/bin/env python

# 예제 내용
# * 드래그 앤 드랍 사용

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication

from PyQt5.QtGui import QDragEnterEvent
from PyQt5.QtGui import QDropEvent
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtGui import QDrag
from PyQt5.QtGui import QPixmap

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QMimeData


__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Button(QPushButton):
    def __init__(self, title, parent):
        QPushButton.__init__(self, title, parent)
        self.offset = 0

    def mouseMoveEvent(self, e: QMouseEvent):
        # 왼쪽 버튼은 클릭용이므로 오른쪽 버튼 입력 허용
        if e.buttons() != Qt.RightButton:
            return

        mime_data = QMimeData()  # 데이터 전송을 위한 MIME 객체 선언
        drag = QDrag(self)  # QDrag는 오직 드래그앤드랍에서만 사용
        drag.setMimeData(mime_data)

        drag.exec_(Qt.MoveAction)


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setFixedSize(300, 300)
        self.btn = Button("Drag me to the moon", self)
        self.init_widget()

    def init_widget(self):
        """
        현재 위젯의 모양등을 초기화
        """
        self.setWindowTitle("Drag and Drop")
        self.setAcceptDrops(True)
        self.btn.show()

    def dragEnterEvent(self, e: QDragEnterEvent):
        # 들어오는 이벤트들 모두 통과
        e.accept()

    def dropEvent(self, e: QDropEvent):
        # 마우스 위치를 이용하여 버튼의 위치를 변경
        position = e.pos()
        self.btn.move(position)

        e.setDropAction(Qt.MoveAction)
        e.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
