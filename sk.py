#!/usr/bin/env python3
import lsk
import math
s=open('ds','r').read().split('\n')
ss={}
pss=set()
for l in s:
    p=l.split(',')
    if len(p)<2:continue
    if lsk.snl(p[1].replace('\\','^'))==[]:continue
    if p[0] in ss:
        ss[p[0]]=ss[p[0]]+1
    else:ss[p[0]]=1
    if ss[p[0]]<=1:
        pss.add(p[1].replace('\\','^'))
pss=[lsk.snl(l) for l in pss]
def k(s):
    n=0
    b=1
    for k in range(0,len(s)):
        p=s[k]
        nn=p<100
        p=p%100
        if p<=42:p=math.floor(p/3)
        if not nn:p=p+100
        n=n+p/b
        b=b*200
    return n
pss.sort(key=lambda l:k(l))
for l in pss:
    print(l)
