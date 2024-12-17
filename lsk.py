#!/usr/bin/env python3
import sys
vs={}
ss='aAiIuUfFxXeEoO'
for k in range(0,len(ss)):
    vs[ss[k]]=1+k*3
nss='yrlvSzshkKgGNcCjJYwWqQRtTdDnpPbBmMH`'
for k in range(0,len(nss)):
    vs[nss[k]]=43+k
for ps in sys.stdin:
    ts=[]
    for v in ps:
        if v==' ' or v=='\n':continue
        elif v=='/':
            ts[-1]+=1
        elif v=='^':
            ts[-1]+=2
        else:
            try:
                ts+=[vs[v]]
            except:
                if 1:print('!',ps)
    sn=[]
    ss=[]
    for k in range(0,len(ts)):
        if ts[k]<43:
            sn+=[ts[k]%3]
            ss+=[k]
    for k in range(1,len(sn)):
        if sn[k]==1 and sn[k-1]==2 and not (k<len(sn)-1 and (sn[k+1]!=1)):
            ts[ss[k]]+=2
    print(ts)
    
