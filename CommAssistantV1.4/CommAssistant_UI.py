# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CommAssistant.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(735, 621)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(306, 551))
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Form.setBaseSize(QtCore.QSize(0, 0))
        Form.setMouseTracking(True)
        Form.setAcceptDrops(False)
        Form.setAutoFillBackground(False)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.TitleBar = QtWidgets.QWidget(Form)
        self.TitleBar.setMinimumSize(QtCore.QSize(0, 41))
        self.TitleBar.setMaximumSize(QtCore.QSize(16777215, 41))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        self.TitleBar.setFont(font)
        self.TitleBar.setMouseTracking(True)
        self.TitleBar.setStyleSheet("#TitleBar\n"
"{\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.TitleBar.setObjectName("TitleBar")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.TitleBar)
        self.horizontalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_10.setSpacing(15)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.TitleIcon = QtWidgets.QLabel(self.TitleBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleIcon.sizePolicy().hasHeightForWidth())
        self.TitleIcon.setSizePolicy(sizePolicy)
        self.TitleIcon.setMinimumSize(QtCore.QSize(25, 25))
        self.TitleIcon.setMaximumSize(QtCore.QSize(25, 25))
        self.TitleIcon.setStyleSheet("border-image: url(C:/images/title_icon.png)")
        self.TitleIcon.setText("")
        self.TitleIcon.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.TitleIcon.setObjectName("TitleIcon")
        self.horizontalLayout_10.addWidget(self.TitleIcon)
        self.TitleName = QtWidgets.QLabel(self.TitleBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleName.sizePolicy().hasHeightForWidth())
        self.TitleName.setSizePolicy(sizePolicy)
        self.TitleName.setMaximumSize(QtCore.QSize(210, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.TitleName.setFont(font)
        self.TitleName.setMouseTracking(True)
        self.TitleName.setTabletTracking(False)
        self.TitleName.setStyleSheet("color: rgb(255, 255, 255);")
        self.TitleName.setObjectName("TitleName")
        self.horizontalLayout_10.addWidget(self.TitleName)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.MinimizeButton = QtWidgets.QPushButton(self.TitleBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MinimizeButton.sizePolicy().hasHeightForWidth())
        self.MinimizeButton.setSizePolicy(sizePolicy)
        self.MinimizeButton.setMinimumSize(QtCore.QSize(25, 25))
        self.MinimizeButton.setMaximumSize(QtCore.QSize(25, 25))
        self.MinimizeButton.setStyleSheet("QPushButton{\n"
"            border-image: url(C:/images/minimize_first.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"            border-image: url(C:/images/minimize_latter.png);\n"
"}\n"
"")
        self.MinimizeButton.setText("")
        self.MinimizeButton.setObjectName("MinimizeButton")
        self.horizontalLayout_10.addWidget(self.MinimizeButton)
        self.MaximizeButton = QtWidgets.QPushButton(self.TitleBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MaximizeButton.sizePolicy().hasHeightForWidth())
        self.MaximizeButton.setSizePolicy(sizePolicy)
        self.MaximizeButton.setMinimumSize(QtCore.QSize(0, 0))
        self.MaximizeButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.MaximizeButton.setAutoFillBackground(False)
        self.MaximizeButton.setStyleSheet("QPushButton{\n"
"    border-image: url(C:/images/maximize_first.png);\n"
"    width: 25px;\n"
"    height:25px\n"
"}\n"
"\n"
"QPushButton:hover{border-image: url(C:/images/maximize_latter.png);}\n"
"")
        self.MaximizeButton.setText("")
        self.MaximizeButton.setObjectName("MaximizeButton")
        self.horizontalLayout_10.addWidget(self.MaximizeButton)
        self.CloseButton = QtWidgets.QPushButton(self.TitleBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(sizePolicy)
        self.CloseButton.setMinimumSize(QtCore.QSize(25, 25))
        self.CloseButton.setMaximumSize(QtCore.QSize(25, 25))
        self.CloseButton.setStyleSheet("QPushButton{\n"
"            border-image: url(C:/images/close_first.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"            border-image: url(C:/images/close_latter.png);\n"
"}\n"
"")
        self.CloseButton.setText("")
        self.CloseButton.setObjectName("CloseButton")
        self.horizontalLayout_10.addWidget(self.CloseButton)
        self.verticalLayout_4.addWidget(self.TitleBar)
        self.MainBackgroud = QtWidgets.QWidget(Form)
        self.MainBackgroud.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.MainBackgroud.setMouseTracking(True)
        self.MainBackgroud.setStyleSheet("#MainBackgroud\n"
"{\n"
"    background-color: rgb(62, 62, 62);\n"
"}")
        self.MainBackgroud.setObjectName("MainBackgroud")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.MainBackgroud)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.ReceiveEdit = QtWidgets.QTextEdit(self.MainBackgroud)
        self.ReceiveEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.ReceiveEdit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ReceiveEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.ReceiveEdit.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.ReceiveEdit.setTabChangesFocus(False)
        self.ReceiveEdit.setUndoRedoEnabled(False)
        self.ReceiveEdit.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.ReceiveEdit.setReadOnly(True)
        self.ReceiveEdit.setOverwriteMode(False)
        self.ReceiveEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.ReceiveEdit.setPlaceholderText("")
        self.ReceiveEdit.setObjectName("ReceiveEdit")
        self.horizontalLayout_8.addWidget(self.ReceiveEdit)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.SerialCOMLabel = QtWidgets.QLabel(self.MainBackgroud)
        self.SerialCOMLabel.setMaximumSize(QtCore.QSize(75, 20))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(10)
        self.SerialCOMLabel.setFont(font)
        self.SerialCOMLabel.setObjectName("SerialCOMLabel")
        self.verticalLayout.addWidget(self.SerialCOMLabel)
        self.SerialCOMComboBox = QtWidgets.QComboBox(self.MainBackgroud)
        self.SerialCOMComboBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SerialCOMComboBox.sizePolicy().hasHeightForWidth())
        self.SerialCOMComboBox.setSizePolicy(sizePolicy)
        self.SerialCOMComboBox.setMaximumSize(QtCore.QSize(218, 16777215))
        self.SerialCOMComboBox.setCurrentText("")
        self.SerialCOMComboBox.setObjectName("SerialCOMComboBox")
        self.verticalLayout.addWidget(self.SerialCOMComboBox)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 4, -1, -1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.SerialBaudRateLabel = QtWidgets.QLabel(self.MainBackgroud)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SerialBaudRateLabel.sizePolicy().hasHeightForWidth())
        self.SerialBaudRateLabel.setSizePolicy(sizePolicy)
        self.SerialBaudRateLabel.setMaximumSize(QtCore.QSize(74, 30))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(10)
        self.SerialBaudRateLabel.setFont(font)
        self.SerialBaudRateLabel.setObjectName("SerialBaudRateLabel")
        self.horizontalLayout_3.addWidget(self.SerialBaudRateLabel)
        self.SerialBaudRateComboBox = QtWidgets.QComboBox(self.MainBackgroud)
        self.SerialBaudRateComboBox.setMaximumSize(QtCore.QSize(113, 23))
        self.SerialBaudRateComboBox.setEditable(False)
        self.SerialBaudRateComboBox.setObjectName("SerialBaudRateComboBox")
        self.SerialBaudRateComboBox.addItem("")
        self.SerialBaudRateComboBox.addItem("")
        self.SerialBaudRateComboBox.addItem("")
        self.SerialBaudRateComboBox.addItem("")
        self.SerialBaudRateComboBox.addItem("")
        self.SerialBaudRateComboBox.addItem("")
        self.SerialBaudRateComboBox.addItem("")
        self.SerialBaudRateComboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.SerialBaudRateComboBox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 4, -1, -1)
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.SerialStopBitsLabel = QtWidgets.QLabel(self.MainBackgroud)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SerialStopBitsLabel.sizePolicy().hasHeightForWidth())
        self.SerialStopBitsLabel.setSizePolicy(sizePolicy)
        self.SerialStopBitsLabel.setMaximumSize(QtCore.QSize(74, 30))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(10)
        self.SerialStopBitsLabel.setFont(font)
        self.SerialStopBitsLabel.setObjectName("SerialStopBitsLabel")
        self.horizontalLayout_4.addWidget(self.SerialStopBitsLabel)
        self.SerialStopBitsComboBox = QtWidgets.QComboBox(self.MainBackgroud)
        self.SerialStopBitsComboBox.setMaximumSize(QtCore.QSize(113, 23))
        self.SerialStopBitsComboBox.setObjectName("SerialStopBitsComboBox")
        self.SerialStopBitsComboBox.addItem("")
        self.SerialStopBitsComboBox.addItem("")
        self.SerialStopBitsComboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.SerialStopBitsComboBox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, 4, -1, -1)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.SerialDataBitsLabel = QtWidgets.QLabel(self.MainBackgroud)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SerialDataBitsLabel.sizePolicy().hasHeightForWidth())
        self.SerialDataBitsLabel.setSizePolicy(sizePolicy)
        self.SerialDataBitsLabel.setMaximumSize(QtCore.QSize(74, 30))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(10)
        self.SerialDataBitsLabel.setFont(font)
        self.SerialDataBitsLabel.setObjectName("SerialDataBitsLabel")
        self.horizontalLayout_5.addWidget(self.SerialDataBitsLabel)
        self.SerialDataBitsComboBox = QtWidgets.QComboBox(self.MainBackgroud)
        self.SerialDataBitsComboBox.setMaximumSize(QtCore.QSize(113, 23))
        self.SerialDataBitsComboBox.setObjectName("SerialDataBitsComboBox")
        self.SerialDataBitsComboBox.addItem("")
        self.SerialDataBitsComboBox.addItem("")
        self.SerialDataBitsComboBox.addItem("")
        self.SerialDataBitsComboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.SerialDataBitsComboBox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 4, -1, -1)
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.SerialParityLabel = QtWidgets.QLabel(self.MainBackgroud)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SerialParityLabel.sizePolicy().hasHeightForWidth())
        self.SerialParityLabel.setSizePolicy(sizePolicy)
        self.SerialParityLabel.setMaximumSize(QtCore.QSize(74, 30))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(10)
        self.SerialParityLabel.setFont(font)
        self.SerialParityLabel.setObjectName("SerialParityLabel")
        self.horizontalLayout_6.addWidget(self.SerialParityLabel)
        self.SerialParityComboBox = QtWidgets.QComboBox(self.MainBackgroud)
        self.SerialParityComboBox.setMaximumSize(QtCore.QSize(113, 23))
        self.SerialParityComboBox.setToolTipDuration(0)
        self.SerialParityComboBox.setMaxVisibleItems(10)
        self.SerialParityComboBox.setObjectName("SerialParityComboBox")
        self.SerialParityComboBox.addItem("")
        self.SerialParityComboBox.addItem("")
        self.SerialParityComboBox.addItem("")
        self.horizontalLayout_6.addWidget(self.SerialParityComboBox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 4, -1, 0)
        self.horizontalLayout_7.setSpacing(3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.OpenLabel = QtWidgets.QLabel(self.MainBackgroud)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OpenLabel.sizePolicy().hasHeightForWidth())
        self.OpenLabel.setSizePolicy(sizePolicy)
        self.OpenLabel.setMaximumSize(QtCore.QSize(74, 30))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(10)
        self.OpenLabel.setFont(font)
        self.OpenLabel.setObjectName("OpenLabel")
        self.horizontalLayout_7.addWidget(self.OpenLabel)
        self.OpenButton = QtWidgets.QPushButton(self.MainBackgroud)
        self.OpenButton.setMaximumSize(QtCore.QSize(113, 31))
        self.OpenButton.setObjectName("OpenButton")
        self.horizontalLayout_7.addWidget(self.OpenButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.verticalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 12, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.RefreshComButton = QtWidgets.QPushButton(self.MainBackgroud)
        self.RefreshComButton.setMinimumSize(QtCore.QSize(81, 28))
        self.RefreshComButton.setMaximumSize(QtCore.QSize(81, 28))
        self.RefreshComButton.setObjectName("RefreshComButton")
        self.horizontalLayout.addWidget(self.RefreshComButton)
        self.ClearReceiveButton = QtWidgets.QPushButton(self.MainBackgroud)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ClearReceiveButton.sizePolicy().hasHeightForWidth())
        self.ClearReceiveButton.setSizePolicy(sizePolicy)
        self.ClearReceiveButton.setMaximumSize(QtCore.QSize(81, 28))
        self.ClearReceiveButton.setObjectName("ClearReceiveButton")
        self.horizontalLayout.addWidget(self.ClearReceiveButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, 12, -1, -1)
        self.horizontalLayout_9.setSpacing(7)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setSpacing(7)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.HexDisplayCheckBox = QtWidgets.QCheckBox(self.MainBackgroud)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HexDisplayCheckBox.sizePolicy().hasHeightForWidth())
        self.HexDisplayCheckBox.setSizePolicy(sizePolicy)
        self.HexDisplayCheckBox.setMaximumSize(QtCore.QSize(18, 16777215))
        self.HexDisplayCheckBox.setStyleSheet("")
        self.HexDisplayCheckBox.setText("")
        self.HexDisplayCheckBox.setObjectName("HexDisplayCheckBox")
        self.horizontalLayout_19.addWidget(self.HexDisplayCheckBox)
        self.label = QtWidgets.QLabel(self.MainBackgroud)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout_19.addWidget(self.label, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setSpacing(7)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.TimeShowCheckBox = QtWidgets.QCheckBox(self.MainBackgroud)
        self.TimeShowCheckBox.setMaximumSize(QtCore.QSize(17, 16777215))
        self.TimeShowCheckBox.setText("")
        self.TimeShowCheckBox.setObjectName("TimeShowCheckBox")
        self.horizontalLayout_18.addWidget(self.TimeShowCheckBox, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.label_5 = QtWidgets.QLabel(self.MainBackgroud)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_18.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_18)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_8.addLayout(self.verticalLayout_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SendEdit = QtWidgets.QTextEdit(self.MainBackgroud)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SendEdit.sizePolicy().hasHeightForWidth())
        self.SendEdit.setSizePolicy(sizePolicy)
        self.SendEdit.setMinimumSize(QtCore.QSize(168, 79))
        self.SendEdit.setMaximumSize(QtCore.QSize(16777215, 100))
        self.SendEdit.setObjectName("SendEdit")
        self.horizontalLayout_2.addWidget(self.SendEdit)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(36)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.SendButton = QtWidgets.QPushButton(self.MainBackgroud)
        self.SendButton.setMinimumSize(QtCore.QSize(90, 0))
        self.SendButton.setMaximumSize(QtCore.QSize(113, 30))
        self.SendButton.setObjectName("SendButton")
        self.verticalLayout_3.addWidget(self.SendButton)
        self.ClearSendButton = QtWidgets.QPushButton(self.MainBackgroud)
        self.ClearSendButton.setMinimumSize(QtCore.QSize(90, 0))
        self.ClearSendButton.setMaximumSize(QtCore.QSize(113, 30))
        self.ClearSendButton.setObjectName("ClearSendButton")
        self.verticalLayout_3.addWidget(self.ClearSendButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.SendBlankCheckBox = QtWidgets.QCheckBox(self.MainBackgroud)
        self.SendBlankCheckBox.setStyleSheet("")
        self.SendBlankCheckBox.setText("")
        self.SendBlankCheckBox.setObjectName("SendBlankCheckBox")
        self.horizontalLayout_14.addWidget(self.SendBlankCheckBox)
        self.label_2 = QtWidgets.QLabel(self.MainBackgroud)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_14.addWidget(self.label_2)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.HexSendCheckBox = QtWidgets.QCheckBox(self.MainBackgroud)
        self.HexSendCheckBox.setStyleSheet("")
        self.HexSendCheckBox.setText("")
        self.HexSendCheckBox.setObjectName("HexSendCheckBox")
        self.horizontalLayout_12.addWidget(self.HexSendCheckBox)
        self.label_3 = QtWidgets.QLabel(self.MainBackgroud)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_12.addWidget(self.label_3)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_12)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.verticalLayout_4.addWidget(self.MainBackgroud)
        self.BottomBar = QtWidgets.QWidget(Form)
        self.BottomBar.setMaximumSize(QtCore.QSize(16777215, 29))
        self.BottomBar.setMouseTracking(True)
        self.BottomBar.setStyleSheet("background-color: rgb(85, 0, 127);")
        self.BottomBar.setObjectName("BottomBar")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.BottomBar)
        self.horizontalLayout_16.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(26)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.ReceiveNumlabel = QtWidgets.QLabel(self.BottomBar)
        self.ReceiveNumlabel.setMinimumSize(QtCore.QSize(120, 0))
        self.ReceiveNumlabel.setMaximumSize(QtCore.QSize(120, 16777215))
        self.ReceiveNumlabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.ReceiveNumlabel.setObjectName("ReceiveNumlabel")
        self.horizontalLayout_11.addWidget(self.ReceiveNumlabel)
        self.SendNumlabel = QtWidgets.QLabel(self.BottomBar)
        self.SendNumlabel.setMinimumSize(QtCore.QSize(120, 0))
        self.SendNumlabel.setMaximumSize(QtCore.QSize(100, 16777215))
        self.SendNumlabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.SendNumlabel.setObjectName("SendNumlabel")
        self.horizontalLayout_11.addWidget(self.SendNumlabel)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_11)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem3)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(26)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_4 = QtWidgets.QLabel(self.BottomBar)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_13.addWidget(self.label_4)
        self.Timelabel = QtWidgets.QLabel(self.BottomBar)
        self.Timelabel.setMaximumSize(QtCore.QSize(141, 16777215))
        self.Timelabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.Timelabel.setObjectName("Timelabel")
        self.horizontalLayout_13.addWidget(self.Timelabel)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_13)
        self.verticalLayout_4.addWidget(self.BottomBar)
        self.BottomBar.raise_()
        self.TitleBar.raise_()
        self.MainBackgroud.raise_()

        self.retranslateUi(Form)
        self.SerialParityComboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "SEGCOM"))
        self.TitleName.setText(_translate("Form", "串口助手 Beta V1.0"))
        self.ReceiveEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.SerialCOMLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">串口选择</span></p></body></html>"))
        self.SerialBaudRateLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">波特率</span></p></body></html>"))
        self.SerialBaudRateComboBox.setItemText(0, _translate("Form", "115200"))
        self.SerialBaudRateComboBox.setItemText(1, _translate("Form", "57600"))
        self.SerialBaudRateComboBox.setItemText(2, _translate("Form", "19200"))
        self.SerialBaudRateComboBox.setItemText(3, _translate("Form", "9600"))
        self.SerialBaudRateComboBox.setItemText(4, _translate("Form", "4800"))
        self.SerialBaudRateComboBox.setItemText(5, _translate("Form", "2400"))
        self.SerialBaudRateComboBox.setItemText(6, _translate("Form", "1200"))
        self.SerialBaudRateComboBox.setItemText(7, _translate("Form", "自定义"))
        self.SerialStopBitsLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">停止位</span></p></body></html>"))
        self.SerialStopBitsComboBox.setItemText(0, _translate("Form", "1"))
        self.SerialStopBitsComboBox.setItemText(1, _translate("Form", "1.5"))
        self.SerialStopBitsComboBox.setItemText(2, _translate("Form", "2"))
        self.SerialDataBitsLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">数据位</span></p></body></html>"))
        self.SerialDataBitsComboBox.setItemText(0, _translate("Form", "8"))
        self.SerialDataBitsComboBox.setItemText(1, _translate("Form", "7"))
        self.SerialDataBitsComboBox.setItemText(2, _translate("Form", "6"))
        self.SerialDataBitsComboBox.setItemText(3, _translate("Form", "5"))
        self.SerialParityLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">奇偶校验</span></p></body></html>"))
        self.SerialParityComboBox.setItemText(0, _translate("Form", "无校验"))
        self.SerialParityComboBox.setItemText(1, _translate("Form", "奇校验"))
        self.SerialParityComboBox.setItemText(2, _translate("Form", "偶校验"))
        self.OpenLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">串口操作</span></p></body></html>"))
        self.OpenButton.setText(_translate("Form", "打开串口"))
        self.RefreshComButton.setText(_translate("Form", "刷新串口"))
        self.ClearReceiveButton.setText(_translate("Form", "清除接收"))
        self.label.setText(_translate("Form", "Hex显示"))
        self.label_5.setText(_translate("Form", "时间戳"))
        self.SendButton.setText(_translate("Form", "发送"))
        self.ClearSendButton.setText(_translate("Form", "清除发送"))
        self.label_2.setText(_translate("Form", "发送新行"))
        self.label_3.setText(_translate("Form", "Hex发送"))
        self.ReceiveNumlabel.setText(_translate("Form", "<html><head/><body><p>Receive: 129</p></body></html>"))
        self.SendNumlabel.setText(_translate("Form", "<html><head/><body><p>Send: 100</p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p>Author:ZJW</p></body></html>"))
        self.Timelabel.setText(_translate("Form", "<html><head/><body><p>当前时间 11:08:26</p></body></html>"))
