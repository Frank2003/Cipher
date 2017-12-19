h="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_base(n,b):
  """ii
Switch n to base b"""
  r=""
  while n:
    r = h[n%b] + r
    n/=b
  return r

def switch_base(number,b1,b2=10):
  """si:i
Switch n from base b1 to base b2"""
  number=number.upper()
  if b1<1 or b2<1:
    raise BaseException("Illegal base!")
  n=0
  for d in number:
    n=n*b1+h.find(d)
  if b2==1: return "1"*n
  return base(n,b2)

def bases(s,mode=None,de=None):
  "s:ib"
  if not mode in [16,32,64]: mode=64
  #url="urlsafe_" if url else ""
  de="decode" if de else "encode"
  import base64
  res=""
  return eval("base64.b%d%s(%s)"%(mode,de,repr(s)))

def ascii(c):
  "s"
  return " ".join(map(lambda a:str(ord(a)),c))

def c_ascii(c):
  "s"
  return "".join(map(lambda a:chr(int(a)),c.split()))

def Hash(s,mode=None):
  "s:s"
  import hashlib
  if not mode in hashlib.algorithms:
    mode='md5'
  return eval("hashlib."+mode+"("+repr(s)+").hexdigest()")
