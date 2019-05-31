from itertools import *
def subsetsum(l,tar):
    k=list(combinations(l,3))
    for i in k:
          if sum(i) == tar:
              return True
          else:
              return False
print('Enter the elements',end='')
lst=[int(x) for x in input().split()]
t=int(input('Enter the target'))
print(subsetsum(lst,t))
