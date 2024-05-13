sum = 0
for i in range(4):
    sum += int(input())
x = sum//60
y = sum - x*60
print(x)
print(y)