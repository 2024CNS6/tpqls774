a, b, c = map(int, input().split())
if a == 0:
    a += c*c - b
    print(a)
elif b == 0:
    b += c*c - a
    print(b)
else:
    for i in range(10**4):
        if a+b == i*i:
            print(i)