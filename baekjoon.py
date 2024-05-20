n = int(input())
count = 0
num = list(map(int, input().split()))

for x in num:
    if x == 1:
        continue
    is_prime = True
    i = 2
    while i * i <= x:
        if x % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        count += 1

print(count)