x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if 1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8:
    if x1 == x2 or y1 == y2:
        print("YES")
    else:
        print("NO")
else:
    print("not possible")