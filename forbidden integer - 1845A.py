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
        if k >= 2 and n%2 == 0:
            print("YES")
            print(n//2)
            print("2 "*(n//2))
        elif k >= 3:
            print("YES")
            print(f"{n//2}")
            print("3", end=" ")
            print("2 "*((n//2)-1))
        else:
            print("NO")

