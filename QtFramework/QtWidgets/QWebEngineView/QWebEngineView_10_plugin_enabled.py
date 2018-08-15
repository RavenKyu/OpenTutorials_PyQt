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

        # Flash 등을 사용하기 위해서 Plugin 사용을 허락
        QWebEngineSettings.globalSettings().setAttribute(
            QWebEngineSettings.PluginsEnabled, True);

        # 로컬파일 사용시 절대경로만 사용해야 함
        url = QDir().current().filePath(
            "html/QWebEngineView_10_plugin_enabled.html")
        url = QUrl.fromLocalFile(url)
        self.setUrl(url)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WebView()
    form.show()
    exit(app.exec_())
