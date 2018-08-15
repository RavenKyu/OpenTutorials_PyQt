#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QWebEngineView 자바스크립트 경고창 커스터마이징

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QDir
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMessageBox

import qwebchannel_rc

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Page(QWebEnginePage):
    # 자바스크립트 경고 박스 요청시 호출
    def javaScriptAlert(self, url, msg):
        msg_box = QMessageBox(
            QMessageBox.Warning, "", "Error", QMessageBox.Ok)
        msg_box.setWindowTitle("Alert")
        msg_box.setInformativeText(msg)
        msg_box.exec()
        return


class WebView(QWebEngineView):
    def __init__(self):
        QWebEngineView.__init__(self)
        # 사용자정의 Page 사용
        self.p = Page(self.page().profile())
        self.setPage(self.p)
        url = QDir().current().filePath(
            "html/QWebEngineView_08_alert.html")
        url = QUrl.fromLocalFile(url)
        self.page().setUrl(url)


if __name__ == "__main__":
    sys.argv.append("--remote-debugging-port=8000")

    app = QApplication(sys.argv)
    form = WebView()
    form.show()
    exit(app.exec_())
