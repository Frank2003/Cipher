
def _cleanup(s):
    c=""
    a=["+","-","[","]","<",">",".",","]
    for i in s:
        if i in a:
            c=c+i
    #print(c)
    return c
        
def _check(s):
    right=0
    left=0
    i=0
    while i<len(s) and right<=left:
        if s[i]=="]":
            right+=1
        if s[i]=="[":
            left+=1
        i+=1
    return [left,right]

def _goto(i,start,s):
    right=0
    left=0
    if start=="]":
        right+=1
    if start=="[":
        left+=1
    while i>=0 and i<len(s) and left!=right:
        if start=="]":
            i-=1
        if start=="[":
            i+=1
        if s[i]=="]":
            right+=1
        if s[i]=="[":
            left+=1
    return i

def interpretbf(s,inp=""):
    "s:s"
    s=_cleanup(s)
    width=256
    cellmax=256
    i=_check(s)
    if i[0]>i[1]:
        raise BaseException("Too Much Left Paren!!!")
    elif i[0]<i[1]:
        raise BaseException("Right Paran Error!!!")
    cells=[0]*256
    i=0 #Current executing Location
    '''
    if "," in s:
        inp=raw_input("Input:")
    '''
    outp=""
    read=0
    pointer=0
    while i<len(s):
        if s[i]=="+":
            cells[pointer]+=1
        if s[i]=="-":
            cells[pointer]-=1
        if s[i]==">":
            pointer+=1
        if s[i]=="<":
            pointer-=1
        if s[i]=="]":
            i=_goto(i,"]",s)
        if s[i]=="[" and cells[pointer]==0:
            i=_goto(i,"[",s)
        if s[i]=="," and read<len(inp):
            cells[pointer]=ord(inp[read])
            read+=1
        elif s[i]==",":
            cells[pointer]=0
        if s[i]==".":
            #print "Output:",cells[pointer],chr(cells[pointer])
            outp=outp+chr(cells[pointer])
        '''
        if out_:
            print s,"\n"," "*i+"^",s[i]
        flag=0
        if out_:
            out=""
            for j in range(pointer-3,pointer+4):
                out=out+"[%d]"%(cells[j%cellmax])
                if j==pointer:
                    flag=len(out)-2
            print out,"\n"+" "*flag+"^",pointer
            sleep(delay)
        if one and out_:
            raw_input()
        '''
        cells[pointer]%=width
        pointer%=cellmax
        i+=1
    return outp

if __name__=="__main__":
    while 1:
        print(interpretbf(input()))
        #interpret(_cleanup(raw_input("Input Code :")),bool(int(raw_input("Show process?(1/0)"))),float(raw_input("Delay?")),bool(int(raw_input("1-1 Step?"))))
