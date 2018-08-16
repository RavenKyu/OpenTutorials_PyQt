#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# QWizard 사용 예제


import sys

from PyQt5.QtWidgets import QWizard
from PyQt5.QtWidgets import QWizardPage
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Start(QWizardPage):
    def __init__(self):
        QWizardPage.__init__(self)
        self.setTitle("Start Page")
        self.setSubTitle("Sub Start Page")

        layout = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(layout)

        self.num = 0
        self.slider = QSlider()
        self.slider.valueChanged.connect(lambda v: setattr(self, "num", v))

        # 등록시 * 를 표시한 목록은 반드시 이벤트 후, 다음 페이지로 이동
        self.registerField("num*", self.slider)
        layout.addWidget(self.slider)

    def isComplete(self):
        print(self.num)
        if self.num != 99:
            return False
        return True


class Form(QWizard):
    def __init__(self):
        QWizard.__init__(self, flags=Qt.Widget)
        self.page_start = Start()
        self.init_widget()
        self.init_pages()

    def init_pages(self):
        self.addPage(self.page_start)

    def init_widget(self):
        self.setWindowTitle("Hello World")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
