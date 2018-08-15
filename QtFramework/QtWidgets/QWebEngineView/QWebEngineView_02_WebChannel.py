#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * Qt와 Javascript을 연결하여 웹을 제어

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QBoxLayout

from PyQt5.QtWidgets import QApplication

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QDir

from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QPushButton

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel

from PyQt5.QtCore import QObject
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class CallHandler(QObject):
    """
    콜 핸들러 클래스는 Js와 통신하는 부분을 분리 목적
    """
    get_text = pyqtSignal(str, name="getText")

    @pyqtSlot(str, name='setText')
    def set_text(self, v):
        print(v)


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)

        # 레이아웃 선언 및 Form Widget에 설정
        self.layout_1 = QBoxLayout(QBoxLayout.LeftToRight, self)
        self.layout_2 = QBoxLayout(QBoxLayout.LeftToRight)
        self.layout_3 = QBoxLayout(QBoxLayout.TopToBottom)

        # 부모 레이아웃에 자식 레이아웃을 추가
        self.layout_1.addLayout(self.layout_2)
        self.layout_1.addLayout(self.layout_3)

        self.web = QWebEngineView()
        self.pb_1 = QPushButton("요청하기")
        self.te_1 = QTextEdit()

        # Web과 통신할 수 있게 채널링
        channel = QWebChannel(self.web.page())
        self.web.page().setWebChannel(channel)
        self.handler = CallHandler()  # 반드시 인스턴스 변수로 사용해야 한다.
        channel.registerObject('handler', self.handler)  # js에서 불리울 이름

        self.setLayout(self.layout_1)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("QWebChannel")
        self.setFixedWidth(640)
        self.setFixedHeight(480)

        # 로컬파일 사용시 절대경로만 사용해야 함
        url = QDir().current().filePath(
            "html/QWebEngineView_02_WebChannel.html")
        url = QUrl.fromLocalFile(url)
        self.web.load(url)

        # 핸들러 시그널 버튼이 눌러지면 console로 Hi를 보낸다.
        self.pb_1.clicked.connect(
            lambda v: self.handler.getText.emit(self.te_1.toPlainText()))

        self.layout_2.addWidget(self.web)
        self.layout_3.addWidget(self.pb_1)
        self.layout_3.addWidget(self.te_1)


if __name__ == "__main__":
    sys.argv.append("--remote-debugging-port=8000")
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())