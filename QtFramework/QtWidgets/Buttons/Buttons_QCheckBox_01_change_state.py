#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * CheckBox 사용
# * CheckBox Signal 사용

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QBoxLayout

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

from PyQt5.QtCore import pyqtSlot

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QWidget):
	MSG = {True: "All Checked", False: "Not All Checked"}

	def __init__(self):
		QWidget.__init__(self, flags=Qt.Widget)
		self.setWindowTitle("CheckBox")
		base_layout = QBoxLayout(QBoxLayout.TopToBottom, self)
		self.setLayout(base_layout)

		# 배치될 위젯 변수 선언
		self.lb = QLabel()
		base_layout.addWidget(self.lb)

		# CheckBox 위젯 생성 및 시그널 연결
		self.cb_list = list()
		for i in range(2):
			w = QCheckBox("CheckBox %s" % i)
			w.stateChanged.connect(self._confirm)
			base_layout.addWidget(w)
			self.cb_list.append(w)

		# 현재 상태 라벨에 출력
		self._confirm()

	@pyqtSlot(int)
	def _confirm(self):
		state = all([bool(x.checkState()) for x in self.cb_list])
		self.lb.setText(self.MSG[state])

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())