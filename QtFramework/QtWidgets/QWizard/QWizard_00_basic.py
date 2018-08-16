#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# QWizard 사용 예제


import sys

from PyQt5.QtWidgets import QWizard
from PyQt5.QtWidgets import QWizardPage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

__author__ = "Deokyu Lim <hong18s@gmail.com>"

class Start(QWizardPage):
    def __init__(self):
        QWizardPage.__init__(self)
        self.setTitle("Start Page")
        self.setSubTitle("Sub Start Page")


class Form(QWizard):
    def __init__(self):
        QWizard.__init__(self, flags=Qt.Widget)
        self.init_widget()
        self.init_pages()

    def init_pages(self):
        self.addPage(Start())

    def init_widget(self):
        self.setWindowTitle("Hello World")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
