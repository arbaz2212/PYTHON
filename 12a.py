def partition (l):
    a=[]
    b=[]
    for i in l:
        if i.upper()>='A' and i.upper()<='M':
            a.append(i)
        else:
            b.append(i)
    print('Group 1:')
    for i in a:
        print(i)
    print('Group 2:')
    for i in b:
        print(i)
print('Enter the first names of soccer players:',end='')
l=[x for x in input().split()]
partition (l)
