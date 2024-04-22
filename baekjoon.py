t = int(input())
count = 0
double = 0
for i in range(t):
    a = input()
    for j in range(len(a)):
        if a[j] == "O":
            double += 1
            count += double
        elif a[j] == "X":
            double = 0
    print(count)
    count = 0
    double = 0