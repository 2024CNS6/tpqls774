import sys
input = sys.stdin.readline

n = int(input())
s = []
for i in range(n):
    s.append(input().strip())
s = list(set(s))
s.sort()
s.sort(key=lambda x : len(x))
for i in range(len(s)):
    print(s[i])