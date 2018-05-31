#!/usr/bin/env python
# coding: utf-8

# 스크린 캡쳐를 하는 프로그램 제작

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QSplitter
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QListWidgetItem


from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtGui import QScreen

from PyQt5.QtGui import QWindow
from PyQt5.QtGui import QResizeEvent
from PyQt5.QtCore import QSize

from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer


from PyQt5.QtWidgets import QApplication

from PyQt5.QtCore import QThread
from PyQt5.QtCore import QWaitCondition
from PyQt5.QtCore import QMutex
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot


class ThreadCapture(QThread):
    """
    단순히 0부터 100까지 카운트만 하는 쓰레드
    값이 변경되면 그 값을 change_value 시그널에 값을 emit 한다.
    """
    # 사용자 정의 시그널 선언
    captured_screen = pyqtSignal(QPixmap, name="capturedScreen")

    def __init__(self):
        QThread.__init__(self, parent=None)
        self.cond = QWaitCondition()
        self.mutex = QMutex()
        self.cnt = 0
        self._status = True


    def __del__(self):
        self.wait()

    def run(self):
        while True:
            self.mutex.lock()
            if not self._status:
                self.cond.wait(self.mutex)
            pixmap = self.capture()
            self.captured_screen(pixmap)
            self.msleep(100)  # ※주의 QThread에서 제공하는 sleep을 사용

            self.mutex.unlock()

    def capture(self):
        screen: QScreen = QGuiApplication.primaryScreen()
        window: QWindow = self.windowHandle()
        if window:
            screen = window.screen()
        if not screen:
            return
        pixmap = screen.grabWindow(0)
        return pixmap

    def toggle_status(self):
        self._status = not self._status
        if self._status:
            self.cond.wakeAll()

    @property
    def status(self):
        return self._status



class CapturedScreenItem(QWidget):
    def __init__(self, pixmap: QPixmap, parent=None):
        QWidget.__init__(self, flags=Qt.Widget, parent=parent)
        layout = QVBoxLayout()

        self.pixmap = pixmap
        self.lb = QLabel(self)
        self.lb.setPixmap(pixmap)
        layout.setSizeConstraint(QVBoxLayout.SetFixedSize)
        self.lb.setStyleSheet("background-color: gray")
        self.lb.setMinimumSize(200, 100)

        layout.addWidget(self.lb)
        self.setLayout(layout)
        self.update_screen_capture()

    def resizeEvent(self, event: QResizeEvent):
        QWidget.resizeEvent(self, event)

        scale_size: QSize = self.pixmap.size()
        # scale_size: QSize = self.size()
        scale_size.scale(self.lb.size(), Qt.KeepAspectRatio)

        if not self.lb.pixmap() or scale_size != self.lb.pixmap().size():
            print("resize")
            self.update_screen_capture()


    def update_screen_capture(self):
        self.lb.setPixmap(self.pixmap.scaledToHeight(
            self.lb.size().height(), Qt.SmoothTransformation))


class ListWidget(QListWidget):
    def __init__(self):
        QListWidget.__init__(self)


class UI(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # self.setFixedSize(640, 480)
        self.setMinimumSize(200, 480)
        self.splitter_1 = QSplitter()
        self.splitter_2 = QSplitter()
        self.lb_captured_screen = QLabel(self)
        self.lb_captured_screen.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.lb_captured_screen.setStyleSheet("background-color: red")
        self.lb_captured_screen.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
        screen_geometry = QApplication.desktop().screenGeometry(self)
        self.lb_captured_screen.setMinimumSize(
            screen_geometry.width() / 8, screen_geometry.height() / 8)

        self.captured_pixmap = QPixmap()
        self.pb = QPushButton("Capture Screen")
        vlayout = QVBoxLayout(self)
        # vlayout.addWidget(self.lb_captured_screen)
        self.viewer = QListWidget()

        self.splitter_1.addWidget(self.lb_captured_screen)
        self.splitter_1.addWidget(self.splitter_2)
        self.splitter_2.addWidget(self.viewer)
        vlayout.addWidget(self.splitter_1)
        vlayout.addWidget(self.pb)
        self.setLayout(vlayout)


class Form(UI):
    def __init__(self):
        UI.__init__(self)
        self.pb.clicked.connect(self.capture)
        self.capture()

    def resizeEvent(self, event: QResizeEvent):
        scale_size: QSize = self.captured_pixmap.size()
        scale_size.scale(self.lb_captured_screen.size(), Qt.KeepAspectRatio)

        if not self.lb_captured_screen.pixmap() \
                or scale_size != self.lb_captured_screen.pixmap().size():
            self.update_screen_capture()
        UI.resizeEvent(self, event)

    def capture(self):
        self.hide()
        QTimer.singleShot(1, self._capture)

    def _capture(self):
        screen: QScreen = QGuiApplication.primaryScreen()
        window: QWindow = self.windowHandle()
        if window:
            screen = window.screen()
        if not screen:
            return
        pixmap = screen.grabWindow(0)
        self.captured_pixmap = pixmap
        self.update_screen_capture()

        item = QListWidgetItem(self.viewer)
        custom_widget = CapturedScreenItem(pixmap)
        item.setSizeHint(custom_widget.sizeHint())
        self.viewer.setItemWidget(item, custom_widget)
        self.viewer.addItem(item)
        self.show()

        self.viewer.scrollToBottom()

    def update_screen_capture(self):
        self.lb_captured_screen.setPixmap(
            self.captured_pixmap.scaled(
                self.lb_captured_screen.size(),
                Qt.KeepAspectRatio, Qt.SmoothTransformation))


if "__main__" == __name__:
    import sys
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())

