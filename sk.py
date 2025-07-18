#!/usr/bin/env python3
import lsk
import math
s=open('ds','r').read().split('\n')
ss={}
pss=set()
for l in s:
    p=l.split(',')
    if len(p)<2:continue
    p[1]=p[1].replace('\\','^')
    if lsk.snl(p[1])==[]:continue
    if p[1].find('/')==-1 and p[1].find('^')==-1:continue
    if p[0] in ss:
        ss[p[0]]=ss[p[0]]+1
    else:ss[p[0]]=1
    if p[2]=='NOM' and (1 or ((ss[p[0]]<=1 and p[3]=='SG') or (ss[p[0]]<=2 and (p[3]=='PL' or p[3]=='SG')))):
        pss.add(p[1])
pss=[(l if 0 else lsk.snl(l)) for l in pss]
def k(s):
    n=0
    b=1
    for k in range(0,len(s)):
        p=s[k]
        p=p%100
        if p<=42:p=math.floor((p-1)/3)
        elif p<=50:p=p+40
        elif p==77:p=p+20
        n=n+p/b
        b=b*200
    return n
if 1:pss.sort(key=lambda l:k(l))
ppl=False
for l in pss:
    if ppl:print(';'+','.join([str(n) for n in l])+';')
    else:print(' '.join([str(n) for n in l]))
