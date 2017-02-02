#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * PaintEvent를 사용하여 실시간으로 값 변경하기
# * MouseEvent를 사용하여 마우스 값 가져오기

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QWidget):
	def __init__(self):
		QWidget.__init__(self, flags=Qt.Widget)
		# 마우스 좌표 저장용 변수
		self.mouse_x = 0
		self.mouse_y = 0

		self.lb = QLabel(self)

		self.properties_list = (
			"width", "height", "x", "y", "geometry",
			"maximumHeight", "maximumWidth", "maximumSize", "minimumSize", "minimumWidth",
			"size", "windowFilePath", "windowTitle",
			"underMouse"
		)  # 출력할 property 이름

		self.init_widget()

	def init_widget(self):
		self.setWindowTitle("Hello World")
		self.setGeometry(100, 100, 640, 480)  # 창 위치, 크기 설정
		self.setMouseTracking(True)  # 마우스 움직임을 캐치

		# QLabel 인스턴스 생성
		# 인자값으로 parent인 self 지정
		# QLabel(str, parent), QLabel(parent) 등으로 줄 수 있음
		self.lb.setStyleSheet("background-color: yellow")  # 라벨위젯과의 구분을 위한 색
		self.lb.setMouseTracking(True)  # False 값일 경우 Label 위젯에서는 mouse 이벤트가 발생하지 않는다.
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
		msg = "\n".join(msg)
		return msg

	def mouseMoveEvent(self, QMouseEvent):
		"""
		위젯 안에서의 마우스 움직임이 일어날 때 호출
		:param QMouseEvent:
		:return:
		"""
		self.mouse_x = QMouseEvent.x()
		self.mouse_y = QMouseEvent.y()
		self.update()

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
		"""
		msg = self.get_properties_value(self.properties_list)
		self.lb.setText(msg)  # Label에 텍스트 설정


if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())
