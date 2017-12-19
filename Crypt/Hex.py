# -*- coding: utf-8 -*-
#T={hex(i)[2:].zfill(2).upper():chr(i) for i in range(256)}
from basic import HEX

def Hex(text,de=None):
    '''s:b
Hexizes text'''
    out=""
    if de:
        text=filter(lambda i: i in HEX,text)
        for i in range(0,len(text),2): out=out+chr(int(text[i:i+2],base=16))
    else:
        t={chr(i):hex(i)[2:].zfill(2).upper() for i in range(256)}
        for i in text: out=out+t[i]
    return out

def Bin(text,de=None):
    "s:b"
    out=""
    if de:
        text=filter(lambda i: i in "01",text)
        for i in range(0,len(text),2): out=out+chr(int(text[i:i+2],base=2))
    else:
        t={chr(i):bin(i)[2:].zfill(8) for i in range(256)}
        for i in text: out=out+t[i]
    return out

def encrypt(text,key=None,HEx=True):
    '''s:sb
Hex=True: output in hex
key="key": sets the key'''
    if key==None: key=chr(0)
    out=""
    for i in range(len(text)):
        out=out+chr((ord(text[i])+ord(key[i%len(key)]))%256)
        '''
        if Hex:
            out=out+hex((ord(text[i])+ord(key[i%len(key)]))%256)[2:].zfill(2).upper()
            #out=out+t[(ord(text[i])+ord(key[i%len(key)]))%256]
        else:
            out=out+chr((ord(text[i])+ord(key[i%len(key)]))%256)
        '''
    return Hex(out) if HEx else out

def decrypt(text,key=None,HEx=True):
    '''s:sb
Hex=True: output in hex
key="key": sets the key'''
    if key==None: key=chr(0)
    if HEx: text=Hex(text,True)
    out=""
    text=filter(lambda i: i in HEX,text)
    for i in range(0,len(text),1+Hex):
        out=out+chr(ord(text[i]-ord(key[i%len(key)])%256))
        '''
        if Hex:
            out=out+chr((int(text[i:i+2],base=16)-ord(key[(i/2)%len(key)]))%256)
            #out=out+chr((T[h:h+2]-ord(key[i%len(key)]))%256)
        else:
            out=out+chr(ord(text[i]-ord(key[i%len(key)])%256))
        '''
    return out

