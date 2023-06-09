# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QButtonGroup


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.msgTypeButtonGroup = QButtonGroup(self)
        self.msgAudienceButtonGroup = QButtonGroup(self)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(632, 510)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 50))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.msgButton = QtWidgets.QRadioButton(self.centralwidget)
        self.msgButton.setObjectName("msgButton")
        self.gridLayout.addWidget(self.msgButton, 1, 0, 1, 1)
        self.imgButton = QtWidgets.QRadioButton(self.centralwidget)
        self.imgButton.setObjectName("imgButton")
        self.gridLayout.addWidget(self.imgButton, 2, 0, 1, 1)
        self.msgTypeButtonGroup.addButton(self.msgButton)
        self.msgTypeButtonGroup.addButton(self.imgButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.individualButton = QtWidgets.QRadioButton(self.centralwidget)
        self.individualButton.setObjectName("individualButton")
        self.gridLayout_3.addWidget(self.individualButton, 2, 0, 1, 1)
        self.groupButton = QtWidgets.QRadioButton(self.centralwidget)
        self.groupButton.setObjectName("groupButton")
        self.gridLayout_3.addWidget(self.groupButton, 3, 0, 1, 1)
        self.individaulAndgroupButton = QtWidgets.QRadioButton(self.centralwidget)
        self.individaulAndgroupButton.setObjectName("individaulAndgroupButton")
        self.gridLayout_3.addWidget(self.individaulAndgroupButton, 4, 0, 1, 1)
        self.msgAudienceButtonGroup.addButton(self.individualButton)
        self.msgAudienceButtonGroup.addButton(self.groupButton)
        self.msgAudienceButtonGroup.addButton(self.individaulAndgroupButton)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setMinimumSize(QtCore.QSize(0, 100))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_2.addWidget(self.plainTextEdit, 1, 1, 6, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 3, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 2, 0, 1, 2)
        self.numFriendsLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.numFriendsLineEdit.setObjectName("numFriendsLineEdit")
        self.gridLayout_4.addWidget(self.numFriendsLineEdit, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 1, 1, 1, 1)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.gridLayout_4.addWidget(self.listView, 4, 0, 1, 1)
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setMinimumSize(QtCore.QSize(0, 40))
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout_2.addWidget(self.cancelButton, 10, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.stop_watch_real_time_label = QtWidgets.QLabel(self.centralwidget)
        self.stop_watch_real_time_label.setMaximumSize(QtCore.QSize(16777215, 16777213))
        self.stop_watch_real_time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.stop_watch_real_time_label.setObjectName("stop_watch_real_time_label")
        self.verticalLayout_3.addWidget(self.stop_watch_real_time_label)
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setMinimumSize(QtCore.QSize(0, 40))
        self.sendButton.setObjectName("sendButton")
        self.gridLayout_2.addWidget(self.sendButton, 10, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 6, 0, 1, 1)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.msgButton.setText(_translate("MainWindow", "문자"))
        self.imgButton.setText(_translate("MainWindow", "사진"))
        self.label.setText(_translate("MainWindow", "\n""어떤 파일을 보내고 싶으신가요?"))
        self.individualButton.setText(_translate("MainWindow", "개인"))
        self.groupButton.setText(_translate("MainWindow", "단체"))
        self.individaulAndgroupButton.setText(_translate("MainWindow", "개인과 단체"))
        self.label_3.setText(_translate("MainWindow", "누구에게 메세지(문자/사진)을 보내고 싶으신가요?"))
        self.label_8.setText(_translate("MainWindow", "현재 문자를 보내게 될 그룹들의 리스트는 다음과 같습니다"))
        self.label_5.setText(_translate("MainWindow", "개인의 경우 몇 명에게메세지(문자/사진)을 보내고 싶으신가요?"))
        self.label_6.setText(_translate("MainWindow", "명"))
        self.cancelButton.setText(_translate("MainWindow", "중단하기"))
        self.label_9.setText(_translate("MainWindow", "지금 걸리고 있는 시간은 아래와 같습니다."))
        self.stop_watch_real_time_label.setText(_translate("MainWindow", "0초"))
        self.sendButton.setText(_translate("MainWindow", "전송하기"))
