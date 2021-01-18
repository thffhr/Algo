N = int(input())
Arr = list(map(int, input().split(' ')))

plus = minus = max_len = 0
pcnt = mcnt = 1
for n in range(1, N):
    if Arr[n-1] <= Arr[n]:
        if not plus:
            plus = 1
        pcnt += 1
    else:
        if plus and max_len < pcnt:
            max_len = pcnt
        plus = 0
        pcnt = 1

if plus and max_len < pcnt:
    max_len = pcnt


for n in range(1, N):
    if Arr[n-1] >= Arr[n]:
        if not minus:
            minus = 1
        mcnt += 1
    else:
        if minus and max_len < mcnt:
            max_len = mcnt
        minus = 0
        mcnt = 1

if minus and max_len < mcnt:
    max_len = mcnt

if N == 1:
    max_len = 1

print(max_len)