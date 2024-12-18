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
    l=str(int(ks))+';'
    for ts in tss:
        l+=','.join([str(v) for v in ts])
        l+=';'
    l+='\n'
    open('ls','a+').write(l)
def p():
    from os import system
    import datetime
    l=open('ls','r').read().split('\n')[0:-1]
    if len(l)==0:
        return
    k=0
    def sl():
        system('clear')
        print(str(k)+'<'+str(len(l)))
        print(datetime.datetime.fromtimestamp(int(l[k].split(';')[0])).strftime('%Y-%m-%d %H:%M:%S'))
    sl()
    while 1:
        nd=input()
        s=False
        if nd=='n':
            system('clear')
            break
        elif len(nd)>0 and nd[0]=='s':
            nd=nd[1:]
            s=True
        if nd=='':
            nd='0'
        try:
            nd=int(nd)
        except:
            continue
        if s:
            if nd<0 and abs(nd)<=len(l):
                k=len(l)+nd
            elif nd<len(l):
                k=nd
            else:continue
        else:
            if k+nd>=0 and k+nd<len(l):
                k=k+nd
            else:continue
        sl()
        tss=l[k].split(';')[1:]
        for ts in tss:
            system('echo '+' '.join(ts.split(','))+'|./sv 13')

if len(sys.argv)>1 and sys.argv[1]=='p':
    p()
else:l()

