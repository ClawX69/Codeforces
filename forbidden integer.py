from itertools import *
import random
test = int(input())

for i in range(test):
    a = input()
    n = int(a.split()[0])
    k = int(a.split()[1])
    x = int(a.split()[2])
    if x != 1:
        print("YES")
        print(n)
        print("1 "*n)
    else:
        if k >= 2 and n%k == 0:
            print("YES")
            print(n//k)
            print("2 "*(n//k))
        elif k>= 3:
            print("YES")
            print(f"{n//2}")
            print("3", end=" ")
            print("2 "*((n//2)-1))
        else:
            print("NO")

