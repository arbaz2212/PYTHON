f = open("my.txt", "w")
f.writelines(["hello world wassup\nhow you doin\n hey man wassup nigga\n kunju kunju."])
f.close()
f = open("my.txt", "r")
l = f.readlines()
print(l)
c = 0
for i in l:
    k = [j for j in i.split()]
    print(k)
    c += len(k)
print("no of words =", c)
