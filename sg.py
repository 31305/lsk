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
            if l[:ns].endswith('a') or l[:ns].endswith('a/'):
                if l[lds+5]=='m':
                    pl=l[ds+3:ns]+'H\n'
                elif l[:lns].endswith('n.') and l[lds+5:lns].find('<')==-1:
                    pl=l[ds+3:ns]+'m\n'
    tp.write(pl.replace('-','').replace('\u2014',''))
