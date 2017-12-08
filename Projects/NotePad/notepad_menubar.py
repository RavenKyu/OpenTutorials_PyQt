#!/usr/bin/env python
# coding: utf-8

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtGui import QKeySequence

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class MenuBarWidget(QMenuBar):
    sig_new_file = pyqtSignal()
    sig_open_file = pyqtSignal()
    sig_save_file = pyqtSignal()
    sig_page_setup = pyqtSignal()
    sig_print = pyqtSignal()
    sig_exit = pyqtSignal()
    sig_status_bar = pyqtSignal(bool)

    def __init__(self):
        QMenuBar.__init__(self)
        self.init_menu_file()
        self.init_menu_edit()
        self.init_menu_format()
        self.init_menu_view()
        self.init_menu_help()
        self.set_all_text()

    def init_menu_file(self):
        # Action 설정
        # 새 파일
        self.act_new_file = QAction(self)
        self.act_new_file.setShortcut(QKeySequence('Ctrl+N'))
        self.act_new_file.triggered.connect(lambda : self.sig_new_file.emit())
        # self.act_new_file.triggered.emmit(self.slot_new)
        # 열기
        self.act_open_file = QAction(self)
        self.act_open_file.setShortcut(QKeySequence('Ctrl+O'))
        self.act_open_file.triggered.connect(lambda : self.sig_open_file.emit())
        # 저장
        self.act_save_file = QAction(self)
        self.act_save_file.setShortcut(QKeySequence('Ctrl+S'))
        self.act_save_file.triggered.connect(lambda : self.sig_save_file.emit())
        # 다른 이름으로 저장
        self.act_save_as_file = QAction(self)
        self.act_save_as_file.triggered.connect(self.slot_save_as)
        # 페이지 설정
        self.act_page_setup = QAction(self)
        self.act_page_setup.setShortcut(QKeySequence('Ctrl+S'))
        self.act_page_setup.triggered.connect(lambda : self.sig_page_setup.emit())
        # 프린트
        self.act_print = QAction(self)
        self.act_print.setShortcut(QKeySequence('Ctrl+P'))
        self.act_print.triggered.connect(lambda : self.sig_print.emit())
        # 끝내기
        self.act_quit = QAction(self.tr('Exit') + "(&X)", self)
        self.act_quit.triggered.connect(lambda : self.sig_exit.emit())
        # 메뉴바 생성 및 액션 적용
        # addAction한 차례로 삽입

        self.menu_file = self.addMenu(self.tr("File") + "(&F)")
        self.menu_file.addAction(self.act_new_file)
        self.menu_file.addAction(self.act_open_file)
        self.menu_file.addAction(self.act_save_file)
        self.menu_file.addAction(self.act_save_as_file)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.act_page_setup)
        self.menu_file.addAction(self.act_print)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.act_quit)

    def init_menu_edit(self):
        # 실행취소
        self.act_undo = QAction(self)
        self.act_undo.setShortcut(QKeySequence('Ctrl+Z'))
        self.act_undo.triggered.connect(self.slot_undo)
        # 잘라내기
        self.act_cut = QAction(self)
        self.act_cut.setShortcut(QKeySequence('Ctrl+X'))
        self.act_cut.triggered.connect(self.slot_cut)
        # 복사
        self.act_copy = QAction(self)
        self.act_copy.setShortcut(QKeySequence('Ctrl+C'))
        self.act_copy.triggered.connect(self.slot_copy)
        # 붙여넣기
        self.act_paste = QAction(self)
        self.act_paste.setShortcut(QKeySequence('Ctrl+V'))
        self.act_paste.triggered.connect(self.slot_paste)
        # 삭제
        self.act_del = QAction(self)
        self.act_del.setShortcut(QKeySequence('Del'))
        self.act_del.triggered.connect(self.slot_del)
        # 찾기
        self.act_find = QAction(self)
        self.act_find.setShortcut(QKeySequence('Ctrl+F'))
        self.act_find.triggered.connect(self.slot_find)
        # 다음찾기
        self.act_find_next = QAction(self)
        self.act_find_next.setShortcut(QKeySequence('F3'))
        self.act_find_next.triggered.connect(self.slot_find_next)
        # 바꾸기
        self.act_replace = QAction(self)
        self.act_replace.setShortcut(QKeySequence('Ctrl+H'))
        self.act_replace.triggered.connect(self.slot_replace)
        # 이동
        self.act_go_to = QAction(self)
        self.act_go_to.setShortcut(QKeySequence('Ctrl+G'))
        self.act_go_to.triggered.connect(self.slot_go_to)
        # 모두선택
        self.act_select_all = QAction(self)
        self.act_select_all.setShortcut(QKeySequence('Ctrl+A'))
        self.act_select_all.triggered.connect(self.slot_select_all)
        # 시간날짜
        self.act_time_date = QAction(self)
        self.act_time_date.setShortcut(QKeySequence('F5'))
        self.act_time_date.triggered.connect(self.slot_time_date)

        self.menu_edit = self.addMenu(self.tr('Edit') + "(&E)")
        self.menu_edit.addAction(self.act_undo)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.act_cut)
        self.menu_edit.addAction(self.act_copy)
        self.menu_edit.addAction(self.act_paste)
        self.menu_edit.addAction(self.act_del)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.act_find)
        self.menu_edit.addAction(self.act_find_next)
        self.menu_edit.addAction(self.act_replace)
        self.menu_edit.addAction(self.act_go_to)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.act_select_all)
        self.menu_edit.addAction(self.act_time_date)

    def init_menu_format(self):
        # 자동 줄 바꾹
        self.act_word_wrap = QAction(self)
        self.act_word_wrap.triggered.connect(self.slot_word_wrap)
        # 글꼴
        self.act_font = QAction(self)
        self.act_font.triggered.connect(self.slot_font)

        self.menu_format = self.addMenu(self.tr('Format') + "(&O)")
        self.menu_format.addAction(self.act_word_wrap)
        self.menu_format.addAction(self.act_font)

    def init_menu_view(self):
        self.act_status_bar = QAction(self)
        self.act_status_bar.setCheckable(True)
        self.act_status_bar.triggered.connect(lambda : self.sig_status_bar.emit(self.act_status_bar.isChecked()))

        self.menu_view = self.addMenu(self.tr('View') + "(&V)")
        self.menu_view.addAction(self.act_status_bar)

    def init_menu_help(self):
        self.act_help = QAction(self)
        self.act_help.triggered.connect(self.slot_help)
        # 메모장 정보
        self.act_about = QAction(self)
        self.act_about.triggered.connect(self.slot_about)

        self.menu_help = self.addMenu(self.tr('Help') + "(&H)")
        self.menu_help.addAction(self.act_help)
        self.menu_help.addSeparator()
        self.menu_help.addAction(self.act_about)

    @pyqtSlot()
    def slot_save_as(self):
        pass

    @pyqtSlot()
    def slot_undo(self):
        pass

    @pyqtSlot()
    def slot_cut(self):
        pass

    @pyqtSlot()
    def slot_copy(self):
        pass

    @pyqtSlot()
    def slot_paste(self):
        pass

    @pyqtSlot()
    def slot_del(self):
        pass

    @pyqtSlot()
    def slot_find(self):
        pass

    @pyqtSlot()
    def slot_find_next(self):
        pass

    @pyqtSlot()
    def slot_replace(self):
        pass

    @pyqtSlot()
    def slot_go_to(self):
        pass

    @pyqtSlot()
    def slot_select_all(self):
        pass

    @pyqtSlot()
    def slot_time_date(self):
        pass

    @pyqtSlot()
    def slot_word_wrap(self):
        pass

    @pyqtSlot()
    def slot_font(self):
        pass

    @pyqtSlot()
    def slot_help(self):
        pass

    @pyqtSlot()
    def slot_about(self):
        pass

    def set_all_text(self):
        self.menu_file.setTitle(self.tr("File") + "(&F)")
        self.act_new_file.setText(self.tr('New') + "(&N)")
        self.act_open_file.setText(self.tr('Open...') + "(&O)")
        self.act_save_file.setText(self.tr('Save') + "(&S)")
        self.act_save_as_file.setText(self.tr('Save as...') + "(&A)")
        self.act_page_setup.setText(self.tr('Page Setup...') + "(&U)")
        self.act_print.setText(self.tr('Print...') + "(&P)")

        self.menu_edit.setTitle(self.tr('Edit') + "(&E)")
        self.act_undo.setText(self.tr('Undo'))
        self.act_cut.setText(self.tr('Cut'))
        self.act_copy.setText(self.tr('Copy'))
        self.act_paste.setText(self.tr('Paste'))
        self.act_del.setText(self.tr('Del'))
        self.act_find.setText(self.tr('Find...'))
        self.act_find_next.setText(self.tr('Find Next'))
        self.act_replace.setText(self.tr('Replace...'))
        self.act_go_to.setText(self.tr('Go To...'))
        self.act_select_all.setText(self.tr('Select All'))
        self.act_time_date.setText(self.tr('Time/Date'))

        self.menu_format.setTitle(self.tr('Format') + "(&O)")
        self.act_word_wrap.setText(self.tr('Word Wrap'))
        self.act_font.setText(self.tr('Font...'))

        self.menu_view.setTitle(self.tr('View') + "(&V)")
        self.act_status_bar.setText(self.tr('Status Bar'))

        self.menu_help.setTitle(self.tr('Help') + "(&H)")
        self.act_help.setText(self.tr('Help'))
        self.act_about.setText(self.tr('About'))

    def retranslate_ui(self):
        self.set_all_text()

if __name__ == "__main__":
    from PyQt5.QtWidgets import QMainWindow
    from PyQt5.QtCore import Qt


    class Form(QMainWindow):
        def __init__(self):
            QMainWindow.__init__(self, flags=Qt.Window)
            self.filename = "제목없음"
            self.init_window()

        def init_window(self):
            """
            현재 위젯의 모양등을 초기화
            """
            self.setWindowTitle("제목 없음 - 메모장")
            self.resize(640, 480)

            self.menu = MenuBarWidget()
            self.setMenuBar(self.menu)

    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())