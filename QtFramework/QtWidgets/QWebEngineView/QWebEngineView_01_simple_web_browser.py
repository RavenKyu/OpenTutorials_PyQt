#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QWebEngineView를 이용한 웹 위젯 사용

import sys

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QBoxLayout

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QKeySequence
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QProgressBar

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot

from PyQt5.QtWidgets import QStatusBar

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class ToolBar(QToolBar):
    back_button_clicked = pyqtSignal(name="backClicked")
    forward_button_clicked = pyqtSignal(name="forwardClicked")
    stop_reload_button_clicked = pyqtSignal(int, name="stopReloadClicked")
    address_changed = pyqtSignal(str, name="addressChanged")

    def __init__(self):
        QToolBar.__init__(self)
        self.setMovable(False)
        self.toggleViewAction().setEnabled(False)
        back_action = QAction(self)
        back_action.setShortcut(QKeySequence(Qt.Key_Back))
        back_action.setIcon(QIcon("images/go-previous.png"))

        self.addAction(back_action)
        back_action.triggered.connect(self.back_button_clicked)

        forward_action = QAction(self)
        forward_action.setShortcut(QKeySequence(Qt.Key_Forward))
        forward_action.setIcon(QIcon("images/go-next.png"))
        self.addAction(forward_action)
        forward_action.triggered.connect(self.forward_button_clicked)

        self.stop_reload_action = QAction(self)
        self.stop_reload_action.setShortcut(QKeySequence(Qt.Key_F5))
        self.stop_reload_action.setIcon(QIcon("images/view-refresh.png"))
        self.stop_reload_action.setData(QWebEnginePage.Reload)
        self.addAction(self.stop_reload_action)
        self.stop_reload_action.triggered.connect(
            lambda: self.stop_reload_button_clicked.emit(
                QWebEnginePage.WebAction(self.stop_reload_action.data())))

        self.le = QLineEdit()
        fav_action = QAction(self)
        self.le.addAction(fav_action, QLineEdit.LeadingPosition)
        self.le.setClearButtonEnabled(True)
        self.addWidget(self.le)
        self.le.editingFinished.connect(
            lambda: self.address_changed.emit(self.le.text()))

    @pyqtSlot(bool, name="changeStopReload")
    def change_stop_reload(self, state):
        if state:
            self.stop_reload_action.setShortcut(QKeySequence(Qt.Key_F5))
            self.stop_reload_action.setIcon(QIcon("images/view-refresh.png"))
            self.stop_reload_action.setData(QWebEnginePage.Reload)
        else:
            self.stop_reload_action.setShortcut(QKeySequence(Qt.Key_Escape))
            self.stop_reload_action.setIcon(QIcon("images/process-stop.png"))
            self.stop_reload_action.setData(QWebEnginePage.Stop)


class StatusBar(QStatusBar):
    def __init__(self):
        QStatusBar.__init__(self)
        self.progress_bar = QProgressBar()
        self.addWidget(self.progress_bar)

    @pyqtSlot(int, name="setProgressValue")
    def set_progress_value(self, v):
        self.progress_bar.setValue(v)


class Form(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("QWebEngineView")
        self.toolbar = ToolBar()
        self.statusbar = StatusBar()
        self.addToolBar(self.toolbar)
        self.web = QWebEngineView()
        self.web.setUrl(QUrl("https://www.qt.io"))
        self.setCentralWidget(self.web)

        self.web.loadProgress.connect(
            lambda v: self.toolbar.changeStopReload(bool(0 <= v >= 100)))
        self.web.loadProgress.connect(self.statusbar.setProgressValue)
        self.toolbar.backClicked.connect(self.web.back)
        self.toolbar.forwardClicked.connect(self.web.forward)
        self.toolbar.stopReloadClicked.connect(
            lambda v: self.web.triggerPageAction(v))
        self.toolbar.addressChanged.connect(lambda v: self.web.setUrl(QUrl(v)))
        self.setStatusBar(self.statusbar)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
