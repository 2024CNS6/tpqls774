al = [0 for i in range(26)]
s_1 = input()
s_2 = s_1.lower()
max_count = []

for i in range(len(s_2)):
    al[ord(s_2[i])-97] += 1

for i in range(26):
    if al[i] == max(al):
        max_count.append(max(al))
        
if len(max_count) > 1:
    print('?')
else:
    s_max = chr(al.index(max(al)) + 97)
    print(s_max.upper())