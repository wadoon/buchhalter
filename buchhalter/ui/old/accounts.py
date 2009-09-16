# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accounts.ui'
#
# Created: Wed Sep 16 14:36:25 2009
#      by: PyQt4 UI code generator 4.5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AccountsDialog(object):
    def setupUi(self, AccountsDialog):
        AccountsDialog.setObjectName("AccountsDialog")
        AccountsDialog.resize(497, 465)
        self.gridLayout = QtGui.QGridLayout(AccountsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(AccountsDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.line = QtGui.QFrame(AccountsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.treeView = QtGui.QTreeView(AccountsDialog)
        self.treeView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.treeView.setObjectName("treeView")
        self.horizontalLayout_2.addWidget(self.treeView)
        spacerItem2 = QtGui.QSpacerItem(2, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtGui.QPushButton(AccountsDialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(AccountsDialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(AccountsDialog)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(AccountsDialog)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.btnBook = QtGui.QPushButton(AccountsDialog)
        self.btnBook.setObjectName("btnBook")
        self.horizontalLayout_3.addWidget(self.btnBook)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(AccountsDialog)
        QtCore.QMetaObject.connectSlotsByName(AccountsDialog)

    def retranslateUi(self, AccountsDialog):
        AccountsDialog.setWindowTitle(QtGui.QApplication.translate("AccountsDialog", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setStyleSheet(QtGui.QApplication.translate("AccountsDialog", "font: 14pt sans-serif bold;", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AccountsDialog", "Accounts", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("AccountsDialog", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("AccountsDialog", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("AccountsDialog", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("AccountsDialog", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBook.setText(QtGui.QApplication.translate("AccountsDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

