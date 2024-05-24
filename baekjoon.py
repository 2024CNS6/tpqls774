n = int(input())
word = ""
word_cnt = 0
cnt = 0

for i in range(n):
    s = input()
    for j in range(len(s)):
        if j == 0:
            pass
        elif s[j] == s[j-1]:
            word_cnt += 1
        elif s[j] not in word:
            word_cnt += 1
        word += s[j]
    if word_cnt == len(s)-1:
        cnt += 1
    word_cnt = 0
    word = ""
print(cnt)