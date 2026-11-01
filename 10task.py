a = int(input())
b = int(input())
c = int(input())
d = int(input())

if d - b >= 0:
    print(c - a, d - b)
elif d - b <= 0:
    print((c - a)-1, (d - b)+100)