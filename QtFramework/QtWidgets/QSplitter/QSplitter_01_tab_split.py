#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * 기본 위젯을 사용하여 기본 창을 생성
# * '창 이름'을 변경한다.

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QSplitter
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QPushButton

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QTabWidget

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QWidget):
    """
    만들고자 하는 프로그램의 기본이 되는 창 또는 폼 위젯.
    본 위젯 위에 다른 위젯을 올려서 모양을 만든다.

    QWidget을 상속받아서 필요한 메소드를 작성.
    """

    def __init__(self):
        """
        보통 __init__ (생성자)에서 필요한 것들을 다를 위젯들을 선언해줘도 되지만 init_widget을 따로 만들어서 호출한다.
        """
        QWidget.__init__(self, flags=Qt.Widget)

        self.te_1 = QTextEdit("1")
        self.te_2 = QTextEdit("2")
        self.te_3 = QTextEdit("3")
        self.pb = QPushButton("->")

        # 이 Splitter에 속한 위젯들은 Splitter Handler에 의해
        # 겹치기 및 크기 조절이 가능해 진다.
        self.splits = QSplitter()
        self.splits.setOrientation(Qt.Horizontal)

        self.tabs = list()

        # 전체 레이아웃
        self.vbox = QBoxLayout(QBoxLayout.TopToBottom)
        self.init_widget()

    def init_widget(self):
        """
        현재 위젯의 모양등을 초기화
        """
        self.setWindowTitle("Splitter")

        # 한 개의 탭을 생성하여 위젯을 담는다.
        self.tabs.append(QTabWidget())
        self.tabs[0].addTab(self.te_1,"1")
        self.tabs[0].addTab(self.te_2,"2")
        self.tabs[0].addTab(self.te_3,"3")

        # 생성한 탭을 Splitter에 등록
        self.splits.addWidget(self.tabs[0])
        # 전체 레이아웃에 위젯 등록
        self.vbox.addWidget(self.splits)
        self.vbox.addWidget(self.pb)
        self.setLayout(self.vbox)

        self.pb.clicked.connect(self.split)

    def split(self):
        if 1 == len(self.tabs[0]):
            return
        # '첫번째 탭 위젯'에서 현제 선택된 위젯의 인덱스와 이름을 가져온다.
        name = self.tabs[0].tabText(self.tabs[0].currentIndex())
        widget = self.tabs[0].currentWidget()
        # '새로운 탭 위젯'을 생성하고 이동시킬 위젯을 새 탭으로 넣는다.
        self.tabs.append(QTabWidget())
        self.tabs[-1].addTab(widget, name)
        # '새로 생성한 탭 위젯'을 Splitter에 추가
        self.splits.addWidget(self.tabs[-1])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
