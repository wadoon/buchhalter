#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, mako

from PyQt4 import *
from buchhalter import *
from buchhalter.ui import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtWebKit

from ply.lex import LexError
from ply.yacc import YaccError, SyntaxError

import  buchhalter.util as util

import logging

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, accfile=None):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

        self.journal = Journal(TAccountBook())	
	

        statusbar = self.statusBar()
        self.statusLabel = QtGui.QLabel(statusbar)
        statusbar.addPermanentWidget(self.statusLabel)
        self.setStatus = self.statusLabel.setText

	if accfile:
            print accfile
            accounts = util.loadAccountXmlFile(accfile)
            self.journal.accounts = accounts           
            print "load accounts: %s " % str(accounts) 
	    self.updateAccountTree()
        else:                                          
            self.on_actionLoad_account_file_triggered()

	self.listJournal.page(). \
	      setLinkDelegationPolicy(QtWebKit.QWebPage.DelegateAllLinks)

	self.treeAccounts.itemDoubleClicked.connect(
		  self.on_treeAccounts_itemDoubleClicked)
  
	self.btnTAccViewRef.clicked.connect(self.updateTAccountView)

#	self.actionExport_Journal.triggered.connect(self.on_btnExportJournal_clicked)

        self.mapping= {
            'revoke'  :self.revokeAccountSentence,
            'template':self.asTemplate
        }

##################

    def updateTAccountView(self):
	def render(acc):
	    s = u"<table>"
	    s += '''<tr class="bline">
			<th align="left">S</th>
			<th colspan="2" align="center">%s</th>
			<th align="right">H</th>
		    </tr>''' %unicode(acc.template)

	    def fmtd(d):
		if d: return '''<td class="debit">#%04d</td>
			      <td class="debit r" align="right">%7.2f</td>'''%d
		else: return '''<td class="debit">----</td>
			      <td class="debit r" align="right">--.--</td>'''

	    def fmta(d):
		if d: return '''<td class="asset">#%04d</td>
			      <td class="asset" align="right">%7.2f</td>'''%d
		else: return '''<td class="asset">----</td>
			      <td class="asset" align="right">--.--</td>'''

	    diff = len(acc.debit) -  len(acc.asset) 
	    debit = list(acc.debit)
	    asset = list(acc.asset)


	    if diff !=  0:
		if diff > 0:
		    asset += (None,) *  diff
		else:
		    debit += (None,) * -diff
	
	    sum_asset = 0 
	    sum_debit = 0

	    for d,a in zip( debit, asset):		
		if a:  sum_asset += a[1]
		if d:  sum_debit += d[1]
		
		s+='''<tr>%s%s</tr>'''%(fmtd(d),fmta(a))

	    if (sum_asset+sum_debit) <=0: return ""

	    s+='''<tr class="dbline">
			<td align="right" class="r" colspan="2">%18.2f</td>
			<td align="right" colspan="2">%18.2f</td>
		  </tr>''' %(sum_debit, sum_asset)	      
	    return s+"</table><br/><br/>"

	html =u"""<style>
		      table { width:100%; border-collapse:collapse;}
		      body {font-family:monospace;font-size:8pt}
		      tr.bline td, tr.bline th {border-bottom:1px solid black;}
		
		      tr.dbline td {border-bottom: 2px solid black; border-top:1px dotted black;}
		      .debit {color:green;}
		      .asset {color:red;}
		      .r     { border-right:1px solid black;}
	      </style>""";
	print self.journal.accounts
	for tpl in self.journal.accounts:
	    tacc = self.journal.getAccount(tpl.number)
	    html+=render(tacc)
	self.viewAccounts.setHtml(html)

    def updateAccountTree(self):
	self.treeAccounts.clear()

	acc2item = lambda acc: \
	    QTreeWidgetItem( QStringList( unicode("%s %s" % (acc.number, acc.common_name) ))) 

	def traverse(paccount):
	    childs = []
	    for acc in book.findSiblings(paccount.number):
		item = acc2item(acc)
		childs.append(item)
		item.addChildren( traverse(acc) )
	    return childs
	
        book = self.journal.accounts
	rootAccounts = [ acc for acc in book \
			    if acc.parent is None ]
	rootItems=[]
	for r in rootAccounts:
	    i = acc2item(r)
	    i.addChildren(traverse(r))
	    rootItems.append(i)

        self.treeAccounts.insertTopLevelItems(0,rootItems)


################
##
    def revokeAccountSentence(self, sntnc):
	ask = QtGui.QMessageBox.question(self , \
	  "Revoke?"			      , \
	  "Are you sure to revoke this record?",\
	   QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel ) 
	if ask == QtGui.QMessageBox.Ok:
	    record = sntnc.revertRecord()
	    self.journal.book(record)
	    self.updateJournalView()
	    self.updateTAccountView()

    def asTemplate(self,sntnc):
	self.txtBookSentence.setText( str(sntnc) )


