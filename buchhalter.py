#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import with_statement
from thread import allocate  as create_lock


from buchhalter import *
from buchhalter.util import *
from buchhalter.exceptions import *

import pickle as pkl
import cmd
import os
import sys
import fnmatch
import codecs

__author__="Alexander Weigl"
__email__="alexweigl@gmail.com"
__date__ ="$05.12.2008 22:06:05$"

class AccountingShell(cmd.Cmd):
    def __init__(self, accounts):
        cmd.Cmd.__init__(self)
        self.journal = Journal(accounts)

        self.cur_acc_cmd = None
        self.book_mode=False
        self.prompt = self.normal_prompt = 'input> '

        #short cuts
        self.do_ro=self.do_rollback
        self.do_co=self.do_commit
        self.do_q =self.do_quit

    def do_quit(self, commands):
        if self.book_mode:
            print 'a account record is still open'
            print 'rollback or commit the record'
            return
        sys.exit(0)

    def do_rollback(self, param ):
        if not self.book_mode:
            print "Not in book mode"
            return

        self._close_book_mode()
        print "sentence is revoked"

    def do_commit(self, param ):

        if not self.book_mode:
            print "Not in book mode"
            return
        no = self.journal.book(self.cur_acc_cmd)
        print "sentence is booked #%d" % no
        self._close_book_mode()

    def do_defineAccount(self, args):
        args = args.split(' ')


    def do_revert(self,args):
        args = args.split(' ')
        for arg in [int(x) for x in args]:
            print 'Revert %d' % arg
            del self.journal[arg]

    def do_finish(self, line):
        self.journal.finish()

    def do_save(self,line):
        filename = line.strip()+".pickle"
        with open(filename, 'w') as fh:
            pkl.dump(self.journal, fh)

    def do_load(self,line):
        filename = line.strip()+".pickle"
        with open(filename) as fh:
            self.journal = pkl.load(fh)


    def do_view(self, line ):
        args=line.split(' ')
        try:
            if args[0] == 'journal':
                self.view_journal()
            elif args[0].isdigit(): # account number
                self.view_account(  args[0] )
        except KeyError , e:
            print 'ERR: view {journal | account number}'


    def do_book(self, params):
        if not self.book_mode:
            self.prompt='book> '
            self.book_mode=True
            self.cur_acc_cmd = AccountingRecord()

    def default(self, param):
        if sys.stdin.closed: return
        if self.book_mode:
            try:
                usrInput = self.parseInput(param)
                self.push( *usrInput )
            except ( InputException , EOFError ) , e:
                print e.message, " :: line is ingored"
            except  AbortInputException, e:
                pass

    def complete_loadAccounts(self, text, line, begidx, endidx ):
            list = fnmatch.filter( os.listdir(), "%s*" % text)
            print 'no matching "%s*"'  % text
            return list

    def _close_book_mode(self):
        """returns out the book mode"""
        self.book_mode = False
        self.cur_acc_cmd = None
        self.prompt = self.normal_prompt


    def complete_revert(self, text, line, begidx, endidx):
        return fnmatch.filter(list(self.journal),"%s*"%text)

    def complete_view(self, text, line, begidx, endidx ):
        acc_no = [x.number for x in self.accounts ]
        acc_no+=('journal',)

        list = fnmatch.filter( acc_no , "%s*" % text)
        return list

    def complete_finish(self, text,line, begidx, endidx):
        return fnmatch.filter( [x.number for x in self.accounts],
                               "%s*" % text)

    def view_journal(self):
        for no, acc_cmd in iter( self.journal ):
            print "#%d=========================" % no
            print str(acc_cmd)
            print "--"

    def view_account(self, no):
        try:
            print str(self.journal.getAccount(no ))
        except KeyError, e:
            print >> sys.stderr, e.message

    def push(self, type, account, value):
        if self.cur_acc_cmd is None:
            raise BaseException('no accounting record is open')

        if   type=='H':
            self.cur_acc_cmd.asset(account,value)
        elif type=='S':
            self.cur_acc_cmd.debit(account,value)


    def parseInput(self, line):
        line = line.split(' ')
        if not ( 2 <= len(line) <= 3 ) :
            raise InputException( 'Tokens mismatch' )

        if line[0] == 'an':
            return ('H', line[1] , float(line[2]))
        else:
            return ('S', line[0] , float(line[1]))

    def help_commit(self):
        return """Adds the active record to the journal and close the book mode"""

    def help_rollback(self):
        return """Usage: rollback\n
Close the book mode without adding the current record to the journal"""

    def help_loadAccounts(self):
        return """Usage: loadAccounts <file>\n
Loads the account information from given file"""

    def help_finish(self):
        return """Usage: finish\n
Makes all account records for 'Jahresabschluss'"""

    def help_view(self):
        return """Usage: view {journal|account no}\n
If the first paramter is journal the complete journal is printed.
If a account number is given the account information is printed out"""

if __name__ == "__main__":
    import optparse

    options = optparse.OptionParser()
    options.add_option('-a','--acount-file', action="store", dest="accfile")


    opts,args = options.parse_args()

    if opts.accfile:
        accounts = loadAccountXmlFile(opts.accfile)
        print accounts
    else:
        accounts = TAccountBook()

    AccountingShell(accounts).cmdloop()

