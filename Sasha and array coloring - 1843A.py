t = int(input())
for _ in range(t):
    n = int(input())
    ele = input().split()
    ele = [int(i) for i in ele]
    if len(ele) == 1:
        print(0)
    else:
        if len(ele) < 4:
            print(max(ele)-min(ele))
        else:
            ele.sort()
            print(sum(ele[int((n/2)+1):n])-sum(ele[:int((n/2))]) if n%2==1 else sum(ele[int((n/2)):n])-sum(ele[:int((n/2))]))
