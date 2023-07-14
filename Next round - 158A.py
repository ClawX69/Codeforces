n,k = input().split()
scores = input().split()
scores = [int(i) for i in scores]
n = int(n)
k = int(k)

if sum(scores) == 0:
    print(0)
else:
    fin = list(filter(lambda x: x >= scores[k-1] and x != 0, scores))
    print(len(fin))