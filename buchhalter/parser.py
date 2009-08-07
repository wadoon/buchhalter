from ply import *
import sys


#Example:
#   2000    20,00
#   2300    25,00
#   an 5000 45,00

tokens = ("FLOAT",  "SEPERATOR",  \
    "ASSET_IDENTIFIER",  "INTEGER")
t_SEPERATOR ="[ \n\t\s]+"
t_ASSET_IDENTIFIER = r'(an|to){1}'

def t_FLOAT(t):
    r'[0-9]+[,.][0-9]*'
    try:
        t.value=float( t.value.replace(',', '.') )
        return t
    except:
        print "Line %d: Number %s is not an int!" % (t.lineno,t.value)


def t_INTEGER(t):
    r'[0-9]+'
    try:
        t.value = int(t.value)
        return t
    except:
        print "Line %d: Number %s is not an int!" %(t.lineno, t.value)

def t_error(t):
    print "token error:", t

def p_error(t):
    print "parse error:",t

def p_num(t):
    r"""num : INTEGER
            | FLOAT"""
    if t[1]:
        t[0] = t[1]
    else:
        t[0] = t[2]
    return t


def p_debit(t):
    r"""debit : INTEGER SEPERATOR num"""
    t[0] = ["DEBIT",  t[1], t[3] ]
    return t

def p_asset(t):
    r"asset : ASSET_IDENTIFIER SEPERATOR debit"
    s = t[3]
    s[0] = "ASSET"
    t[0] = s
    return t


def p_accsentence(t):
    r"""accsentence : debit SEPERATOR accsentence
                    | asset SEPERATOR accsentence
                    | debit
                    | asset
    """
    if len(t) == 2:
        t[0] = [ t[1] ]
    else:
        l = t[3]
        l.append(t[1])
        t[0]=l

start = 'accsentence'
#start="asset"

lex.lex(debug=0)
yacc.yacc(debug=0)

if __name__ == "__main__":
    import sys
    if len(sys.argv)==2:
        i=sys.argv[1]
    else:
        i=str()
        while True:
            try:
                s = raw_input()
                if i:
                    i += "\n" + s
                else:
                    i = s
            except EOFError, e:
                break
            except BaseException, e:
                print e

    print "_"*80
    print i
    print "_"*80

    lex.input(i)

    while True:
        tok = lex.token()
        if tok:
            print tok
        else:
            break;

    print "-"*80
    print yacc.parse(i)
