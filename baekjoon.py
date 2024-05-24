s = list(input())
length = len(s)
for i in range(len(s)):
    if i == 0:
        continue
    if s[i-1] == 'c' and s[i] == '=':
        length -= 1
    elif s[i-1] == 'c' and s[i] == '-':
        length -= 1
    elif s[i-2] == 'd' and s[i-1] == 'z' and s[i] == '=':
        length -= 2
    elif s[i-1] == 'd' and s[i] == '-':
        length -= 1
    elif s[i-1] == 'l' and s[i] == 'j':
        length -= 1
    elif s[i-1] == 'n' and s[i] == 'j':
        length -= 1
    elif s[i-1] == 's' and s[i] == '=':
        length -= 1
    elif s[i-1] == 'z' and s[i] == '=':
        length -= 1

print(length)