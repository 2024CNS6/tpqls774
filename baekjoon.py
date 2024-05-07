div = []
count = 1
a = 0

for i in range(10):
    num = int(input())
    na = num % 42
    div.append(na)
div.sort()

for n in range(9):
    if div[n] < div[n+1]:
        count += 1

print(count)