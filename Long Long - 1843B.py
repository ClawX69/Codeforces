t = int(input())
for _ in range(t):
    n = int(input())
    value = input().split()
    values = [int(i) for i in value]
    op = 0
    flag = False
    for i in range(len(values)):
        if values[i] < 0:
            if i == n-1:
                op += 1
                continue
            flag = True
            continue
        elif values[i] > 0:
            if flag:
                op += 1
                flag = False
                continue
        else:
            if flag and i == n-1:
                op += 1
                continue
    print(sum([abs(i) for i in values]), op)

