# -*- coding: utf-8 -*-
from __future__ import with_statement
from thread import allocate  as create_lock

import cmd
import os
import sys
import fnmatch
import codecs

from itertools import chain

__author__="Alexander Weigl"
__email__="alexweigl@gmail.com"
__date__ ="$26.12.2008$"


class TAccountTemplate(object):
    def __init__(self, number, short_name=None , 
                 common_name = None, account_type=None):
        self.number = number
        self.parent = None
        self.common_name = common_name
        self.short_name = short_name

    def createBeginRecord(self, ebk, value):
        raise NotImplemented("not yet implemented")   
        
    def __str__(self):
        return "%s (%s)" %( self.common_name,  self.number)

    def __hash__(self):
        return hash(self.number)

    def __cmp__(self,other):
	return cmp(self.number,other.number)

    def __eq__(self, other):
#        print "__eq__", self, other
        t = type(other)
        if   t is int:
            return self.number == t
        elif t is  TAccountTemplate:
            return self.number == other.number
        else:
            raise NotImplementedError

class TAccount(object):
    def __init__(self, template):
        self.template = template
        
        self.debit=[]
        self.asset=[]

    def book(self, no,  acc_cmd):
        for accNo, value  in acc_cmd._debit:
#	    print repr(accNo) , repr(self.template.number),accNo == self.template.number
            if accNo == self.template.number:
                self.debit.append( (no,value) )
        
        for accNo, value in acc_cmd._asset:
#	    print accNo , self.template.number,accNo == self.template.number
            if accNo == self.template.number:
                self.asset.append( (no, value) )        

    def sumDebit(self):
        return self.sumSide(self.debit)
    def sumAsset(self):
        return self.sumSide(self.asset)

    def sumSide(self,side):
	return sum(map(lambda x:x[1], side))        

    def finishAccount(self):
        """
        This function determines the smallest side a
        nd make a account record in the journal to  balance out the account
        """
        this   = self.template.number
        parent = self.template.parent

        asset = self.sumAsset()
        debit = self.sumDebit()
        
        diff = debit - asset
        
        # debit equals asset, no record is required??
        if diff == 0: return
        
        if parent == None:
            print "Account %s has no parent" % this
            return 
        
        acc = AccountingRecord()
        
        if diff < 0: 
            # Asset is bigger, book in debit
            diff=abs(diff)
            acc.debit( this  , diff)
            acc.asset( parent, diff)
        else:
            acc.debit( parent, diff)
            acc.asset( this  , diff)    
        return acc

    def __str__(self):        
        head = unicode(self.template).center(35)        
        out = "S"+head+"H\n"
        out += ( "_" * 37 ) + "\n"

        diff = len(self.debit) -  len(self.asset) 

        debit = list(self.debit)
        asset = list(self.asset)


        if diff !=  0:
            if diff > 0:
                asset += (None,) *  diff
            else:
                debit += (None,) * -diff
    
        sum_asset = 0 
        sum_debit = 0

        for d,a in zip( debit, asset):
            out += self.fmtLine(d) + '|' + self.fmtLine(a) + "\n"
            if a:  sum_asset += a[1]
            if d:  sum_debit += d[1]
        
        out += "-" * 37 + "\n"
        out += "%18.2f|%18.2f\n" % (sum_debit, sum_asset)
        out += "=" * 37 + "\n\n"
        return out

                
    def fmtLine(self, item):
        if item == None:
            return ' ' * 18
        return "#%04d      %7.2f" % item
                   

class TAccountBook(set):
    def __init__(self,lis=()): 
        set.__init__(self,lis)
        self.finishWay = []

    def __getitem__(self, key):
        predict = lambda x: x.number == key                
        t = filter( predict, self )
        
        if t:
            return t.pop()
        else:
            raise KeyError("No value for key %s" % key)

    def add(self, acc ):
        if not isinstance(acc, TAccountTemplate):
            raise TypeError('acc has to TAccountTemplate instance')    
        return set.add(self, acc)

    def __delitem__(self, key):
        k = self[key]
        self.taccounts.remove(k)
        del k

    def findSiblings(self,rootNo):
	return [ acc for acc in self if acc.parent==rootNo ]

class AccountingRecord(object):
    def __init__(self, debit=None , asset=None ):
            self._debit   = debit if debit else []
            self._asset   = asset if asset else []

    def asset(self, acc_no, value):
        self._asset.append( (acc_no,value)  )

    def debit(self, acc_no, value):
        self._debit.append( (acc_no, value) )


    def is_valid(self):
        #sum  = lambda list: reduce(   lambda x, y: x+y, [ x[1] for x in list ] )
        return bool( sum(self._debit) - sum(self._asset) )

    def __bool__(self):
        return self.is_valid()

    def __str__(self):
        out = '';

        for line in self._debit:
            out += "%s\t\t%10.2f\n" % line

        for line in self._asset:
            out += "an %s\t\t%10.2f\n" % line
        return out
    
    def revertRecord(self):
        return AccountingRecord(debit=self._asset, asset=self._debit)


class AutoIncrement(object):
    LOCK = create_lock()
    def __init__(self, start=0, step=1):
        self.number = start
        self.step = step

    def __call__(self, *params, **kwargs):
        try:
            AutoIncrement.LOCK.acquire()
            self.number += self.step
            return int(self.number)
        finally:
            AutoIncrement.LOCK.release()

class Journal(object):
    def __init__(self, accounts):
        self.storage=[]
        self.auto_inc=AutoIncrement()
        self.accounts = accounts

    def book(self, bookcmd):
        if not bookcmd:
            raise BaseException("book command is not valid: \n" + str(bookcmd) )
	
	nums   = [ acc.number for acc in self.accounts ]
	inv_no = [ no for no,val in chain(bookcmd._asset, bookcmd._debit) if no not in nums]

	if len(inv_no) > 0:
	    raise BaseException("record contains invalid accounts (%s)" % str(inv_no) )

        no = self.auto_inc()
        self.storage.append( ( no ,  bookcmd )  )
        return no

    def __iter__(self):
        return iter(self.storage)

    def finish(self):        
        for account in self.accounts.finishWay:
	   # print "finish: ",account
            acc = self.getAccount(account)
	    #print unicode(acc)
	    rec = acc.finishAccount()
	    if rec is not None:
		self.book( acc.finishAccount() )

    def getAccount(self, no):
         acc = TAccount(self.accounts[no])
         for record in self: acc.book(*record)
         return acc     

    def getPosition(self,pos):
         return self.storage[pos]

    def __getitem__(self,key): 
        for no, record in self:
            if no == key:
                return record
        return None

    def __len__(self):
        return len(self.storage)

    def __getslice__(self, slice):
        return self.storage.__getslice__(self,slice)

    def __delslice__(self, slice):
        for book in slice:
            del self[book]
            
    def __delitem__(self,key):
        from buchhalter.util import revertRecord
        self.book(revertRecord(self[key]))
