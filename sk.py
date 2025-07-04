#!/usr/bin/env python3
import lsk
import math
s=open('ds','r').read().split('\n')
ss={}
pss=set()
for l in s:
    p=l.split(',')
    if len(p)<2:continue
    if lsk.snl(p[1])==[]:continue
    if p[0] in ss:
        ss[p[0]]=ss[p[0]]+1
    else:ss[p[0]]=1
    if ss[p[0]]<=4:
        pss.add(p[1])
pss=[lsk.snl(l) for l in pss]
def k(s):
    n=0
    for k in range(0,len(s)):
        nn=s[k]<100
        s[k]=s[k]%100
        if s[k]<=42:s[k]=math.floor(s[k]/3)
        if not nn:s[k]=s[k]+100
        n=n*100+s[k]
    return n
pss.sort(key=lambda l:k(l))
for l in pss:
    print(l)
