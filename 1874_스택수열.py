N = int(input())
Arr = [int(input()) for _ in range(N)]
Stack = []
AWS = []
i = 0

for n in range(1, N+1):
    Stack.append(n)
    AWS.append('+')
    while Stack:
        if Arr[i] == Stack[-1]:
            Stack.pop(-1)
            AWS.append('-')
            i += 1
        else:
            break

if Stack:
    print('NO')
else:
    for a in range(len(AWS)):
        print(AWS[a])
