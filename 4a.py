d = {1:"one", 2:"two", 3:"three"}
l = [1,2,3,4]
try:
    print(d[4])
except KeyError:
    print("Wrong Key")

try:
    print(int("wer"))
except ValueError:
    print("YOU invoked a Value Error")

try:
    print(l[10])
except IndexError:
    print("Wrong Index")

except:
    print("SOME EXCEPTION HAS OCCURED")
else:
    print("NO EXCEPTION WHAT SO EVER !")
