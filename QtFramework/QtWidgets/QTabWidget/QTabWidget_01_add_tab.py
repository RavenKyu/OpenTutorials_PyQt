#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QTabWidget 탭에 다양한 위젯 추가

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QToolButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

__author__ = "Deokyu Lim <hong18s@gmail.com>"



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

		# 탭 추가 버튼 생성
		tbw_addbtn = QToolButton()
		self.tbw.setCornerWidget(tbw_addbtn, Qt.TopLeftCorner) # 버튼 위치
		tbw_addbtn.setAutoRaise(True)  # 마우스가 올라오면 올라옴
		tbw_addbtn.setIcon(QIcon("plus_icon.png"))  # 아이콘 지정
		tbw_addbtn.clicked.connect(self.add_new_tab)  # 클릭시 시그널 지정
		form_lbx.addWidget(self.tbw)

		# 기본 탭 생성
		self.add_new_tab()


	@pyqtSlot()
	def add_new_tab(self):
		"""
		텍스트 에디트를 가진 텝을 생성
		"""
		self.tbw.addTab(QTextEdit(), "tab #%d" % (self.tbw.count() + 1))


if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())