#!/usr/bin/env python
# coding: utf-8

from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import pyqtSlot


class StatusBar(QStatusBar):
    @pyqtSlot(QTextCursor)
    def __init__(self):
        QStatusBar.__init__(self)
        self.setVisible(False)

    def change_cursor_info(self, data:QTextCursor):
        ss = data.selectionStart()
        se = data.selectionEnd()

        selected_info = ""
        if se - ss:
            selected_info = "{0} {1}  ".format(se - ss, "char" if (se-ss) == 1 else "chars")
        self.showMessage("{0}{1}:{2}".format(
            selected_info,
            data.blockNumber(),
            data.columnNumber())
        )

