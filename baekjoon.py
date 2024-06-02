from collections import deque
n = int(input())
card_li = [i for i in range(1, n+1)]
card = deque(card_li)
for i in range(n-1):
    card.remove(card[0])
    card.rotate(-1)
result = list(card)
print(*result)