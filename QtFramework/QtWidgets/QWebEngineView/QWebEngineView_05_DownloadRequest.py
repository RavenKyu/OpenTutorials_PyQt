#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QWebEngineView 다운로드 요청

import sys

from PyQt5.QtCore import QDir
from PyQt5.QtCore import QUrl

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineWidgets import QWebEngineSettings
from PyQt5.QtWebEngineWidgets import QWebEngineDownloadItem

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog


__author__ = "Deokyu Lim <hong18s@gmail.com>"


class WebView(QWebEngineView):
    def __init__(self):
        QWebEngineView.__init__(self)
        self.settings().setAttribute(
            QWebEngineSettings.JavascriptCanOpenWindows, True)

        self.setPage(self.page())
        self.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.settings().setAttribute(QWebEngineSettings.JavascriptCanOpenWindows, True)
        self.page().profile().downloadRequested.connect(self.download_file)

        # 로컬파일 사용시 절대경로만 사용해야 함
        url = QDir().current().filePath(
            "html/QWebEngineView_05_download_request.html")
        url = QUrl.fromLocalFile(url)
        self.setUrl(url)

    # 웹 다운로드 요청시 열어줄 파일 다이얼로그 처리
    def download_file(self, item: QWebEngineDownloadItem):
        # 다운로드 되는 것이 웹페이지 파일일 경우 포맷 지정
        # item.setSavePageFormat(QWebEngineDownloadItem.SingleHtmlSaveFormat)
        path = QFileDialog.getSaveFileName(self, "Save as", item.path())
        # 취소했다면 ('', '') 리턴
        if not path[0]:
            return
        # 다운받을 path 지정 및 다운로드 시작
        item.setPath(path[0])
        item.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WebView()
    form.show()
    exit(app.exec_())
