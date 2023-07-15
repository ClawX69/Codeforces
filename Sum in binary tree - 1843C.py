t = int(input())
for i in range(t):
    n = int(input())
    sum = n
    while(n!=1):
        sum += n//2
        n = n//2

    print(sum)
