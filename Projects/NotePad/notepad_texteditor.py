#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# 윈도우 메모장(NotePad) 만들기


from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtCore import Qt

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class TextEditor(QTextEdit):
    def __init__(self):
        QTextEdit.__init__(self)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    form = TextEditor()
    form.show()
    exit(app.exec_())