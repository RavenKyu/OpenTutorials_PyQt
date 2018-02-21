#!/usr/bin/env python

# 예제 내용
# * 드래그 앤 드랍 사용
# * 드래그시 위젯의 모양 표시
# * 드랍시 마우스 포인터가 TopLeft가 아닌 그랩 포인트에 위치

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QPoint

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

        # 데이터 전송을 위한 MIME 객체 선언
        # 데이터 타입, 보낼 데이터를 Bytes 형으로 저장
        mime_data = QMimeData()
        mime_data.setData("application/hotspot", b"%d %d" % (e.x(), e.y()))

        drag = QDrag(self)
        # MIME 타입데이터를 Drag에 설정
        drag.setMimeData(mime_data)
        # 드래그시 위젯의 모양 유지를 위해 QPixmap에 모양을 렌더링
        pixmap = QPixmap(self.size())
        self.render(pixmap)
        drag.setPixmap(pixmap)

        drag.setHotSpot(e.pos() - self.rect().topLeft())
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
        e.accept()

    def dropEvent(self, e: QDropEvent):
        position = e.pos()

        # 보내온 데이터를 받기
        # 그랩 당시의 마우스 위치값을 함께 계산하여 위젯 위치 보정
        offset = e.mimeData().data("application/hotspot")
        x, y = offset.data().decode('utf-8').split()
        self.btn.move(position - QPoint(int(x), int(y)))

        e.setDropAction(Qt.MoveAction)
        e.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
