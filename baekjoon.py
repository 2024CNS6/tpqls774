import sys
input = sys.stdin.readline
n = int(input())
people = []
for i in range(n):
    [a, b] = input().split()
    people.append([int(a), b])
people.sort(key=lambda x : (x[0]))
for i in range(n):
    print(*people[i])