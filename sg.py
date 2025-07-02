#!/usr/bin/env python3
tp=open('tp','w')
import sys
p=''
for l in sys.stdin:
    if l.startswith('<L>'):
        l=l.split('<k2>')[1].split('<')[0].split(';')[0]
        if l.find('/')!=-1 or l.find('^')!=-1:
            l=l.replace('\u2014','').replace('-','').replace('L','l')
            if p!=l:
                tp.write(l+'\n')
            p=l

