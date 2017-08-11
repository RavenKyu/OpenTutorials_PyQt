#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# 윈도우 메모장(NotePad) 만들기

import sys

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self, flags=Qt.Window)
		self.filename = "제목없음"
		self.init_window()

	def init_window(self):
		"""
		현재 위젯의 모양등을 초기화
		"""
		self.setWindowTitle("제목 없음 - 메모장")
		self.resize(640, 480)
		self.setWindowIcon(QIcon("notepad.ico"))


if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())