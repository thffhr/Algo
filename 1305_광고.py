L = int(input())
ad = input()
idx = 0
for i in range(1, L):
    for j in range(i):
        if ad[j] == ad[abs(j)-1]:
            idx = j
print(L-idx-1)
