#!/usr/bin/python

import sys,os

from PyQt4 import *
from buchhalter import *
from buchhalter.ui import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtWebKit

from ply.lex import LexError
from ply.yacc import YaccError,  SyntaxError

import  buchhalter.util as util


class JournalViewModel(QAbstractTableModel):
    def __init__(self, journal, parent, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.journal = journal
        self.header = ["Accounts", "Debit" , "Asset"]

    def __len__(self):
        return  len(self.journal)

    def rowCount(self, parent):
        print "rowCount() =%d" % len(self)
        return len(self)

    def columnCount(self, parent):
        return 3

    def data(self, index, role):
        print "data() %d,%d,%d" %(index.row(),index.column(),role)
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole and role != 3:
            return QVariant()

        no,acc = self.journal.getPosition(index.row())

        c = index.column()
        d,a = acc._debit,acc._asset

        if c == 0:
            print "TEST"
            d = [ "%s"%acc for acc,val in d ]
            a = [ "an %s"%acc for acc,val in a ]
            s =  "<br>".join( d+a )
            return QVariant(s )
        elif c==1:
            d = [ "   %6.2d"%val for acc,val in d ]
            a = [ "" for acc,val in a ]
            s = "\n".join( d+a )
            return QVariant(s)

        elif c==2:
            d = [ "" for acc,val in d ]
            a = [ "   %6.2d"%val for acc,val in a ]
            s="\n".join( d+a )
            return QVariant(s)
        else:
            return QVariant("error")

    def headerData(self, col, orientation, role):

        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.header[col])
        return QVariant()

    def fireDataChanged(self):
        print "fireDataChanged()", len(self)
        i1 = self.index(0,0)
        i2 = self.index(len(self)-1,2)
        self.emit(QtCore.SIGNAL('dataChanged(const QModelIndex &,const QModelIndex  &)'), i1,i2)
        self.dataChanged.emit(i1, i2)
        print i1,i2


        self.beginInsertRows(self.index(len(self), 2), len(self), len(self)+1)
        self.endInsertRows( )



class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

        self.journal = Journal(TAccountBook())
        self.on_actionLoad_account_file_triggered()

        #self.journalModel = JournalViewModel( self.journal, self.listJournal)
        #self.listJournal.setModel( self.journalModel )

        statusbar = self.statusBar()
        self.statusLabel = QtGui.QLabel(statusbar)
        statusbar.addPermanentWidget(self.statusLabel)
        self.setStatus = self.statusLabel.setText

        self.webJournal.page().setLinkDelegationPolicy(QtWebKit.QWebPage.DelegateAllLinks)

#        self.connect(self.btnBook, QtCore.SIGNAL("clicked()"),
#                     self, QtCore.SLOT("accept()"))
#        self.connect(self.webJournal, QtCore.SIGNAL("linkClicked(QUrl)"),
#                     self.on_webJournal_linkClicked)

        QtCore.QObject.connect(self.webJournal, \
            QtCore.SIGNAL("linkClicked(QUrl)"), self.on_webJournal_linkClicked)

        QtCore.QObject.connect(self.webJournal, \
            QtCore.SIGNAL("linkClicked(QUrl)"), lambda u: sys.stdout.write(u))

    #@pyqtSignature('on_webJournal_linkClicked(QUrl)')
    def on_webJournal_linkClicked(self, qurl):
        print "Link Clicked ",  qurl

    @pyqtSignature('')
    def updateJournalView(self):
        html = "<table>"
        for no,  acccmd in self.journal:
            html +="<tr><th>#%05d</th><td><pre>"%no
            #iter over debit
#            for account,  value in acccmd._debit:
#                html += "%-45s %6.2d\n" %( account,  value)
#            for account,  value in acccmd._asset:
#                html += "an %-45s %6.2d\n" %( account,  value)
            html += str(acccmd)
            html +="</pre></td>"
            html +="<td><a href='http://b/a.html'>S%d</a></td>" % no
            html +="<td><a href=\"http://google.de\">S%d</a></td>" % no
            html +="</tr>"
        html+="</html>"
        self.webJournal.setHtml(html)

    @pyqtSignature('')
    def on_btnBook_clicked(self):
        print "btnBook pressed"
        acc = AccountingRecord()

        try:
            book = self.txtBookSentence.document().toPlainText()
            book = str(book)
            result = util.parseSentence(book)
        except YaccError, e:
            box = QtGui.QMessageBox()
            box.setText(str(e))
            box.setStandardButtons(QMessageBox.Ok )
            box.setDefaultButton(QMessageBox.Ok);
            box.exec_()
            raise
            return

        for line in result:
            print( line )
            type,account, val = line
            if   type == 'ASSET':
                acc.asset( account, val )
            elif type == "DEBIT":
                acc.debit(account, val )


        self.txtBookSentence.document().clear()
        self.journal.book(acc)
        self.updateJournalView();

    @pyqtSignature('')
    def on_actionAbout_triggered(self):
        a = AboutDialog()
        a.exec_()

    @pyqtSignature('')
    def on_actionLoad_account_file_triggered(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self,
                         "Open Account File", ".", "All Files (*.*)")

        if not fileName:
            setStatus("user cancel")
            return

        try:
            print fileName
            accounts = util.loadAccountXmlFile(fileName)
            self.journal.accounts = accounts
            print "load accounts: %s " % str(accounts)
        except BaseException , e:
            print e
            box = QtGui.QMessageBox()
            box.setText(str(e));
            box.setStandardButtons(QMessageBox.Ok )
            box.setDefaultButton(QMessageBox.Ok);
            box.exec_()


class AboutDialog(QtGui.QDialog, Ui_About):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)



if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
