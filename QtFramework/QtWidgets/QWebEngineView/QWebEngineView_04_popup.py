#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QWebEngineView 새 창, 새 탭, 다이얼로그 창 생성 요구

import sys

from PyQt5.QtCore import QDir
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineWidgets import QWebEngineSettings
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWebEngineWidgets import QWebEngineProfile

from PyQt5.QtGui import QCloseEvent

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class WebView(QWebEngineView):
    def __init__(self):
        QWebEngineView.__init__(self)
        self.settings().setAttribute(
            QWebEngineSettings.JavascriptCanOpenWindows, True)
        self.p = Page()
        self.setPage(self.p)
        self.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.settings().setAttribute(QWebEngineSettings.JavascriptCanOpenWindows, True)

    def createWindow(self, wind_type):
        print(wind_type)
        # 새로운 탭 생성 요구시
        if wind_type == QWebEnginePage.WebBrowserTab:
            # 주의: 아래 코드는 새 윈도우를 만들어 주는 코드이다.
            # 본 예제는 탭을 사용하지 않으므로 새 창으로 대체

            # View 는 반드시 클래스 변수 생성로 해주어야 한다.
            # 로컬 변수로 생성시 메서드 리턴시 소멸
            # self.popup = WebPopupWindow(self.page().profile())
            self.popup = WebPopupWindow(self.p.profile())
            view = self.popup.view()
            self.popup.show()
            return view
        if wind_type == QWebEnginePage.WebBrowserBackgroundTab:
            pass
        # 새로운 창 생성 요구시
        if wind_type == QWebEnginePage.WebBrowserWindow:
            pass
        # 다이얼로그 창 생성 요구시
        if wind_type == QWebEnginePage.WebDialog:
            popup = Frame(self.page().profile())
            popup.show()
            return popup.web
        return None


class Page(QWebEnginePage):
    pass


class WebPopupWindow(WebView):
    def __init__(self, profile: QWebEngineProfile):
        WebView.__init__(self)
        page = Page(profile, self)
        # window.open 의 인수값으로 입력된 위치크기 정보를 이용하여 크기 변경
        # window.open에서 width, height, x, y 값이 인자 값으로 있다면 아래의
        # 코드가 반드시 필요
        page.geometryChangeRequested.connect(self.setGeometry)

        self.setPage(page)
        self.setFocus()

    def closeEvent(self, event: QCloseEvent):
        WebView.closeEvent(self, event)


class Frame(QWidget):
    def __init__(self, profile):
        QWidget.__init__(self)
        self.web = WebPopupWindow(profile)
        self.web.show()


if __name__ == "__main__":
    sys.argv.append("--remote-debugging-port=8000")

    app = QApplication(sys.argv)
    form = WebView()
    # 로컬파일 사용시 절대경로만 사용해야 함
    url = QDir().current().filePath(
        "html/QWebEngineView_04_popup.html")
    url = QUrl.fromLocalFile(url)
    form.setUrl(url)
    form.show()
    exit(app.exec_())
