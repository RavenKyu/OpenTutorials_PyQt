#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * 사용자정의 시그널 만들어 사용하기

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal

import time
__author__ = "Deokyu Lim <hong18s@gmail.com>"


class TicGenerator(QThread):
    """
    5초마다 틱 신호를 전달
    """
    # 사용자 정의 시그널 선언
    # 외부에서 사용할때 tic대신 Tic을 이용하여 호출할 수 있다.
    # Qt의 시그널 및 슬롯 이름은 Camel을 사용하기 때문에 파이썬의 PEP8을 지키면서 작성한다면 name을 반드시 사용
    tic = pyqtSignal(name="Tic")

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            t = int(time.time())
            if not t % 5 == 0:
                self.usleep(1)
                continue
            self.Tic.emit()
            self.msleep(1000)


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.te = QTextEdit()
        self.tic_gen = TicGenerator()
        self.init_widget()
        self.tic_gen.start()

    def init_widget(self):
        self.setWindowTitle("Custom Signal")
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
        self.setLayout(form_lbx)

        # 시그널 슬롯 연결
        self.tic_gen.Tic.connect(
            lambda: self.te.insertPlainText(time.strftime("[%H:%M:%S] Tic!\n"))
        )

        form_lbx.addWidget(self.te)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())