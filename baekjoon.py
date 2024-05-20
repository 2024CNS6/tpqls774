s = input()
while True:
    if s == '0':
        break
    if s == s[::-1]:
        print('yes')
    else:
        print('no')
    s = input()