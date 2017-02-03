#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * 버튼의 기본 사용법을 알아본다
# * '창 이름'을 변경한다.

import sys

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSlot

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Button(QPushButton):
	"""
	QPushButton 은 QWidget을 상속받고 있으므로 단일 창으로 표출 가능
	"""
	def __init__(self):
		QPushButton.__init__(self, "0")
		self.setFixedSize(100, 100)
		self.click_cnt = 0
		# 시그널이 일어나면 self._pressed를 연결
		# pressed는 QPushButton의 부모위젯인 QAbstratButton에서 상속
		self.pressed.connect(self._pressed)

	@pyqtSlot()  # pyqtSlot 데코레이터는 꼭 필요는 없다. 하지만 메모리 사용 및 호출 속도에서 약간의 이득을 얻을 수 있다.
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
