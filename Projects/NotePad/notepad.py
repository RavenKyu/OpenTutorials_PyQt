#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# 윈도우 메모장(NotePad) 만들기

import sys
import codecs

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QTextDocument
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTranslator
from PyQt5.QtCore import QLocale
from PyQt5.QtCore import QEvent
from PyQt5.QtCore import pyqtSlot
from PyQt5.Qt import QDialog
from PyQt5.Qt import QPrintDialog
from PyQt5.Qt import QPageSetupDialog
from PyQt5.Qt import QPrinter

from notepad_menubar import MenuBarWidget
from notepad_texteditor import TextEditor
from notepad_statusbar import StatusBar

__author__ = "Deokyu Lim <hong18s@gmail.com>"

class Form(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, flags=Qt.Window)
        self.menu = MenuBarWidget()
        self.status_bar = StatusBar()
        self.editor = TextEditor()
        self.translator = QTranslator()  # I18N 관련
        self.filename = str()
        self.change_locale("translate\\" + QLocale.system().name() + ".qm")  # 시스템 로케일 사용

        self.document_prt = QPrinter()

        self.init_window()
        self.init_setting()

    def init_setting(self):
        # 초기설정
        # 시작시 아무런 수정사항이 없기 때문에 저장 버튼 비활성화
        self.filename = str()
        self.set_window_title()
        self.editor.clear()
        self.menu.act_save_file.setEnabled(False)
        # 새로만들기 또는 종료시 현재 저장상태를 확인 후 수행
        self.is_saved = True

    @pyqtSlot()
    def slot_contents_changed(self):
        self.is_saved = False
        self.menu.act_save_file.setEnabled(True)

    @pyqtSlot()
    def slot_new(self):
        """
        저장유무 확인 후 저장
        :return:
        """
        if not self.is_saved:
            reply = QMessageBox.information(
                self, self.tr("Save"), self.tr("작성한 내용을 저장하시겠습니까?"),
                QMessageBox.Save | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Save)
            if reply == QMessageBox.Save:
                if not self.slot_save():
                    return  # 도중 취소
            elif reply == QMessageBox.No:
                pass
            else:
                return  # 취소 버튼
        self.init_setting()


    @pyqtSlot()
    def slot_open(self):
        fdial = QFileDialog(self)
        fdial.setAcceptMode(QFileDialog.AcceptOpen)
        file_name = fdial.getOpenFileName(self, self.tr("Open File"), filter='*.txt')[0]
        if file_name == '':
            return False
        fd = open(file_name, "r")
        buf = fd.read()
        fd.close()
        self.editor.clear()
        self.editor.insertPlainText(buf)
        self.filename = file_name
        self.set_window_title()
        self.is_saved = True
        return True


    @pyqtSlot()
    def slot_save(self):
        buf = self.editor.toPlainText()  # 에디터에 작성된 글을 가져온다
        fdial = QFileDialog(self)
        fdial.setAcceptMode(QFileDialog.AcceptSave)
        file_name = self.filename
        if not self.filename:
            file_name = fdial.getSaveFileName(self, self.tr("Save File"), filter='*.txt')[0]
        if not file_name:
            return False
        fd = open(file_name, 'w')
        fd.write(buf)
        fd.close()
        self.filename = file_name
        self.menu.act_save_file.setEnabled(False)
        self.set_window_title()
        return True

    @pyqtSlot()
    def slot_page_setup(self):
        page_dialog = QPageSetupDialog(self.document_prt)
        if page_dialog.exec() != QDialog.Accepted:
            return
        self.document_prt = page_dialog.printer()

    @pyqtSlot()
    def slot_print(self):
        printer = QPrintDialog(self.document_prt)
        if printer.exec() != QDialog.Accepted:
            return
        doc = QTextDocument()
        doc.setPlainText(self.editor.toPlainText())
        doc.print(self.document_prt)

    @pyqtSlot()
    def slot_quit(self):
        pass

    @pyqtSlot(bool)
    def slot_status_bar(self, status):
        print(status)
        pass

    def init_window(self):
        """
        현재 위젯의 모양등을 초기화
        """
        self.set_window_title()
        self.resize(640, 480)
        self.setWindowIcon(QIcon("notepad.ico"))
        self.setMenuBar(self.menu)
        self.setCentralWidget(self.editor)
        self.setStatusBar(self.status_bar)
        self.init_signal()

    def init_signal(self):
        """
        위젯들 끼리의 시그널 슬롯 연결
        :return:
        """
        self.editor.textChanged.connect(self.slot_contents_changed)
        self.editor.cursorPositionChanged.connect(lambda: self.status_bar.change_cursor_info(self.editor.textCursor()))
        self.menu.sig_status_bar.connect(self.status_bar.setVisible)
        self.menu.sig_new_file.connect(self.slot_new)
        self.menu.sig_open_file.connect(self.slot_open)
        self.menu.sig_save_file.connect(self.slot_save)
        self.menu.sig_page_setup.connect(self.slot_page_setup)
        self.menu.sig_print.connect(self.slot_print)
        self.menu.sig_status_bar.connect(self.slot_status_bar)


    def set_window_title(self):
        """
        윈도우 타이틀 변경
        :return:
        """
        filename = self.filename
        if not self.filename:
            filename = self.tr("untitled")
        else:
            filename = filename[filename.rfind('/') + 1:]
        self.setWindowTitle("{} - {}".format(filename, self.tr("Notepad")))

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