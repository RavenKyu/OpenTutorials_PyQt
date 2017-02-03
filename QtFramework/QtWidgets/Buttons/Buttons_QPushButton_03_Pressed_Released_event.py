#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * 토클 버튼의 사용법을 알아본다


import sys

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSlot

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Button(QPushButton):
	def __init__(self):
		QPushButton.__init__(self, "Relesed")
		self.setFixedSize(100, 100)
		self.setStyleSheet("background-color: red")

	def mousePressEvent(self, QMouseEvent):
		self.setText("Pressing")
		self.setStyleSheet("background-color: green")

	def mouseReleaseEvent(self, QMouseEvent):
		self.setText("Relesed")
		self.setStyleSheet("background-color: red")



	@pyqtSlot(bool)
	def slot_toggle(self, state):
		"""
		toggle 상태에 따라 배경색과 상태 텍스트 변환
		"""
		self.setStyleSheet("background-color: %s" % ({True: "green", False: "red"}[state]))
		self.setText({True: "ON", False: "OFF"}[state])

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Button()
	form.show()
	exit(app.exec_())
