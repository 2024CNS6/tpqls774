n = int(input())
dt = []
for i in range(n):
    dt.append(list(map(int, input().split())))
dt.sort()
for i in range(n):
    print(*dt[i])