#substitution cipher
from basic import ord_a,ord_A

def atbash(c,raw=False):
  '''s:b
a->z b->y ... y->b z->a'''
  if raw: return raw_atbash(c)
  r=""
  d={}
  for i in range(26): d[chr(ord_a+i)]=chr(ord_a+25-i)
  for i in range(26): d[chr(ord_A+i)]=chr(ord_A+25-i)
  for i in c:
    r=r+d.get(i,i)
  return r

def raw_atbash(c):
  '''s
1->254 2->253 and so on'''
  r=""
  for i in c:
    r=r+chr(255-ord(i))
  return r

def subs(c,k,de=False,r=False):
  "ss:bb"
  r=""
  d={}
  if r:
    for i in range(256):
      if de: d[k[i]]=chr(i)
      else: d[chr(i)]=k[i]
  else:
    for i in range(26):
      if de: d[k[i]]=chr(ord_A+i)
      else: d[chr(ord_a+i)]=d[chr(ord_A+i)]=k[i]
  for i in c:
    r+=d.get(i,i)
  return r

  '''
  r=""
  d={}
  l=[chr(ord_a+i) for i in range(25)]
  for i in range(26):
    d[chr(ord_a+i)]=k[i]
    d[chr(ord_A+i)]=k[i].upper()
  for i in c:
    if i.lower() in l:
      del l[l.index(i.lower())]
    r+=d.get(i,i)
  print l
  return r
  '''

#print subs(file("a.py","r").read(),"liyfeabcdghjkmnopqrstuvwxz")
