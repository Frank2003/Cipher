from basic import ord_a,ord_A,randint
from random import choice
'''
def num(a):#ASCII
    c=0
    for i in range(len(a)-1,-1,-1):
        c+=(ord(a[i])-32)*(96**i)
    return c

def length(a):
    l=0
    while a:
        a/=2
        l+=1
    return l
'''
def rands(l,req=None,same=False):
    "s:sb"
    ""
    r=""#0
    ra=""
    ls=[]
    _0=map(str,range(10))
    _A=map(chr,range(ord_A,ord_A+26))
    _a=map(chr,range(ord_a,ord_a+26))
    __=filter(lambda a: a not in _a+_A+_0,map(chr,range(33,127)))
    if not req:
        ls=map(chr,range(33,127))
    else:
        for i in req:
            if i=="-":
                ls=map(chr,range(256))
            if i=="a" and not 'a' in ls:
                ls.extend(_a)
            if i=="A" and not 'A' in ls:
                ls.extend(_A)
            if i=='0' and not '0' in ls:
                ls.extend(_0)
            if i=="!" and not '!' in ls:
                ls.extend(__)
    if same and l>len(ls):
        raise BaseException("Length Error!")
    for i in range(l):
        ra=choice(ls)
        while ra in r and same:
            ra=choice(ls)
        r=r+ra#r+=random.randint(0,95)*(96**i)
    return r

def Char(a):#ASCII
    c=""
    while a:
        c=c+chr(a%96+32)
        a/=96
    return c

def Add(a,b,text=True):
    "ss:b"
    c=""
    t=0
    while t<len(a):
        c+=chr((ord(a[t])+ord(b[t%len(b)])-64)%96+32) if text else chr((ord(a[t])+ord(b[t%len(b)]))%256) #c+=(a+b)%96*(96**t)#a/=96#b/=96
        t+=1
    return c

def Subtract(a,b,text=True):
    "ss:b"
    c=""
    t=0
    while t<len(a):
        c+=chr((ord(a[t])-ord(b[t%len(b)]))%96+32) if text else chr((ord(a[t])-ord(b[t%len(b)]))%256) #c+=(a-b)%96*(96**t)#a/=96#b/=96
        t+=1
    return c

def shift(s,move):
    "si"
    left=0
    end=0
    first=1
    i=0
    res=""
    while move>=8:
        res+=chr(0)
        move-=8
    while move<=-8:
        i+=1
        move+=8
    if move==0: return res+s
    while 1:
        try:
            b=ord(s[i])
        except:
            b=0
        if(move>0):
            res+=chr((left<<(8-move))+(b>>move))
            left=b%(1<<move)
        if(i>=len(s)): break
        if(move<0):
            if(first):
                first=0
                left=b
            else:
                res+=chr((left<<(-move))+(b>>(8+move)))
                left=b%(1<<(8+move))
        i+=1
    return res

if __name__=="__main__":
    a="Hello!"
    key=rands(len(a))
    b=add(a,key)
    c=subtract(b,key)
    print(key,b,c)
