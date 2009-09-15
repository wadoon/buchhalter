#!/usr/bin/python

import sys,os

from PyQt4 import *
from buchhalter import *
from buchhalter.ui import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

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
    def __init__(self, accfile=None):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

        self.journal = Journal(TAccountBook())

#        self.journalModel = JournalViewModel( self.journal, self.listJournal)
#        self.listJournal.setModel( self.journalModel )

        statusbar = self.statusBar()
        self.statusLabel = QtGui.QLabel(statusbar)
        statusbar.addPermanentWidget(self.statusLabel)
        self.setStatus = self.statusLabel.setText


        if accfile:
            print accfile
            accounts = util.loadAccountXmlFile(accfile)
            self.journal.accounts = accounts
            print "load accounts: %s " % str(accounts)
        else:
            self.on_actionLoad_account_file_triggered()
        
        self.actionShow_accounts.toggled.connect(
            self.toggleAccounts)

#        self.connect(self.btnBook, QtCore.SIGNAL("clicked()"),
#                     self, QtCore.SLOT("accept()"))
#        self.connect(self.cancelButton, QtCore.SIGNAL("clicked()"),
#                     self, QtCore.SLOT("reject()"))


    @pyqtSignature('')
    def on_btnBook_clicked(self):
        print "btnBook pressed"
        acc = AccountingRecord()

        book = self.txtBookSentence.document().toPlainText()

        clear = True
        for line0 in book.split("\n"):
            line = line0.split(' ')
            if not ( 2 <= len(line) <= 3 ) :
                box = QtGui.QMessageBox()
                box.setText("line '%s' is not right formatted" % line0)
                box.setInformativeText("""Only 2-3 tokens are allowed in one line
                So type for an debit: "<account> <value>"
                For an asset:         "an <account> <value" """ )
                box.setStandardButtons(QMessageBox.Ok )
                box.setDefaultButton(QMessageBox.Ok);
                box.exec_()
                clear = False
                break
            
            if line[0] == 'an':                
                acc.asset( line[1] , float(line[2]))
                print "Haben:", line[1], line[2]
            else:
                acc.debit(line[0] , float(line[1]))
                print "Soll:", line[0], line[1]

        if clear:
            print sys.getrefcount(self.journalModel)
            self.txtBookSentence.document().clear()
            self.journal.book(acc)
            self.journalModel.fireDataChanged()

    @pyqtSignature('')
    def on_actionAbout_triggered(self):
        a = AboutDialog()
        a.exec_()
    
    @pyqtSignature('')
    def toggleAccounts(self, visible):
        print "test", visible
        self.dockWidget.setVisible( visible)
#        self.actionShow_accounts.isChecked(self.dockWidget.isVisible())
        print self.dockWidget.isVisible()


    @pyqtSignature('')
    def on_actionLoad_account_file_triggered(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, 
                         "Open Account File", ".", "All Files (*.*)")

        if not fileName:
            self.setStatus("user cancel")
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
    import optparse
    opts  = optparse.OptionParser()

    app = QtGui.QApplication( sys.argv )
  
    o,a = opts.parse_args(sys.argv);
    if a:
        ui = MainWindow(a[1])
    else:
        ui = MainWindow()
    ui.show()
    
    sys.exit(app.exec_())
