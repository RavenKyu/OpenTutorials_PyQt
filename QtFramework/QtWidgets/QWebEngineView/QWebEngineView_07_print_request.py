#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QWebEngineView 새 창, 새 탭, 다이얼로그 창 생성 요구

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QDir
from PyQt5.QtCore import QFile
from PyQt5.QtCore import QObject
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineWidgets import QWebEngineScript
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtPrintSupport import QPrintDialog

import qwebchannel_rc

from PyQt5.QtWebChannel import QWebChannel

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class CallHandler(QObject):
    request_print = pyqtSignal(name="requestPrint")

    def __init__(self, parent=None):
        QObject.__init__(self, parent)

    @pyqtSlot(name="webToAppRequestPrint")
    def web_to_app_request_print(self):
        self.request_print.emit()


class WebView(QWebEngineView):
    def __init__(self):
        QWebEngineView.__init__(self)
        url = QDir().current().filePath(
            "html/QWebEngineView_07_print_request.html")
        url = QUrl.fromLocalFile(url)
        self.setUrl(url)
        web_channel_js = QWebEngineScript()
        web_channel_js.setInjectionPoint(QWebEngineScript.DocumentCreation)
        web_channel_js.setWorldId(QWebEngineScript.MainWorld)
        web_channel_js.setRunsOnSubFrames(True)
        web_channel_js_file = QFile(":/qwebchannel")
        web_channel_js_file.open(QFile.ReadOnly)
        js = str(web_channel_js_file.readAll(), 'utf-8')
        web_channel_js.setSourceCode(js)
        self.page().scripts().insert(web_channel_js)

        # Javascript window.print()를 오버라이드
        # 기본 window.print()는 웹브라우져에게 프린터 다이얼로그를 요청하지만
        # 받을 수 없기 때문에 QWebChannel을 통해 받는다.
        override_js_print = QWebEngineScript()
        override_js_print.setInjectionPoint(QWebEngineScript.DocumentCreation)
        override_js_print.setWorldId(QWebEngineScript.MainWorld)
        override_js_print.setName("oveerridejsprint.js")
        override_js_print.setRunsOnSubFrames(True)
        override_js_print.setSourceCode(
            "window.print = function() { "
            "   new QWebChannel(qt.webChannelTransport, function(channel) { "
            "       handler = channel.objects.handler; "
            "       handler.webToAppRequestPrint(); "
            "   });"
            "};"
        )
        self.page().scripts().insert(override_js_print)
        channel = QWebChannel(self.page())
        self.page().setWebChannel(channel)
        self.handler = CallHandler()
        channel.registerObject('handler', self.handler)

        # 시그널슬롯 처리
        self.handler.request_print.connect(self.printer)

    # 프린트 다이얼로그 처리
    def printer(self):
        prnt_dialog = QPrintDialog(self)
        if not prnt_dialog.exec():
            prnt_dialog.deleteLater()
            return
        self.page().print(
            prnt_dialog.printer(), lambda status: prnt_dialog.deleteLater())


if __name__ == "__main__":
    sys.argv.append("--remote-debugging-port=8000")

    app = QApplication(sys.argv)
    form = WebView()
    form.show()
    exit(app.exec_())
