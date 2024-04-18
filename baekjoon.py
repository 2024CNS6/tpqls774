num = []
for i in range(1, 29):
    num.append(int(input()))

for j in range(1, 31):
    if j not in num:
        print(j)