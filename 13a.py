from re import *
def wellbracketed(s):
    l=list(s)
    lp=0
    rp=0
    for i in l:
        if i=='(':
            lp+=1
        elif i==')':
            rp+=1
        if rp>lp:
            return False
        if lp==rp:
            return True
    return False
s=input('Enter the string: ')
print(wellbracketed(s))
