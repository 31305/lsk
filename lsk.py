#!/usr/bin/env python3
import sys
import time
vs={}
ss='aAiIuUfFxXeEoO'
for k in range(0,len(ss)):
    vs[ss[k]]=1+k*3
nss='yrlvSzshkKgGNcCjJYwWqQRtTdDnpPbBmMH`'
for k in range(0,len(nss)):
    vs[nss[k]]=43+k
def l():
    ks=time.time()
    tss=[]
    for ps in sys.stdin:
        if ps=='\n':
            break
        ts=[]
        for v in ps:
            if v==' ' or v=='\n':continue
            elif v=='~':
                ts[-1]+=100
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
        tss+=[ts]
    l=str(ks)+';'
    for ts in tss:
        l+=','.join([str(v) for v in ts])
        l+=';'
    l+='\n'
    open('ls','a+').write(l)
def p():
    l=open('ls','r').read().split('\n')
if len(sys.argv)>1 and sys.argv[1]=='p':
    p()
else:l()

