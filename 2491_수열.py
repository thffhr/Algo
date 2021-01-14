N = int(input())
Arr1 = list(map(int, input().split(' ')))
Arr2 = []

for i in range(1, N):
    Arr2.append(Arr1[i-1] - Arr1[i])

maxLen = 0
for n in range(N-1):
    if Arr2[n] >= 0:
        Mcnt = 1
        for m1 in range(n, N-1):
            if Arr2[m1] >= 0:
                Mcnt += 1
            else:
                break
        if maxLen <= Mcnt:
            maxLen = Mcnt
    if Arr2[n] <= 0:
        Pcnt = 1
        for m2 in range(n, N-1):
            if Arr2[m2] <= 0:
                Pcnt += 1
            else:
                break
        if maxLen <= Pcnt:
            maxLen = Pcnt

print(maxLen)