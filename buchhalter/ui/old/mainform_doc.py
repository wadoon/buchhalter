# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainform_doc.ui'
#
# Created: Wed Sep 16 14:36:25 2009
#      by: PyQt4 UI code generator 4.5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(605, 602)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.lblJournal = QtGui.QLabel(self.centralwidget)
        self.lblJournal.setStyleSheet("font: 14pt sans-serif bold;")
        self.lblJournal.setObjectName("lblJournal")
        self.horizontalLayout_4.addWidget(self.lblJournal)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.listJournal = QtWebKit.QWebView(self.centralwidget)
        self.listJournal.setUrl(QtCore.QUrl("about:blank"))
        self.listJournal.setObjectName("listJournal")
        self.horizontalLayout_5.addWidget(self.listJournal)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 605, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setFloating(False)
        self.dockWidget.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.dockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_2 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.label_2 = QtGui.QLabel(self.dockWidgetContents)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.treeKonten = QtGui.QTreeView(self.dockWidgetContents)
        self.treeKonten.setObjectName("treeKonten")
        self.verticalLayout_3.addWidget(self.treeKonten)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)
        self.dockWidget_3 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_3.setObjectName("dockWidget_3")
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.gridLayout_4 = QtGui.QGridLayout(self.dockWidgetContents_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label = QtGui.QLabel(self.dockWidgetContents_3)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.line = QtGui.QFrame(self.dockWidgetContents_3)
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
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.txtBookSentence = QtGui.QTextEdit(self.dockWidgetContents_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtBookSentence.sizePolicy().hasHeightForWidth())
        self.txtBookSentence.setSizePolicy(sizePolicy)
        self.txtBookSentence.setMinimumSize(QtCore.QSize(250, 100))
        self.txtBookSentence.setMaximumSize(QtCore.QSize(16777215, 100))
        self.txtBookSentence.setObjectName("txtBookSentence")
        self.horizontalLayout_2.addWidget(self.txtBookSentence)
        spacerItem5 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.btnBook = QtGui.QPushButton(self.dockWidgetContents_3)
        self.btnBook.setObjectName("btnBook")
        self.horizontalLayout_3.addWidget(self.btnBook)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget_3)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setCheckable(False)
        self.actionAbout.setObjectName("actionAbout")
        self.actionLoad_account_file = QtGui.QAction(MainWindow)
        self.actionLoad_account_file.setEnabled(False)
        self.actionLoad_account_file.setObjectName("actionLoad_account_file")
        self.actionShow_accounts = QtGui.QAction(MainWindow)
        self.actionShow_accounts.setCheckable(True)
        self.actionShow_accounts.setChecked(True)
        self.actionShow_accounts.setObjectName("actionShow_accounts")
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionShow_accounts_2 = QtGui.QAction(MainWindow)
        self.actionShow_accounts_2.setCheckable(True)
        self.actionShow_accounts_2.setChecked(True)
        self.actionShow_accounts_2.setObjectName("actionShow_accounts_2")
        self.menuFile.addAction(self.actionLoad_account_file)
        self.menuFile.addAction(self.actionShow_accounts)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.label.setBuddy(self.txtBookSentence)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.dockWidget, QtCore.SIGNAL("visibilityChanged(bool)"), self.actionShow_accounts.setChecked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.lblJournal.setText(QtGui.QApplication.translate("MainWindow", "Journal", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setStyleSheet(QtGui.QApplication.translate("MainWindow", "font: 14pt sans-serif bold;", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Kontenrahmen", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setStyleSheet(QtGui.QApplication.translate("MainWindow", "font: 14pt sans-serif bold;", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Buchungssatz", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBook.setText(QtGui.QApplication.translate("MainWindow", "Buchen", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_account_file.setText(QtGui.QApplication.translate("MainWindow", "Load account file...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_accounts.setText(QtGui.QApplication.translate("MainWindow", "Show accounts", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_accounts.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+K", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_accounts_2.setText(QtGui.QApplication.translate("MainWindow", "Show accounts", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
