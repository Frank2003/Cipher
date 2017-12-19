import random
ord_a=ord("a")
ord_A=ord("A")
BASES="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
HEX=BASES[:16]
def randint(a,b):
    "ii"
    return random.randint(a,b)

def ensure(a,b):
    if b=='a':
        for i in ('i','s'):
            try:
                return ensure(a,i)
            except:
                pass
    try:
        if b=='s':
            return str(a) if a!=None else '' 
        if b=='i':
            return eval(a)
        if b=='b':
            return bool(a)
    except:
        raise BaseException("Error while converting!")
    raise BaseException("Unsupported type!")

def valid(a,t):
    try:
        ensure(a,t)
        return True
    except:
        return False

