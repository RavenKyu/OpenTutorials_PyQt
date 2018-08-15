#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QWebEngineView 창 닫기 요구

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QDir
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineWidgets import QWebEngineSettings

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class WebView(QWebEngineView):
    def __init__(self):
        QWebEngineView.__init__(self)
        self.settings().setAttribute(
            QWebEngineSettings.JavascriptCanOpenWindows, True)
        # QWebEnginePage에서 windowsCloseRequest를 가지고 있다.
        self.page().windowCloseRequested.connect(self.close)

        # 로컬파일 사용시 절대경로만 사용해야 함
        url = QDir().current().filePath(
            "html/QWebEngineView_06_close_request.html")
        url = QUrl.fromLocalFile(url)
        self.setUrl(url)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WebView()
    form.show()
    exit(app.exec_())
