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
from PyQt5.QtCore import QLocale

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QWidget):
	def __init__(self):
		QWidget.__init__(self, flags=Qt.Widget)
		self.init_widget()

	def init_widget(self):
		self.setWindowTitle(self.tr("Hello World"))

if __name__ == "__main__":
	app = QApplication(sys.argv)

	# 다국어 지원
	translator = QTranslator()
	translator.load("translate\ko_KR.qm")

	# 현재 시스템 로케일 이름을 출력
	tr_path = "translate\\" + QLocale.system().name() + ".qm"
	print(tr_path)
	# translator.load(tr_path)  # 여기선 사용하지 않으므로 주석

	app.installTranslator(translator)

	form = Form()
	form.show()
	exit(app.exec_())