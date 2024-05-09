n = int(input())
num = list(map(int, input().split()))
num.sort()
m = max(num)
new = []
for i in range(len(num)):
    new.append(num[i]/m*100)
print(sum(new)/n)