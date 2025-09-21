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
				if 1:
				    print('!',ps,file=sys.stderr)
				    return []
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
    tss=[]
    l=''
    nv=False
    for ps in sys.stdin:
        if ps=='\n':
            break
        l+=str(int(time.time()))+';'
        for pps in ps.split(' '):
            l+=','.join([str(v) for v in snl(pps)])
            l+=';'
        if nv:l+='nv;'
        l+='\n'
        nv=True
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
def vv():
    k=0
    import pathlib
    from os import system
    ks=pathlib.Path(__file__).parent.resolve().joinpath('k')
    try:
        k=int(open(ks,'r').read())
    except:pass
    l=open(pathlib.Path(__file__).parent.resolve().joinpath('l'),'r').read().split('\n')
    if k<len(l)-1:
        ts=snl(l[k])
        system('echo '+' '.join([str(s) for s in ts])+'|'+str(pathlib.Path(__file__).parent.resolve())+'/sv 13')
        k=k+1
        open(ks,'w').write(str(k))
def sl():
    for ps in sys.stdin:
        ts=snl(ps)
        print(' '.join([str(s) for s in ts]))
if __name__ == "__main__" and len(sys.argv)>1:
    if sys.argv[1]=='-n':
        nv()
    elif sys.argv[1]=='-k':
        kv()
    elif sys.argv[1]=='-v':
        vv()
    elif sys.argv[1]=='-s':
        sl()
    else:l()

