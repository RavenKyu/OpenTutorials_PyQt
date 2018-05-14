#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QDomDocument 를 이용한 돔트리뷰 구성

import sys

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTreeView

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QSplitter
from PyQt5.QtGui import QKeySequence
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QProgressBar

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot

from PyQt5.QtXml import QDomDocument

from QtFramework.QtCore.QDomDocument.QDomDocument_00_basic import DomModel

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class DomTreeViewer(QTreeView):
    def __init__(self):
        QTreeView.__init__(self)
        self.setVisible(False)


class ToolBar(QToolBar):
    back_button_clicked = pyqtSignal(name="backClicked")
    forward_button_clicked = pyqtSignal(name="forwardClicked")
    stop_reload_button_clicked = pyqtSignal(int, name="stopReloadClicked")
    address_changed = pyqtSignal(QUrl, name="addressChanged")
    dom_tree_viewer_clicked = pyqtSignal(name="domTreeViewerClicked")

    def __init__(self):
        QToolBar.__init__(self)
        self.setMovable(False)
        self.toggleViewAction().setEnabled(False)
        self.le = QLineEdit()
        self.init_ui()

    def init_ui(self):
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

        fav_action = QAction(self)
        self.le.addAction(fav_action, QLineEdit.LeadingPosition)
        self.le.setClearButtonEnabled(True)
        self.addWidget(self.le)
        self.le.editingFinished.connect(
            lambda: self.address_changed.emit(QUrl(self.le.text())))

        self.addSeparator()
        self.dom_tree_viewer = QAction(self)
        self.dom_tree_viewer.setIcon(QIcon("images/view-dom_tree.png"))
        self.dom_tree_viewer.triggered.connect(self.dom_tree_viewer_clicked)
        self.addAction(self.dom_tree_viewer)


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
        self.splitter = QSplitter()
        self.toolbar = ToolBar()
        self.status_bar = StatusBar()
        self.dom_tree_viewer = DomTreeViewer()
        self.web = QWebEngineView()

        self.init_widget()
        self.toolbar.le.setText("https://www.qt.io")
        self.toolbar.le.editingFinished.emit()

    def init_widget(self):
        self.setWindowTitle("QWebEngineView")
        self.addToolBar(self.toolbar)
        self.splitter.addWidget(self.dom_tree_viewer)

        self.splitter.addWidget(self.web)
        self.setCentralWidget(self.splitter)

        self.web.loadProgress.connect(
            lambda v: self.toolbar.change_stop_reload(bool(0 <= v >= 100)))
        self.web.loadProgress.connect(self.status_bar.set_progress_value)
        self.toolbar.backClicked.connect(self.web.back)
        self.toolbar.forwardClicked.connect(self.web.forward)
        self.toolbar.stopReloadClicked.connect(
            lambda v: self.web.triggerPageAction(v))
        self.toolbar.addressChanged.connect(self.web.setUrl)
        self.setStatusBar(self.status_bar)

        # 돔트리뷰 버튼 토글 구성
        self.toolbar.domTreeViewerClicked.connect(
            lambda: self.dom_tree_viewer.setVisible(
                not self.dom_tree_viewer.isVisible()))

        # 페이지 로딩이 끝나면 돔 트리 구성
        self.web.loadFinished.connect(self.load_finished)
        self.dom_tree_viewer.setAlternatingRowColors(True)

    def load_finished(self):
        # 돔트리를 스트링으로 가져오는 자바크스립 코드를 실행
        page = self.web.page()
        js = "(new XMLSerializer()).serializeToString(window.document)"
        page.runJavaScript(js, lambda v: self.set_new_dom_tree(v))

    def set_new_dom_tree(self, xml):
        document = QDomDocument()
        if document.setContent(xml):
            model = DomModel(document, self)
            self.dom_tree_viewer.setModel(model)
            self.dom_tree_viewer.expandAll()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
