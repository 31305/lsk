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
def snl(ps):
	ts=[]
	for v in ps:
		if v==' ' or v=='\n':continue
		elif v=='~':
			ts[-1]+=100
		elif v=='/':
			if len(ts)>0:ts[-1]+=1
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
	return ts
def nv():
    from os import system
    ks=time.time()
    pps=''
    for ps in sys.stdin:
        if ps=='@#\n':
            ps=pps
        pps=ps
        ts=snl(ps)
        system('echo '+' '.join([str(s) for s in ts])+'|./sv 13')
def l():
    ks=time.time()
    tss=[]
    for ps in sys.stdin:
        if ps=='\n':
            break
        ts=snl(ps)
        tss+=[ts]
    l=str(int(ks))+';'
    for ts in tss:
        l+=','.join([str(v) for v in ts])
        l+=';'
    l+='\n'
    open(sys.argv[1],'a+').write(l)
def kv():
    from os import system
    import curses
    curses.initscr()
    l=open(sys.argv[2],'r').read().split('\n')
    for p in l[:-1]:
        sys.stdin.read(1)
        ts=snl(p)
        system('echo '+' '.join([str(s) for s in ts])+'|./sv 13')
    curses.endwin()
if len(sys.argv)>1:
    if sys.argv[1]=='-n':
        nv()
    elif sys.argv[1]=='-k':
        kv()
    else:l()

