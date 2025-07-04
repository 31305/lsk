#!/usr/bin/env python3
tp=open('tpn','w')
import sys
p=''
import lsk
for l in sys.stdin:
    if 0 and l.startswith('<L>'):
        l=l.split('<k2>')[1].split('<')[0].split(';')[0]
        if l.find('/')!=-1 or l.find('^')!=-1:
            l=l.replace('\u2014','').replace('-','').replace('L','l')
            if p!=l:
                tp.write(l+'\n')
            p=l
    pl=''
    ds=l.find('<s>')
    if ds!=-1:
        ns=l.find('</s>')
        lds=l.find('<lex>')
        if lds!=-1 and l[ds+3:ns].find('<')==-1 and (l[ds+3:ns].find('/')!=-1 or l[ds+3:ns].find('^')!=-1):
            lns=l.find('</lex>')
            if l[:ns].endswith('a') or l[:ns].endswith('a/') or l[:ns].endswith('a^'):
                if l[lds+5]=='m':
                    pl=l[ds+3:ns]+'H'
                elif l[:lns].endswith('n.') and l[lds+5:lns].find('<')==-1:
                    pl=l[ds+3:ns]+'m'
            elif l[:ns].endswith('A') or l[:ns].endswith('A/') or l[:ns].endswith('A^') or l[:ns].endswith('I') or l[:ns].endswith('I/') or l[:ns].endswith('I^'):
                if l[lds+5]=='f':
                    pl=l[ds+3:ns]
            elif l[:ns].endswith('m'):
                pl=l[ds+3:ns]
            elif l[:ns].endswith('s'):
                if (l[:lns].endswith('n.') or l[:lns].endswith('ind.')) and l[lds+5:lns].find('<')==-1:
                    pl=l[ds+3:ns-1]+'H'
            elif l[:ns].endswith('u') or l[:ns].endswith('u/') or l[:ns].endswith('u^'):
                if l[lds+5]=='m':
                    pl=l[ds+3:ns]+'H'
                elif l[:lns].endswith('n.') and l[lds+5:lns].find('<')==-1:
                    pl=l[ds+3:ns]
            elif l[:ns].endswith('i') or l[:ns].endswith('i/') or l[:ns].endswith('i^'):
                if l[lds+5]=='m':
                    pl=l[ds+3:ns]+'H'
                elif l[:lns].endswith('n.') and l[lds+5:lns].find('<')==-1:
                    pl=l[ds+3:ns]
                elif l[:lns].find('f')!=-1 and l[lds+5:lns].find('<')==-1:
                    pl=l[ds+3:ns]+'H'
    pl=pl.replace('-','').replace('\u2014','')
    if len(lsk.snl(pl))==0:pl=''
    if pl!='' and pl!=p:
        tp.write(pl+'\n')
        p=pl
