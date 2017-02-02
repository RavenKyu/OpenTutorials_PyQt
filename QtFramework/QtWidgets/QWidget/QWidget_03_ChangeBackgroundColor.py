#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * 마우스의 움직임에 따라 위젯의 배경색을 바꾼

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QPalette

from math import sqrt

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Label(QLabel):
	def __init__(self, parent=None):
		super(Label, self).__init__(parent)
		self.setMouseTracking(True)  # 마우스가 Label 위를 이동하는 것을 감
		self.setAutoFillBackground(True)  # 자동으로 배경색을 바꾸는 것 허용
		self.rgb = str()


class Form(QWidget):
	def __init__(self):
		QWidget.__init__(self, flags=Qt.Widget)
		# 마우스 좌표 저장용 변수
		self.mouse_x = 0
		self.mouse_y = 0

		self.lb = Label(self)
		self.properties_list = (
			"width", "height", "x", "y", "geometry",
			"maximumHeight", "maximumWidth", "maximumSize", "minimumSize", "minimumWidth",
			"size", "windowFilePath", "windowTitle",
			"underMouse"
		)  # 출력할 property 이름
		self.rgb_value = ''

		self.init_widget()
		self.show()

	def init_widget(self):
		self.setWindowTitle("Hello World")
		self.setGeometry(100, 100, 640, 480)  # 창 위치, 크기 설정
		self.setMouseTracking(True)  # 마우스 움직임을 캐치

		# QLabel 을 상속받은 Label인스턴스 생성
		# 인자값으로 parent인 self 지정

		msg = self.get_properties_value(self.properties_list)  # property 이름과 값을 돌려주는 함수 호출
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
		msg.append("{:>20s} : {:<30s}".format("mouse_x", str(self.mouse_x)))
		msg.append("{:>20s} : {:<30s}".format("mouse_y", str(self.mouse_y)))
		msg.append("{:>20s} : {:<30s}".format("label", self.rgb_value))
		msg = "\n".join(msg)
		return msg

	def mouseMoveEvent(self, QMouseEvent):
		"""
		위젯 안에서의 마우스 움직임이 일어날 때 호출
		"""
		self.mouse_x = QMouseEvent.x()
		self.mouse_y = QMouseEvent.y()
		self.set_widget_bgcolor(self.lb, self.mouse_x, self.mouse_y)
		self.update()

	def set_widget_bgcolor(self, widget, mx, my):
		"""
		파라메터로 받은 위젯의 색을 바꿔준다.
		"""
		if not isinstance(widget, QWidget):
			return False
		lw = widget.width()
		lh = widget.height()
		if (lw < mx) or (lh <my):
			return False

		v = int(sqrt(mx ** 2 + my ** 2))
		r = int(sqrt(lw ** 2 + lh ** 2))
		r = int(v/r * 255)
		g = int(mx / lw * 255)
		b = int(my / lh * 255)
		pal = QPalette()
		pal.setColor(QPalette.Background, QColor(r, g, b))
		widget.setPalette(pal)
		self.rgb_value = "r{0},g{1},b{0}".format(r, g, b)

	def moveEvent(self, QMoveEvent):
		"""
		창이 이동했을 경우(이동 중 아님.) 호출
		:param QMoveEvent:
		:return:
		"""
		self.update()

	def paintEvent(self, QPaintEvent):
		"""
		창을 다시 그려야 할 때 호출
		:param QPaintEvent:
		:return:
		"""
		msg = self.get_properties_value(self.properties_list)
		self.lb.setText(msg)  # Label에 텍스트 설정


if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	exit(app.exec_())
