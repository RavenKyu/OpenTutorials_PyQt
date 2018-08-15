#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * 웹채널 사용시 데이터 타입

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QDir
from PyQt5.QtCore import QJsonValue
from PyQt5.QtCore import QJsonDocument
from PyQt5.QtCore import QObject
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot


__author__ = "Deokyu Lim <hong18s@gmail.com>"


class CallHandler(QObject):
    """
    콜 핸들러 클래스는 Js와 통신하는 부분을 분리 목적
    """
    # app_to_web_send_data = pyqtSignal(dict, name="appToWebSendData")
    app_to_web_send_data = pyqtSignal(QJsonDocument, name="appToWebSendData")

    # ==========================================================================
    @staticmethod
    def recursive_qjsonvalue_convert(data):
        """
        QWebChannel을 통하여 받은 데이터는 요소 모두가 QJasonValue 이다.
        재귀를 이용하여 요소의 타입을 검색하고 바른 반환 값을 넘긴다.
        :param data:
        :return:
        """
        if not isinstance(data, QJsonValue):
            return data
        # Python의 List
        if data.isArray():
            array = data.toArray()
            new_array = list()
            for d in array:
                new_array.append(
                    CallHandler.recursive_qjsonvalue_convert(d))
            return new_array
        # Python의 Dict
        elif data.isObject():
            objects = data.toObject()
            new_dict = dict()
            for key in list(objects.keys()):
                d = objects[key]
                new_dict[key] = \
                    CallHandler.recursive_qjsonvalue_convert(d)
            return new_dict

        elif data.isBool():
            return data.toBool()
        elif data.isDouble():
            return data.toDouble()
        elif data.isString():
            return data.toString()
        elif data.isUndefined():
            return None
        elif data.isNull():
            return None

    @pyqtSlot(QJsonValue, name='webToAppSendData')
    def web_to_app_send_data(self, value):
        # QJasonValue 데이터를 Python Dict 형태로 변환
        data = CallHandler.recursive_qjsonvalue_convert(value)
        print(data)


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
            "html/QWebEngineView_09_WebChannelDataType.html")
        url = QUrl.fromLocalFile(url)
        self.web.load(url)

        # 핸들러 시그널 버튼이 눌러지면 console로 value를 보낸다.
        value = {"data": "ABC", "msg": ["DEF", 1, {"A": False, "B": True}]}
        document = QJsonDocument()
        document.setObject(value)
        self.pb_1.clicked.connect(
            lambda v: self.handler.app_to_web_send_data.emit(document))

        self.layout_2.addWidget(self.web)
        self.layout_3.addWidget(self.pb_1)


if __name__ == "__main__":
    sys.argv.append("--remote-debugging-port=8000")
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())