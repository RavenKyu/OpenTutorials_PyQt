#!/usr/bin/env python
# coding: utf-8

# Serial 설정과 동작을 관리하는 모듈

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtSerialPort import QSerialPort
from PyQt5.QtSerialPort import QSerialPortInfo
from PyQt5.QtCore import QIODevice

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal

__author__ = "Deokyu Lim <hong18s@gmail.com>"
__platform__ = sys.platform

class SerialControler(QWidget):
    BAUDRATES = (
        QSerialPort.Baud1200,
        QSerialPort.Baud2400,
        QSerialPort.Baud4800,
        QSerialPort.Baud9600,
        QSerialPort.Baud19200,
        QSerialPort.Baud38400,
        QSerialPort.Baud57600,
        QSerialPort.Baud115200,
    )

    DATABITS = (
        QSerialPort.Data5,
        QSerialPort.Data6,
        QSerialPort.Data7,
        QSerialPort.Data8,
    )

    FLOWCONTROL = (
        QSerialPort.NoFlowControl,
        QSerialPort.HardwareControl,
        QSerialPort.SoftwareControl,
    )

    PARITY = (
        QSerialPort.NoParity,
        QSerialPort.EvenParity,
        QSerialPort.OddParity,
        QSerialPort.SpaceParity,
        QSerialPort.MarkParity,
    )

    STOPBITS = (
        QSerialPort.OneStop,
        QSerialPort.OneAndHalfStop,
        QSerialPort.TwoStop,

    )

    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.gb = QGroupBox(self.tr("Serial"))
        self.cb_port = QComboBox()
        self.cb_baud_rate = QComboBox()
        self.cb_data_bits = QComboBox()
        self.cb_flow_control = QComboBox()
        self.cb_parity = QComboBox()
        self.cb_stop_bits = QComboBox()

        self.serial = QSerialPort()
        self.serial_info = QSerialPortInfo()
        self.init_widget()


    def init_widget(self):
        self.setWindowTitle("Serial Controler")
        layout = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
        grid_box = QGridLayout()

        grid_box.addWidget(QLabel(self.tr("Port")), 0, 0)
        grid_box.addWidget(self.cb_port, 0, 1)

        grid_box.addWidget(QLabel(self.tr("Baud Rate")), 1, 0)
        grid_box.addWidget(self.cb_baud_rate, 1, 1)

        grid_box.addWidget(QLabel(self.tr("Data Bits")), 2, 0)
        grid_box.addWidget(self.cb_data_bits, 2, 1)

        grid_box.addWidget(QLabel(self.tr("Flow Control")), 3, 0)
        grid_box.addWidget(self.cb_flow_control, 3, 1)

        grid_box.addWidget(QLabel(self.tr("Parity")), 4, 0)
        grid_box.addWidget(self.cb_parity, 4, 1)

        grid_box.addWidget(QLabel(self.tr("Stop Bits")), 5, 0)
        grid_box.addWidget(self.cb_stop_bits, 5, 1)

        self._fill_serial_info()
        self.gb.setLayout(grid_box)
        layout.addWidget(self.gb)
        self.setLayout(layout)

    def _fill_serial_info(self):
        self.cb_port.insertItems(0, self._get_available_port())
        self.cb_baud_rate.insertItems(0, [str(x) for x in self.BAUDRATES])
        self.cb_data_bits.insertItems(0, [str(x) for x in self.DATABITS])
        flow_name = {0: "None", 1: "Hardware", 2: "Software"}
        self.cb_flow_control.insertItems(0, [flow_name[x] for x in self.FLOWCONTROL])
        parity_name = {0: "None", 2: "Even", 3: "Odd", 4: "Space", 5: "Mark"}
        self.cb_parity.insertItems(0, [parity_name[x] for x in self.PARITY])
        stop_bits_name = {1: "1", 3: "1.5", 2: "2"}
        self.cb_stop_bits.insertItems(0, [stop_bits_name[x] for x in self.STOPBITS])

    @staticmethod
    def get_port_path():
        """
        현재플래폼에 맞게 경로 또는 지정어를 반환
        :return:
        """
        return {"linux": '/dev/ttyS', "win32": 'COM'}[__platform__]

    def _get_available_port(self):
        """
        255개의 포트를 열고 닫으면서 사용가능한 포트를 찾아서 반환
        :return:
        """
        available_port = list()
        port_path = self.get_port_path()

        for number in range(255):
            port_name = port_path + str(number)
            if not self._open(port_name):
                continue
            available_port.append(port_name)
            self.serial.close()
        return available_port

    def _open(self, port_name, baudrate=QSerialPort.Baud9600, data_bits=QSerialPort.Data8,
              flow_control=QSerialPort.NoFlowControl, parity=QSerialPort.NoParity, stop_bits=QSerialPort.OneStop):
        """
        인자값으로 받은 시리얼 접속 정보를 이용하여 해당 포트를 연결한다.
        :param port_name:
        :param baudrate:
        :param data_bits:
        :param flow_control:
        :param parity:
        :param stop_bits:
        :return: bool
        """
        info = QSerialPortInfo(port_name)
        self.serial.setPort(info)
        self.serial.setBaudRate(baudrate)
        self.serial.setDataBits(data_bits)
        self.serial.setFlowControl(flow_control)
        self.serial.setParity(parity)
        self.serial.setStopBits(stop_bits)
        return self.serial.open(QIODevice.ReadWrite)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = SerialControler()
    form.show()
    exit(app.exec_())