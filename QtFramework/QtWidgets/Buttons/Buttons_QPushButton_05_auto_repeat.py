#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * 설정된 인터벌을 참고하여 주기적 pressed 시그널 발생

import sys

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSlot

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Button(QPushButton):
	def __init__(self):
		QPushButton.__init__(self, "0")
		self.setFixedSize(100, 100)

		# 주기적으로 pressed 시그널 발생
		# 밀리세컨드 단위로 인터벌 조정 가능
		self.setAutoRepeatInterval(10)
		self.setAutoRepeat(True)
		self.click_cnt = 0

		self.pressed.connect(self._pressed)
	#
	@pyqtSlot()
	def _pressed(self):
		"""
		클릭 수를 카운터하여 표출
		"""
		self.click_cnt += 1
		self.setText(str(self.click_cnt))

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Button()
	form.show()
	exit(app.exec_())
