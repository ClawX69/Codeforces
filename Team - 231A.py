n = int(input())
count = 0
for i in range(n):
    sub = input().split()
    if sub.count('1') >= 2:
        count += 1
    else:
        pass
print(count)