#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * 시그널 선언시 인자 타입을 선언 후 값 전달하기

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
import string
import time
import random
__author__ = "Deokyu Lim <hong18s@gmail.com>"


class OtpTokenGenerator(QThread):
    """
    1초마다 남은 시간
    5초마다 변화된 OTP 코드를 시그널로 전달
    """
    # 사용자 정의 시그널 선언
    value_changed = pyqtSignal(str, name="ValueChanged")
    expires_in = pyqtSignal(int, name="ExpiresIn")

    EXPIRE_TIME = 5

    def __init__(self):
        QThread.__init__(self)
        self.characters = list(string.ascii_uppercase)
        self.token = self.generate()

    def __del__(self):
        self.wait()

    def generate(self):
        random.shuffle(self.characters)
        return ''.join(self.characters[0:5])

    def run(self):
        """
        토큰 값과 남은 시간을 실시간으로 전송(emit)한다.
        :return:
        """
        self.value_changed.emit(self.token)  # 시작 후 첫 OTP코드 전달
        while True:
            t = int(time.time()) % self.EXPIRE_TIME
            self.expires_in.emit(self.EXPIRE_TIME - t)  # 남은 시간을 전달
            if t != 0:
                self.usleep(1)
                continue
            # 바뀐 토큰 값을 전달
            self.token = self.generate()
            self.value_changed.emit(self.token)
            self.msleep(1000)


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.lb_token = QLabel()
        self.lb_expire_time = QLabel()
        self.otp_gen = OtpTokenGenerator()
        self.init_widget()
        self.otp_gen.start()

    def init_widget(self):
        self.setWindowTitle("Custom Signal")
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
        self.setLayout(form_lbx)

        # 시그널 슬롯 연결
        self.otp_gen.ValueChanged.connect(self.lb_token.setText)
        self.otp_gen.ExpiresIn.connect(lambda v: self.lb_expire_time.setText(str(v)))

        form_lbx.addWidget(self.lb_token)
        form_lbx.addWidget(self.lb_expire_time)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())