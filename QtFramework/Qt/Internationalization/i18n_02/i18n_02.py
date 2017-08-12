#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# i18n 을 위한 예제
# 창의 기본 이름이 Hello World지만 한국어 사용일 경우 안녕 세계가 뜨로록 한다.
# * '창 이름'을 변경한다.

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTranslator
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QEvent
from PyQt5.QtCore import QLocale

from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QBoxLayout

from PyQt5.QtCore import pyqtSlot

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QWidget):
	I18N = [
		["English", "translate\en_US.qm"],
		["한국어", "translate\ko_KR.qm"],
		["日本語", "translate\ja_JP.qm"]
	]
	def __init__(self):
		QWidget.__init__(self, flags=Qt.Window)
		self.setMinimumWidth(330)
		self.lb = QLabel()
		self.qb = QComboBox()
		self.qb.addItems([n[0] for n in self.I18N])  # 콤보 박스에 지원하는 언어 삽입
		self.init_widget()

	def init_widget(self):
		self.setWindowTitle("{} - {}".format(self.tr("Hello World"), self.tr("English")))

		form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
		self.setLayout(form_lbx)

		self.lb.setText(self.tr("Good Morning"))
		self.lb.setStyleSheet("font-size: 30px")
		self.qb.currentIndexChanged.connect(self.change_locale)  # 콤보박스의 선택된 내용이 바뀌면 시그널

		form_lbx.addWidget(self.qb)
		form_lbx.addWidget(self.lb)

	@pyqtSlot(int)
	def change_locale(self, idx):
		global translator
		global app

		# 번역스크립트 교체
		app.removeTranslator(translator)
		t = self.I18N[idx][1]
		translator.load(t)
		app.installTranslator(translator)
		self.init_widget()


if __name__ == "__main__":
	app = QApplication(sys.argv)

	# 다국어 지원
	translator = QTranslator()
	translator.load("translate\en_US.qm")
	app.installTranslator(translator)

	form = Form()
	form.show()

	exit(app.exec_())