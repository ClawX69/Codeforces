t = int(input())
for _ in range(t):
    n,m = input().split()
    n,m = int(n), int(m)
    p1 = input().split()
    p1 = [int(i) for i in p1]
    p1.sort()
    p2 = input().split()
    p2 = [int(i) for i in p2]
    p2.sort()
    flag = True
    while True:
        if len(p1) == 0 and len(p2) == 0:
            print("Draw")
            break
        elif len(p1) == 0:
            print("Tenzing")
            break
        elif len(p2) == 0:
            print("Tsondu")
            break
        if flag:
            score1 = max(p1)-min(p2)
            score2 = min(p2)-max(p1)
            flag = False
            if score1 <= 0 and score2 <= 0:
                p1.remove(max(p1))
                p2.remove(min(p2))
            elif score1 <= 0:
                p1.remove(max(p1))
                p2[0] = score2
                p2.sort()
            else:
                p2.remove(min(p2))
                p1[-1] = score1
                p1.sort()
        else:
            score1 = max(p2)-min(p1)
            score2 = min(p1)-max(p2)
            if score1 <= 0 and score2 <= 0:
                p2.remove(max(p2))
                p1.remove(min(p1))
            elif score1 <= 0:
                p2.remove(max(p2))
                p1[0] = score2
                p1.sort()
            else:
                p1.remove(min(p1))
                p2[-1] = score1
                p2.sort()
