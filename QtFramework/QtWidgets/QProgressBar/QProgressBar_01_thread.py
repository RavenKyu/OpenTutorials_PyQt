#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * 실행상태바의 기본 사용
# * Thread를 이용한 동시성

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread
from PyQt5.QtCore import QWaitCondition
from PyQt5.QtCore import QMutex
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Thread(QThread):
    """
    단순히 0부터 100까지 카운트만 하는 쓰레드
    값이 변경되면 그 값을 change_value 시그널에 값을 emit 한다.
    """
    # 사용자 정의 시그널 선언
    change_value = pyqtSignal(int)

    def __init__(self):
        QThread.__init__(self)
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

            if 100 == self.cnt:
                self.cnt = 0
            self.cnt += 1
            self.change_value.emit(self.cnt)
            self.msleep(100)  # ※주의 QThread에서 제공하는 sleep을 사용

            self.mutex.unlock()

    def toggle_status(self):
        self._status = not self._status
        if self._status:
            self.cond.wakeAll()

    @property
    def status(self):
        return self._status


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.pgsb = QProgressBar()
        self.pb = QPushButton("Pause")
        self.th = Thread()
        self.init_widget()
        self.th.start()

    def init_widget(self):
        self.setWindowTitle("QProgressBar with QThread")
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
        self.setLayout(form_lbx)

        # 시그널 슬롯 연결
        self.pb.clicked.connect(self.slot_clicked_button)
        self.th.change_value.connect(self.pgsb.setValue)

        form_lbx.addWidget(self.pgsb)
        form_lbx.addWidget(self.pb)

    @pyqtSlot()
    def slot_clicked_button(self):
        """
        사용자정의 슬롯
        쓰레드의 status 상태 변경
        버튼 문자 변경
        쓰레드 재시작
        """
        self.th.toggle_status()
        self.pb.setText({True: "Pause", False: "Resume"}[self.th.status])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())