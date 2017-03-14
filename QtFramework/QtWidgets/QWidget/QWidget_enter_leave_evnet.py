# coding: utf-8

import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt


class IconWidget(QLabel):
	def __init__(self, parent=None):
		super(IconWidget, self).__init__(parent)
		color = "yellow"
		self.setStyleSheet("background-color: %s" % color)  # 라벨위젯과의 구분을 위한 색

	def enterEvent(self, event):
		self.raise_()

	def leaveEvent(self, event):
		self.lower()

class Dock(QWidget):
	def __init__(self, parent=None):
		super(Dock, self).__init__(parent, flags=Qt.Widget)
		self.default_interval = 10
		self.default_width = 100
		self.default_height = 100
		self.icons = []

	def _create_icon(self, n=10):
		self.icons = [IconWidget() for _ in range(n)]


class Form(QWidget):
	def __init__(self):
		QWidget.__init__(self, flags=Qt.Widget)
		self.setWindowTitle("Widget raise and lower")

		self.lb1 = TestWidget("red", parent=self)
		self.lb1.setGeometry(10, 10, 100, 100)

		self.lb2 = TestWidget("pink", parent=self)
		self.lb2.setGeometry(40, 40, 100, 100)

		self.lb3 = TestWidget("yellow", parent=self)
		self.lb3.setGeometry(70, 70, 100, 100)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())