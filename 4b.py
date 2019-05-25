class listt:
    def __init__(self, a):
        self.l    = a
    def __add__(self, a):
        self.l = self.l + a.l
        return listt(self.l)
    def __str__(self):
        return("list obj : "+str(self.l))


l1 = listt([1,2,3,4,5])
print(l1)
l2 = listt([1,2,3])
print(l2)
l1 = l1 + l2
print(type(l1),id(l1),l1)
print(l2)
