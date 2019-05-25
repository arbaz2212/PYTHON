def geometric(l):
    r = l[1] / l[0]
    for i in range(1, len(l)-1, 1):
       if l[i+1] / l[i] != r:
           return False
    return True

print(geometric([44,22,11,5.5,2.75]))
