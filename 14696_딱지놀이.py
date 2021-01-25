import copy
R = int(input())
A = []
B = []
for rr in range(2*R):
    Info = list(map(int, input().split(' ')))
    Input = [0, 0, 0, 0]
    for i in range(Info[0]):
        if Info[1:][i] == 1:
            Input[0] += 1
        elif Info[1:][i] == 2:
            Input[1] += 1
        elif Info[1:][i] == 3:
            Input[2] += 1
        else:
            Input[3] += 1
    if rr == 0 or not rr%2:
        A.append(copy.deepcopy(Input))
    else:
        B.append(copy.deepcopy(Input))

Win = []
for r in range(R):
    winner = ''
    for card in range(3, -1, -1):
        if A[r][card] > B[r][card]:
            winner = 'A'
            break
        elif A[r][card] < B[r][card]:
            winner = 'B'
            break
    if winner == '':
        winner = 'D'
    Win.append(winner)

for p in range(R):
    print(Win[p])