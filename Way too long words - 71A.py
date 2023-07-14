n = int(input())

for i in range(n):
    s = input()
    if len(s) <= 10:
        print(s)
    else:
        print(f"{s[0]}{len(s[1:len(s)-1])}{s[-1]}")