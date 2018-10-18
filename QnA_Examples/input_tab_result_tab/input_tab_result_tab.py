#!/usr/bin/env python
# coding: utf-8
#
# lshsai 님의 질문
# 하나의 큰 mainwindow에서 텝 1(input data 페이지) | 탭2(결과 페이지) 이런식으로 구성되어져 있다면,
# 탭1번 페이지에서 데이터 넣고, 결과값 출력(q버튼)을 클릭했을때,
# 탭2번 페이지로 넘어가서 결과 페이지를 보여주게 하려면 어떻 명령어를 사용해야 하는지 알 수 있을까요?


import sys
import random

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QBoxLayout

from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTabWidget

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class InputPage(QWidget):
    # 계산 버튼이 눌러졌을때 값을 전달할 시그널
    result_changed = pyqtSignal(int, name="resultChanged")

    def __init__(self):
        QWidget.__init__(self)
        self.input_a = 0
        self.input_b = 0

        # 사용될 위젯 생성
        self.lb = QLabel()
        self.pb_change_numbers = QPushButton("Change Numbers!")
        self.pb_cal = QPushButton("Calculate!")

        # 위젯 배치
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
        self.setLayout(form_lbx)
        form_lbx.addWidget(self.lb)
        form_lbx.addWidget(self.pb_change_numbers)
        form_lbx.addWidget(self.pb_cal)

        # 시그널 슬롯 연결
        self.pb_change_numbers.clicked.connect(self.set_random_numbers)
        self.pb_cal.clicked.connect(self.calculate)

        # 기본 값 생성
        self.set_random_numbers()

    # 계산하여 값을 전송
    @pyqtSlot()
    def calculate(self):
        result = self.input_a + self.input_b
        self.result_changed.emit(result)

    @pyqtSlot()
    def set_random_numbers(self):
        self.input_a = random.randrange(1, 100)
        self.input_b = random.randrange(1, 100)
        self.lb.setText("{0} + {1}".format(self.input_a, self.input_b))


class ResultPage(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.lb_result = QLabel()
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
        self.setLayout(form_lbx)
        form_lbx.addWidget(self.lb_result)

    # 페이지 중앙 라벨에 값을 바꿀 수 있는 슬롯
    @pyqtSlot(int, name="setValue")
    def set_value(self, v: int):
        self.lb_result.setText(str(v))


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.tbw = QTabWidget()
        self.init_widget()

    def init_widget(self):
        """
        현재 위젯의 모양등을 초기화
        """
        self.setWindowTitle("Tab Widget")
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
        self.setLayout(form_lbx)
        form_lbx.addWidget(self.tbw)

        # 페이지 생성
        self.page_input = InputPage()
        self.page_result = ResultPage()

        # 기본 탭 생성
        self.tbw.addTab(self.page_input, "Input Page")
        self.tbw.addTab(self.page_result, "Result Page")

        # 시그널 슬롯 연결
        # 입력 페이지의 값이 계산되면 즉시 결과 페이지에 반영됨
        self.page_input.result_changed.connect(self.page_result.set_value)
        # 탭을 결과 페이지로 강제 이동
        self.page_input.result_changed.connect(
            lambda __: self.tbw.setCurrentIndex(1))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())