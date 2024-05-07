n = int(input())
cnt = 0
x, s = map(int, input().split())
for i in range(n):
    c, p = map(int, input().split())
    if x >= c and p > s:
        cnt += 1
if cnt >= 1:
    print('YES')
else:
    print('NO')