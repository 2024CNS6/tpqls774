s = list(input().split())
order = 0
for i in range(len(s)):
	order += ord(s[i][0]) - ord('a') + 1
print(len(s))
print(order)