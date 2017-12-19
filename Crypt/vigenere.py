from basic import ord_a,ord_A

def vigenere(s,y,encrypt=True):
  "ss:b"
  res=""
  s=s.lower()
  ls=len(s)
  ly=len(y)
  for i in range(ls):
    if encrypt:
      res = res + chr((ord(s[i])+ord(y[i%ly])-2*ord_a)%26+ord_A)
    else:
      res = res + chr((ord(s[i])-ord(y[i%ly]))%26+ord_A)
  return res

def caeser(s,y,encrypt=True):
  "si:b"
  return vigenere(s,chr(y+ord_a),encrypt)

'''
def raw_vigenere(s,k,encrypt=True):
  res=""
  ls=len(s)
  ly=len(k)
  for i in range(ls):
    if encrypt:
      res = res + chr((ord(c[i])+ord(y[i%ly]-64))%95+32)
    else:
      res = res + chr((ord(c[i])-ord(y[i%ly]))%95+32)
  return res
'''
