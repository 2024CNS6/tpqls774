n = int(input())
a = []
b = []
name = "양예성"
for i in range(n):
    if i%2 == 0:
        a.append(name[i%3])
    else:
        b.append(name[i%3])
print(f'전우진 : {''.join(a)}')
print(f'윤세욱 : {''.join(b)}')