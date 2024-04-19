t = int(input())
s = []
for i in range(t):
    a, b = input().split()
    for j in range(len(b)):
        s.append(int(a)*b[j])
    print(f"{''.join(s)}")
    s = []