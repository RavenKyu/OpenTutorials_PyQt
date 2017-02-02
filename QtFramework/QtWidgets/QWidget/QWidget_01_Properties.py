#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * Label을 Form에 붙여서 텍스트 출력
# * QWidget이 가진 속성을 출력

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QWidget):
	def __init__(self):
		QWidget.__init__(self, flags=Qt.Widget)

		# self 변수 초기화. 꼭 필요하지는 않음
		self.lb = None

		self.init_widget()

	def init_widget(self):
		self.setWindowTitle("Hello World")
		self.setGeometry(100, 100, 640, 480)  # 창 위치, 크기 설정

		# QLabel 인스턴스 생성
		# 인자값으로 parent인 self 지정
		# QLabel(str, parent), QLabel(parent) 등으로 줄 수 있음
		self.lb = QLabel(self)
		properties_list = (
			"width", "height", "x", "y", "geometry",
			"maximumHeight", "maximumWidth", "maximumSize", "minimumSize", "minimumWidth",
			"size", "windowFilePath", "windowTitle"
		)  # 출력할 property 이름
		msg = self.get_properties_value(properties_list)  # property 이름과 값을 돌려주는 함수 호출
		self.lb.setText(msg)  # Label에 텍스트 설정

	def get_properties_value(self, properties):
		"""
		인자 값으로 property의 이름을 담은 시퀀스 자료형
		property를 차례로 호출하며 이름과 값의 문자열 생성

		:param properties list or tuple
		:return str
		"""
		msg = []
		for p in properties:
			if not hasattr(self, p):
				continue
			value = getattr(self, p)()  # == self.width(), self.x()
			msg.append("{:>20s} : {:<30s}".format(p, str(value)))
		msg = "\n".join(msg)
		return msg


if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())
