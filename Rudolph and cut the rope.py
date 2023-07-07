n = int(input())
for i in range(n):
    values = {}
    noropes = int(input())
    count = 0
    for j in range(noropes):
        lines = input()
        a = int(lines.split()[0])
        b = int(lines.split()[1])
        values[a] = b
        if a > b:
            count += 1
    print(count)

