n = int(input())
li = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    ss = ""
    if score >= 90:
        ss += "A"
    elif score >= 80:
        ss += "B"
    elif score >= 70:
        ss += "C"
    elif score >= 60:
        ss += "D"
    else:
        ss += "F"
    li.append((name, ss, score))
li.sort(key=lambda x : (x[2], x[0]), reverse=True)
for i in li:
    print(i[0], i[1])