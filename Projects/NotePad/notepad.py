#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# 윈도우 메모장(NotePad) 만들기

import sys

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTranslator
from PyQt5.QtCore import QLocale
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QEvent

from notepad_menubar import MenuBarWidget
from notepad_texteditor import TextEditor

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self, flags=Qt.Window)
		self.menu = MenuBarWidget()
		self.editor = TextEditor()
		self.translator = QTranslator()  # I18N 관련
		self.change_locale("translate\\" + QLocale.system().name() + ".qm")  # 시스템 로케일 사용
		self.filename = self.tr("untitled")
		self.init_window()

	def init_window(self):
		"""
		현재 위젯의 모양등을 초기화
		"""
		self.set_window_title()
		self.resize(640, 480)
		self.setWindowIcon(QIcon("notepad.ico"))
		self.setMenuBar(self.menu)
		self.setCentralWidget(self.editor)

	def set_window_title(self):
		"""
		윈도우 타이틀 변경
		:return:
		"""
		self.setWindowTitle("{} - {}".format(self.filename, self.tr("Notepad")))

	def change_locale(self, filename):
		"""
		번역파일을 받아서 로드
		:param filename:
		:return:
		"""
		global app
		app.removeTranslator(self.translator)
		self.translator.load(filename)
		app.installTranslator(self.translator)

	def retranslate_ui(self):
		self.set_window_title()
		self.menu.retranslate_ui()

	def changeEvent(self, event):
		"""
		언어가 바뀜을 감시
		:param event:
		:return:
		"""
		# 들어온 이벤트 중 언어가 바뀌었는지 검사
		if event.type() == QEvent.LanguageChange:
			self.retranslate_ui()
		QMainWindow.changeEvent(self, event)  # 나머지 일을 할 수 있게 넘겨줌


if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())