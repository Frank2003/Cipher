from shift import *
from base import *
from basic import *
from BFinterpreter import *
from Hex import *
from subs import *
from morse import *
from vigenere import *

#commands
d={"-h":"Help","-b":"bases","-rs":"rands","-es":"Add","-ds":"Subtract"}
#s for str
#b for bool
#i for int
args={"len":"s","eval":"s","chr":"i","int":"s:i","ord":"s"}
funcs=args.keys()

def f(n):
  's'
  _F=open(n,"r")
  res=_F.read()
  _F.close()
  return res

def o(f,a=False):
  's:b'
  sys.stdout=open(f,'a' if a else 'w')

def r(s):
  's'
  return s[::-1]

def Help():
  ''
  return """Available commands:
	Add:		s s :b
	Bin:		s :b
	Hash:		s :s
	Help:		None
	Hex:		s :b
	Subtract:	s s :b
	atbash:		s :b
	base:		s i
	caeser:		s i :b
	decrypt:	s :s :b
	dmorse:		s :s
	encrypt:	s :s :b
	f:		s
	interpretbf:	s :s
	morse:		s :s
	o:		s :b
	r:		s
	randint:	i i
	rands:		s :s :b
	raw_atbash:	s
	shift:		s i
	subs:		s s :b :b
	switch_base:	s i :i
	vigenere:	s s :b
	chr:		i
	ord:		s
	eval:		s
	len:		s
	-(skip an UNECESSARY argument)
	/(end function)
	Note:
	    s means string
	    b means boolean(-/+)
	    i means integer or expression
	    : means UNECESSARY argument	    
	Example:
	    -o out.txt -m -f exam.ple turns file exam.ple to morse code and outputs to out.txt"""
  """Available commands:('()' marks an unecessary argument)
            vigenere:       -v string key
            caeser:         -c string shift
            encrypt:        [-e|--hex] string (key) (?hex)
            decrypt:        -d string (key) (?hex)
            (decode)morse:  -(d)m word
            reverse:        -r string
            file I/O:       [-f/-o] file_name
            base64,...      -b string
            atbash          -a string (?raw)
            substitude      -s string key (?d)
            -               skip an UNECESSARY argument
            /               end function"""

def expand(s):
  if s==' ':
    return
  nes=""
  for i in s:
    if i==":":
      nes=":"
      continue
    if i=="\n":
      break
    yield nes+i

def abrv(func):
  return ''.join(map(lambda s:s[0] if s else '',func.split('_')))

def isfunc(q):
  try:
    return type(eval(q)) in [type(r),type(eval)] and eval(q+'.__doc__')!=None
  except:
    return False

def legal(f,funcs):
  try:
    identify(f,funcs)
    return True
  except:
    return False

def identify(q,funcs):
  q=q.strip('-')
  if d.get(q,False):
    return d[q]
  if len(q)==1:
    for i in funcs[funcs.index("__package__")+1:]:
      if i.startswith(q) and isfunc(i):
        return i
  for i in funcs:
    ii=i.replace('_','')
    if ii.lower().startswith(q) or ii.lower().endswith(q) or abrv(i)==q:
      if isfunc(i):
        return i
  raise BaseException("No match!")