###############################################################################
## SLOT:        
    @pyqtSignature('')
    def on_actionFinish_triggered(self):
	ask = QtGui.QMessageBox.question(self , \
	  "Finish?"			      , \
	  "Are you sure to make the finish of this Jounral?",\
	   QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel ) 
	if ask == QtGui.QMessageBox.Ok:
	    self.journal.finish()
	    self.updateJournalView()
	    self.updateTAccountView()

    @pyqtSignature('')
    def on_actionLoad_triggered(self):
	fil = QFileDialog.getOpenFileName(self,"Choose pickle file")
	try:
	    self.journal = util.loadJournal(str(fil))
	    self.updateAccountTree()
	    self.updateJournalView()
	    self.updateTAccountView()
	except BaseException, e:
	    logging.error(e)

    @pyqtSignature('')
    def on_actionSave_triggered(self):
	fil = QFileDialog.getSaveFileName(self,"Choose pickle file to save")
	#try:
	util.saveJournal(str(fil), self.journal )
	self.updateAccountTree()
	self.updateJournalView()
	self.updateTAccountView()
	#except BaseException, e:
	#    logging.error(e)

    @pyqtSignature('on_treeAccounts_itemDoubleClicked(QTreeWidgetItem,int)')
    def on_treeAccounts_itemDoubleClicked(self,item,column):
	logging.debug('on_treeAccounts_itemDoubleClicked(QTreeWidgetItem,int)')
	if item is None: return
	text = item.text(0)
	no,name = text.split(' ')
	self.txtBookSentence.insertPlainText(no)
	self.txtBookSentence.setFocus()

    #@pyqtSignature('on_listJournal_linkClicked(QUrl)')
    def on_listJournal_linkClicked(self, qurl):
	qurl=str( qurl.toString() )
	cmd,no=qurl.split(":")
        logging.debug("Link Clicked %s"% qurl)

	try:
	    no = int(no)
	    self.mapping[cmd](self.journal[no])
	except KeyError,e:
	    logging.error("action %s was not registered" % cmd)
	
  
    @pyqtSignature('')
    def on_btnExportJournal_clicked(self):
	filter="Html (*.html);; Text (*.txt)"
	filn = str(QtGui.QFileDialog.getSaveFileName ( self, "Export Journal", ".", \
	    filter,filter))
	if filn:
	    with open(filn, "w") as fil:
		if filn.endswith("txt"):
		    for no, acc_cmd in iter( self.journal ):
			fil.write( "#%d=========================\n%s\n" % (no ,str(acc_cmd)))
		if filn.endswith("html"):
		    fil.write(self.listJournal.page().mainFrame().toHtml())

    @pyqtSignature('')
    def updateJournalView(self):	
	#logging.debug(self.listJournal.url())
	rimg = "<img src='%s/remove.png' alt='R' />"%os.path.abspath(".")
	timg = "<img src='%s/editcopy.png' alt='T' />"%os.path.abspath(".")
        html = "<style>td {border-bottom:1px solid black;} pre{ margin:0;padding:0; }</style><table width='100%'>"
        for no,  acccmd in self.journal:
            html +="<tr><th>#%05d</th><td>"%no

	    html += "<pre style='color:green'>"
            for account,  value in acccmd._debit:
                html += "%-45s %6.2d\n" %( account,  value)
	    html +=  "</pre><pre style='color:red'>"
            for account,  value in acccmd._asset:
                html += "an %-45s %6.2d\n" %( account,  value)
#            html += str(acccmd)
            html +="</pre></td>"
            html +="<td><a href='revoke:%d'>%s</a>&nbsp;"    % (no,rimg)
            html +="<a href='template:%d'>%s</a></td>" % (no,timg)
            html +="</tr>"
        html+="</html>"
        self.listJournal.setHtml(html)

    @pyqtSignature('')
    def on_btnBook_clicked(self):
        print "btnBook pressed"
        acc = AccountingRecord()

        try:
            book = self.txtBookSentence.document().toPlainText()
            book = str(book).strip(" \n\t")
            result = util.parseSentence(book)	    
        except YaccError, e:
            QtGui.QMessageBox().warning(self, "Warning","The given input has not a well-formed format\n" + str(e) )
	    return        	

        for line in result:
            print( line )
            type,account, val = line
            if   type == 'ASSET':
                acc.asset( account, val )
            elif type == "DEBIT":
                acc.debit(account, val )

	if not result:	
            QtGui.QMessageBox().warning(self, "Balance is odd","debit and asset must have the same sum!" + str(e) )
	    return

	try: 	no = self.journal.book(acc)
	except BaseException,e: 
	    QtGui.QMessageBox().warning(self, "Accounts are not valid", str(e) )
	    return

	self.setStatus("accounting record inserted #%d"%no)
        self.txtBookSentence.document().clear()        
        self.updateJournalView(); self.updateTAccountView()
        
    @pyqtSignature('')
    def on_actionAbout_triggered(self):
	#QtGui.QMessageBox.about(self, "About this software", "test")
        a = AboutDialog()
        a.exec_()

    @pyqtSignature('')
    def on_actionAbout_Qt_triggered(self):
        QtGui.QMessageBox.aboutQt(self, "About Qt")

    @pyqtSignature('')
    def on_actionLoad_account_file_triggered(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self,
                         "Open Account File", ".", "All Files (*.*)")
        if not fileName:
            self.setStatus("user cancel")
            return
        try:
            accounts = util.loadAccountXmlFile(fileName)
	    self.journal = Journal(accounts)
            print "load accounts: %s " % str(accounts)
	    self.updateAccountTree()
	    self.updateJournalView()
	    self.updateTAccountView()
        except BaseException , e:
	    logging.error(e)
            QtGui.QMessageBox().warning(self, "Exception", str(e))

class AboutDialog(QtGui.QDialog, Ui_About):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)

if __name__=='__main__':

    logging.basicConfig( 
      level = logging.DEBUG, 
    format = "%(asctime)s [%(levelname)-8s] %(message)s" ) 

    logging.info("Program started")

    import optparse
    opts  = optparse.OptionParser()

    app = QtGui.QApplication( sys.argv )
  
    o,a = opts.parse_args(sys.argv);

    try: 		ui = MainWindow(a[1])
    except IndexError:  ui = MainWindow()

    ui.show()
    
    sys.exit(app.exec_())
