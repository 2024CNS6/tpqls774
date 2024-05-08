n = int(input())
new = n
cnt = 0
while True:
    a = new//10   
    b = new - a*10
    sum = a+b
    if sum >= 10:
        c = sum//10
        d = sum - c*10
        new = b*10 + d
    else:
        new = b*10 + sum
    cnt += 1
    if new == n:
        break
print(cnt)